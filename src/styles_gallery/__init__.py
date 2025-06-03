"""Styles Gallery - Universal plotting style management"""

from .formats.common_format import UniversalStyleFormat, UNIVERSAL_STYLE_SCHEMA

__version__ = "20250602_000000_0_1_0_4"
__all__ = [
    "UniversalStyleFormat", 
    "UNIVERSAL_STYLE_SCHEMA"
]

# Optional imports that require external libraries
try:
    from .image_engine import UniversalImageEngine, save_image
    __all__.extend(["UniversalImageEngine", "save_image"])
except ImportError:
    UniversalImageEngine = None
    save_image = None

try:
    from .adapters import MatplotlibAdapter, PlotlyAdapter, BokehAdapter
    if MatplotlibAdapter:
        __all__.append("MatplotlibAdapter")
    if PlotlyAdapter:
        __all__.append("PlotlyAdapter")
    if BokehAdapter:
        __all__.append("BokehAdapter")
except ImportError:
    pass

# Advanced features
try:
    from .templates import StyleTemplateManager, ACADEMIC_STYLES, PRESENTATION_STYLES, PUBLICATION_STYLES
    __all__.extend(["StyleTemplateManager", "ACADEMIC_STYLES", "PRESENTATION_STYLES", "PUBLICATION_STYLES"])
except ImportError:
    pass

try:
    from .performance_cache import OptimizedStyleFormat, get_cache_stats, clear_all_caches
    __all__.extend(["OptimizedStyleFormat", "get_cache_stats", "clear_all_caches"])
except ImportError:
    pass