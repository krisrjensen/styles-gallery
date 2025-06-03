"""Performance optimization and caching for styles gallery"""

import time
import hashlib
import json
import weakref
from typing import Dict, Any, Optional, Tuple, Union
from functools import wraps, lru_cache
from datetime import datetime, timedelta
import threading
from pathlib import Path

from .formats.common_format import UniversalStyleFormat


class StyleCache:
    """High-performance caching for style formats and configurations"""
    
    def __init__(self, max_size: int = 1000, ttl_seconds: int = 3600):
        self.max_size = max_size
        self.ttl_seconds = ttl_seconds
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.access_times: Dict[str, float] = {}
        self.lock = threading.RLock()
        
    def _generate_key(self, *args, **kwargs) -> str:
        """Generate cache key from arguments"""
        key_data = {
            'args': args,
            'kwargs': sorted(kwargs.items())
        }
        key_str = json.dumps(key_data, sort_keys=True, default=str)
        return hashlib.md5(key_str.encode()).hexdigest()
    
    def get(self, key: str) -> Optional[Any]:
        """Get item from cache"""
        with self.lock:
            if key not in self.cache:
                return None
            
            entry = self.cache[key]
            
            # Check TTL
            if time.time() - entry['timestamp'] > self.ttl_seconds:
                del self.cache[key]
                del self.access_times[key]
                return None
            
            # Update access time
            self.access_times[key] = time.time()
            return entry['value']
    
    def put(self, key: str, value: Any) -> None:
        """Put item in cache"""
        with self.lock:
            # Evict if at capacity
            if len(self.cache) >= self.max_size and key not in self.cache:
                self._evict_lru()
            
            self.cache[key] = {
                'value': value,
                'timestamp': time.time()
            }
            self.access_times[key] = time.time()
    
    def _evict_lru(self) -> None:
        """Evict least recently used item"""
        if not self.access_times:
            return
        
        lru_key = min(self.access_times.keys(), key=lambda k: self.access_times[k])
        del self.cache[lru_key]
        del self.access_times[lru_key]
    
    def clear(self) -> None:
        """Clear all cache entries"""
        with self.lock:
            self.cache.clear()
            self.access_times.clear()
    
    def size(self) -> int:
        """Get current cache size"""
        return len(self.cache)
    
    def stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        with self.lock:
            now = time.time()
            expired_count = sum(
                1 for entry in self.cache.values()
                if now - entry['timestamp'] > self.ttl_seconds
            )
            
            return {
                'size': len(self.cache),
                'max_size': self.max_size,
                'expired_entries': expired_count,
                'hit_ratio': getattr(self, '_hit_count', 0) / max(getattr(self, '_access_count', 1), 1)
            }


# Global cache instance
_style_cache = StyleCache()


def cached_style(ttl_seconds: int = 3600):
    """Decorator for caching style operations"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate cache key
            cache_key = _style_cache._generate_key(func.__name__, *args, **kwargs)
            
            # Try to get from cache
            cached_result = _style_cache.get(cache_key)
            if cached_result is not None:
                return cached_result
            
            # Compute result and cache it
            result = func(*args, **kwargs)
            _style_cache.put(cache_key, result)
            
            return result
        return wrapper
    return decorator


class OptimizedStyleFormat(UniversalStyleFormat):
    """Performance-optimized version of UniversalStyleFormat"""
    
    def __init__(self, schema: Optional[Dict[str, Any]] = None):
        super().__init__(schema)
        self._computed_cache = {}
        self._schema_hash = self._compute_schema_hash()
    
    def _compute_schema_hash(self) -> str:
        """Compute hash of schema for cache invalidation"""
        schema_str = json.dumps(self.schema, sort_keys=True)
        return hashlib.md5(schema_str.encode()).hexdigest()
    
    def _invalidate_cache_if_needed(self) -> None:
        """Invalidate cache if schema has changed"""
        current_hash = self._compute_schema_hash()
        if current_hash != self._schema_hash:
            self._computed_cache.clear()
            self._schema_hash = current_hash
    
    @cached_style(ttl_seconds=3600)
    def get_figure_size(self) -> Tuple[float, float]:
        """Cached version of get_figure_size"""
        self._invalidate_cache_if_needed()
        
        cache_key = 'figure_size'
        if cache_key in self._computed_cache:
            return self._computed_cache[cache_key]
        
        result = super().get_figure_size()
        self._computed_cache[cache_key] = result
        return result
    
    @cached_style(ttl_seconds=3600)
    def get_font_config(self) -> Dict[str, Any]:
        """Cached version of get_font_config"""
        self._invalidate_cache_if_needed()
        
        cache_key = 'font_config'
        if cache_key in self._computed_cache:
            return self._computed_cache[cache_key]
        
        result = super().get_font_config()
        self._computed_cache[cache_key] = result
        return result
    
    @cached_style(ttl_seconds=3600)
    def get_color_config(self) -> Dict[str, Any]:
        """Cached version of get_color_config"""
        self._invalidate_cache_if_needed()
        
        cache_key = 'color_config'
        if cache_key in self._computed_cache:
            return self._computed_cache[cache_key]
        
        result = super().get_color_config()
        self._computed_cache[cache_key] = result
        return result


class LazyStyleLoader:
    """Lazy loading for style templates and configurations"""
    
    def __init__(self):
        self._loaded_templates = {}
        self._template_refs = weakref.WeakValueDictionary()
        self.load_times = {}
    
    def get_template(self, template_name: str) -> Optional[UniversalStyleFormat]:
        """Lazily load and cache template"""
        # Check weak reference cache first
        if template_name in self._template_refs:
            return self._template_refs[template_name]
        
        # Check if we've loaded it before
        if template_name in self._loaded_templates:
            style = OptimizedStyleFormat(self._loaded_templates[template_name])
            self._template_refs[template_name] = style
            return style
        
        # Load template (this would interface with template manager)
        try:
            from .templates.template_manager import StyleTemplateManager
            manager = StyleTemplateManager()
            template_schema = manager.templates.get(template_name)
            
            if template_schema:
                self._loaded_templates[template_name] = template_schema
                self.load_times[template_name] = time.time()
                
                style = OptimizedStyleFormat(template_schema)
                self._template_refs[template_name] = style
                return style
            
        except ImportError:
            pass  # Template manager not available
        
        return None
    
    def preload_templates(self, template_names: list) -> None:
        """Preload multiple templates for better performance"""
        for template_name in template_names:
            self.get_template(template_name)
    
    def clear_old_templates(self, max_age_seconds: int = 7200) -> int:
        """Clear templates older than specified age"""
        current_time = time.time()
        old_templates = []
        
        for template_name, load_time in self.load_times.items():
            if current_time - load_time > max_age_seconds:
                old_templates.append(template_name)
        
        for template_name in old_templates:
            self._loaded_templates.pop(template_name, None)
            self.load_times.pop(template_name, None)
        
        return len(old_templates)


class PerformanceMonitor:
    """Monitor performance metrics for styles gallery"""
    
    def __init__(self):
        self.metrics = {
            'style_creation_times': [],
            'cache_hits': 0,
            'cache_misses': 0,
            'template_loads': 0,
            'image_saves': 0
        }
        self.start_time = time.time()
    
    def record_style_creation(self, creation_time: float) -> None:
        """Record style creation time"""
        self.metrics['style_creation_times'].append(creation_time)
        # Keep only last 1000 measurements
        if len(self.metrics['style_creation_times']) > 1000:
            self.metrics['style_creation_times'].pop(0)
    
    def record_cache_hit(self) -> None:
        """Record cache hit"""
        self.metrics['cache_hits'] += 1
    
    def record_cache_miss(self) -> None:
        """Record cache miss"""
        self.metrics['cache_misses'] += 1
    
    def record_template_load(self) -> None:
        """Record template load"""
        self.metrics['template_loads'] += 1
    
    def record_image_save(self) -> None:
        """Record image save operation"""
        self.metrics['image_saves'] += 1
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Get comprehensive performance report"""
        uptime = time.time() - self.start_time
        creation_times = self.metrics['style_creation_times']
        
        report = {
            'uptime_seconds': uptime,
            'cache_performance': {
                'hit_rate': self.metrics['cache_hits'] / max(
                    self.metrics['cache_hits'] + self.metrics['cache_misses'], 1
                ),
                'total_hits': self.metrics['cache_hits'],
                'total_misses': self.metrics['cache_misses']
            },
            'style_creation': {
                'total_creations': len(creation_times),
                'average_time': sum(creation_times) / max(len(creation_times), 1),
                'min_time': min(creation_times) if creation_times else 0,
                'max_time': max(creation_times) if creation_times else 0
            },
            'operations': {
                'template_loads': self.metrics['template_loads'],
                'image_saves': self.metrics['image_saves']
            },
            'memory_usage': self._get_memory_usage()
        }
        
        return report
    
    def _get_memory_usage(self) -> Dict[str, Any]:
        """Get memory usage information"""
        try:
            import psutil
            process = psutil.Process()
            memory_info = process.memory_info()
            
            return {
                'rss_mb': memory_info.rss / 1024 / 1024,
                'vms_mb': memory_info.vms / 1024 / 1024,
                'available': True
            }
        except ImportError:
            return {'available': False, 'error': 'psutil not installed'}


# Global instances
_lazy_loader = LazyStyleLoader()
_performance_monitor = PerformanceMonitor()


def optimize_for_batch_processing():
    """Optimize settings for batch processing scenarios"""
    global _style_cache
    
    # Increase cache size for batch operations
    _style_cache.max_size = 5000
    _style_cache.ttl_seconds = 7200  # 2 hours
    
    # Preload common templates
    common_templates = [
        'ieee_standard', 'nature_style', 'scientific_report',
        'corporate_presentation', 'slide_deck'
    ]
    _lazy_loader.preload_templates(common_templates)


def get_cache_stats() -> Dict[str, Any]:
    """Get comprehensive cache statistics"""
    return {
        'style_cache': _style_cache.stats(),
        'template_cache': {
            'loaded_templates': len(_lazy_loader._loaded_templates),
            'weak_references': len(_lazy_loader._template_refs)
        },
        'performance': _performance_monitor.get_performance_report()
    }


def clear_all_caches():
    """Clear all caches to free memory"""
    _style_cache.clear()
    _lazy_loader._loaded_templates.clear()
    _lazy_loader._template_refs.clear()
    _lazy_loader.load_times.clear()


def performance_benchmark(func):
    """Decorator to benchmark function performance"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        _performance_monitor.record_style_creation(execution_time)
        
        return result
    return wrapper