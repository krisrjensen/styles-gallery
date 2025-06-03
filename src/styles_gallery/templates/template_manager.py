"""Template manager for style templates"""

from typing import Dict, List, Optional, Any
from ..formats.common_format import UniversalStyleFormat
from .academic_styles import ACADEMIC_STYLES
from .presentation_styles import PRESENTATION_STYLES
from .publication_styles import PUBLICATION_STYLES


class StyleTemplateManager:
    """Manager for pre-built style templates"""
    
    def __init__(self):
        self.templates = {}
        self._load_builtin_templates()
    
    def _load_builtin_templates(self):
        """Load all built-in templates"""
        self.templates.update(ACADEMIC_STYLES)
        self.templates.update(PRESENTATION_STYLES)
        self.templates.update(PUBLICATION_STYLES)
    
    def list_templates(self, category: Optional[str] = None) -> List[str]:
        """List available templates, optionally filtered by category
        
        Args:
            category: Optional category filter ('academic', 'presentation', 'publication')
            
        Returns:
            list: List of template names
        """
        if category is None:
            return list(self.templates.keys())
        
        return [
            name for name, template in self.templates.items()
            if template.get("metadata", {}).get("category") == category
        ]
    
    def get_template(self, name: str) -> Optional[UniversalStyleFormat]:
        """Get a template by name
        
        Args:
            name: Template name
            
        Returns:
            UniversalStyleFormat or None: Template style format
        """
        template_schema = self.templates.get(name)
        if template_schema:
            return UniversalStyleFormat(template_schema)
        return None
    
    def get_template_info(self, name: str) -> Optional[Dict[str, Any]]:
        """Get template metadata and information
        
        Args:
            name: Template name
            
        Returns:
            dict or None: Template metadata
        """
        template = self.templates.get(name)
        if template:
            return template.get("metadata", {})
        return None
    
    def search_templates(self, query: str) -> List[str]:
        """Search templates by name, description, or use case
        
        Args:
            query: Search query
            
        Returns:
            list: List of matching template names
        """
        query_lower = query.lower()
        matches = []
        
        for name, template in self.templates.items():
            metadata = template.get("metadata", {})
            
            # Search in name, description, and use_case
            searchable_fields = [
                name.lower(),
                metadata.get("name", "").lower(),
                metadata.get("description", "").lower(),
                metadata.get("use_case", "").lower()
            ]
            
            if any(query_lower in field for field in searchable_fields):
                matches.append(name)
        
        return matches
    
    def get_templates_by_category(self) -> Dict[str, List[str]]:
        """Get templates organized by category
        
        Returns:
            dict: Dictionary mapping categories to template lists
        """
        categories = {}
        
        for name, template in self.templates.items():
            category = template.get("metadata", {}).get("category", "uncategorized")
            if category not in categories:
                categories[category] = []
            categories[category].append(name)
        
        return categories
    
    def get_recommended_templates(self, use_case: str) -> List[str]:
        """Get recommended templates for a specific use case
        
        Args:
            use_case: Description of intended use case
            
        Returns:
            list: List of recommended template names
        """
        use_case_lower = use_case.lower()
        recommendations = []
        
        # Define use case mappings
        use_case_keywords = {
            "journal": ["ieee_standard", "nature_style", "acs_journal", "high_impact_journal"],
            "publication": ["scientific_report", "book_chapter", "white_paper"],
            "presentation": ["corporate_presentation", "slide_deck", "infographic"],
            "thesis": ["thesis_style", "book_chapter"],
            "poster": ["conference_poster", "infographic"],
            "web": ["web_display", "dashboard_style"],
            "report": ["scientific_report", "technical_manual", "white_paper"],
            "business": ["corporate_presentation", "dashboard_style", "white_paper"]
        }
        
        # Find matching templates
        for keyword, templates in use_case_keywords.items():
            if keyword in use_case_lower:
                recommendations.extend(templates)
        
        # Remove duplicates while preserving order
        return list(dict.fromkeys(recommendations))
    
    def add_custom_template(self, name: str, template_schema: Dict[str, Any]) -> bool:
        """Add a custom template
        
        Args:
            name: Template name
            template_schema: Template schema dictionary
            
        Returns:
            bool: True if added successfully
        """
        if name in self.templates:
            return False  # Template already exists
        
        # Validate basic structure
        required_fields = ["version", "figure", "fonts", "colors", "layout"]
        if not all(field in template_schema for field in required_fields):
            return False
        
        self.templates[name] = template_schema
        return True
    
    def remove_custom_template(self, name: str) -> bool:
        """Remove a custom template (cannot remove built-in templates)
        
        Args:
            name: Template name
            
        Returns:
            bool: True if removed successfully
        """
        # Check if it's a built-in template
        builtin_templates = set()
        builtin_templates.update(ACADEMIC_STYLES.keys())
        builtin_templates.update(PRESENTATION_STYLES.keys())
        builtin_templates.update(PUBLICATION_STYLES.keys())
        
        if name in builtin_templates:
            return False  # Cannot remove built-in templates
        
        if name in self.templates:
            del self.templates[name]
            return True
        
        return False
    
    def export_template(self, name: str) -> Optional[str]:
        """Export a template to JSON string
        
        Args:
            name: Template name
            
        Returns:
            str or None: JSON string of template
        """
        template = self.templates.get(name)
        if template:
            import json
            return json.dumps(template, indent=2)
        return None
    
    def import_template(self, name: str, json_string: str) -> bool:
        """Import a template from JSON string
        
        Args:
            name: Template name
            json_string: JSON string of template
            
        Returns:
            bool: True if imported successfully
        """
        try:
            import json
            template_schema = json.loads(json_string)
            return self.add_custom_template(name, template_schema)
        except (json.JSONDecodeError, ValueError):
            return False
    
    def create_style_from_template(self, template_name: str, 
                                 modifications: Optional[Dict[str, Any]] = None) -> Optional[UniversalStyleFormat]:
        """Create a style format from template with optional modifications
        
        Args:
            template_name: Name of template to use as base
            modifications: Optional modifications to apply
            
        Returns:
            UniversalStyleFormat or None: Modified style format
        """
        base_template = self.templates.get(template_name)
        if not base_template:
            return None
        
        # Create a copy of the template
        import copy
        modified_schema = copy.deepcopy(base_template)
        
        # Apply modifications if provided
        if modifications:
            self._deep_update(modified_schema, modifications)
        
        return UniversalStyleFormat(modified_schema)
    
    def _deep_update(self, base_dict: Dict[str, Any], update_dict: Dict[str, Any]) -> None:
        """Recursively update a dictionary"""
        for key, value in update_dict.items():
            if key in base_dict and isinstance(base_dict[key], dict) and isinstance(value, dict):
                self._deep_update(base_dict[key], value)
            else:
                base_dict[key] = value