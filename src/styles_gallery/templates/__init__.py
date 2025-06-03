"""Pre-built style templates for common use cases"""

from .academic_styles import ACADEMIC_STYLES
from .presentation_styles import PRESENTATION_STYLES
from .publication_styles import PUBLICATION_STYLES
from .demo_templates import DEMO_TEMPLATES, get_demo_matplotlib_config, get_demo_css_styles, apply_demo_matplotlib_style, get_demo_color_constants
from .template_manager import StyleTemplateManager

__all__ = [
    "ACADEMIC_STYLES",
    "PRESENTATION_STYLES", 
    "PUBLICATION_STYLES",
    "DEMO_TEMPLATES",
    "StyleTemplateManager",
    "get_demo_matplotlib_config",
    "get_demo_css_styles", 
    "apply_demo_matplotlib_style",
    "get_demo_color_constants"
]