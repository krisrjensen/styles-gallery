"""Pre-built style templates for common use cases"""

from .academic_styles import ACADEMIC_STYLES
from .presentation_styles import PRESENTATION_STYLES
from .publication_styles import PUBLICATION_STYLES
from .template_manager import StyleTemplateManager

__all__ = [
    "ACADEMIC_STYLES",
    "PRESENTATION_STYLES", 
    "PUBLICATION_STYLES",
    "StyleTemplateManager"
]