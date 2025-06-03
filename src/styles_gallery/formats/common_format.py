# Universal style format specification
from typing import Dict, Any, Optional
from dataclasses import dataclass
import json
from datetime import datetime

UNIVERSAL_STYLE_SCHEMA = {
    "version": "1.0",
    "metadata": {
        "name": "Scientific Publication Style",
        "description": "IEEE standard publication style",
        "author": "System",
        "created": "2025-06-02"
    },
    "figure": {
        "size": {"width": 6.4, "height": 4.8},
        "dpi": 300,
        "background": "white"
    },
    "fonts": {
        "family": "serif",
        "size": {"default": 12, "title": 14, "label": 10},
        "weight": "normal"
    },
    "colors": {
        "palette": "viridis",
        "primary": "#1f77b4",
        "secondary": "#ff7f0e",
        "grid": "#cccccc"
    },
    "layout": {
        "margins": {"left": 0.1, "right": 0.05, "top": 0.05, "bottom": 0.1},
        "grid": {"alpha": 0.3, "linewidth": 0.5}
    }
}

@dataclass
class UniversalStyleFormat:
    """Universal style format for consistent plotting across libraries"""
    
    def __init__(self, schema: Optional[Dict[str, Any]] = None):
        self.schema = schema or UNIVERSAL_STYLE_SCHEMA.copy()
    
    def get_figure_size(self) -> tuple:
        """Get figure size as tuple (width, height)"""
        size = self.schema["figure"]["size"]
        return (size["width"], size["height"])
    
    def get_dpi(self) -> int:
        """Get figure DPI"""
        return self.schema["figure"]["dpi"]
    
    def get_font_config(self) -> Dict[str, Any]:
        """Get font configuration"""
        return self.schema["fonts"]
    
    def get_color_config(self) -> Dict[str, Any]:
        """Get color configuration"""
        return self.schema["colors"]
    
    def get_layout_config(self) -> Dict[str, Any]:
        """Get layout configuration"""
        return self.schema["layout"]
    
    def to_json(self) -> str:
        """Export style to JSON string"""
        return json.dumps(self.schema, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'UniversalStyleFormat':
        """Create style from JSON string"""
        schema = json.loads(json_str)
        return cls(schema)
    
    def save_to_file(self, filepath: str) -> None:
        """Save style to JSON file"""
        with open(filepath, 'w') as f:
            f.write(self.to_json())
    
    @classmethod
    def load_from_file(cls, filepath: str) -> 'UniversalStyleFormat':
        """Load style from JSON file"""
        with open(filepath, 'r') as f:
            json_str = f.read()
        return cls.from_json(json_str)