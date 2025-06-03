"""Presentation and business style templates"""

PRESENTATION_STYLES = {
    "corporate_presentation": {
        "version": "1.0",
        "metadata": {
            "name": "Corporate Presentation",
            "description": "Professional corporate presentation style",
            "category": "presentation",
            "use_case": "Business presentations and reports"
        },
        "figure": {
            "size": {"width": 8.0, "height": 6.0},
            "dpi": 150,
            "background": "white"
        },
        "fonts": {
            "family": "Arial",
            "size": {"default": 12, "title": 16, "label": 11, "caption": 10},
            "weight": "normal"
        },
        "colors": {
            "palette": "corporate",
            "primary": "#003366",  # Corporate blue
            "secondary": "#FF6600",  # Corporate orange
            "grid": "#e6e6e6"
        },
        "layout": {
            "margins": {"left": 0.08, "right": 0.05, "top": 0.05, "bottom": 0.08},
            "grid": {"alpha": 0.3, "linewidth": 0.5}
        }
    },
    
    "slide_deck": {
        "version": "1.0",
        "metadata": {
            "name": "Slide Deck",
            "description": "Optimized for PowerPoint/slide presentations",
            "category": "presentation",
            "use_case": "PowerPoint and slide presentations"
        },
        "figure": {
            "size": {"width": 10.0, "height": 7.5},  # 4:3 aspect ratio
            "dpi": 96,  # Screen resolution
            "background": "white"
        },
        "fonts": {
            "family": "Calibri",
            "size": {"default": 14, "title": 18, "label": 12, "caption": 11},
            "weight": "normal"
        },
        "colors": {
            "palette": "office",
            "primary": "#4472C4",  # Office blue
            "secondary": "#E7E6E6",  # Office gray
            "grid": "#d9d9d9"
        },
        "layout": {
            "margins": {"left": 0.06, "right": 0.04, "top": 0.04, "bottom": 0.06},
            "grid": {"alpha": 0.25, "linewidth": 0.4}
        }
    },
    
    "dashboard_style": {
        "version": "1.0",
        "metadata": {
            "name": "Dashboard",
            "description": "Style for executive dashboards",
            "category": "presentation",
            "use_case": "Executive dashboards and KPI displays"
        },
        "figure": {
            "size": {"width": 12.0, "height": 8.0},  # Wide format
            "dpi": 100,
            "background": "#f8f9fa"  # Light gray background
        },
        "fonts": {
            "family": "Segoe UI",
            "size": {"default": 11, "title": 14, "label": 10, "caption": 9},
            "weight": "normal"
        },
        "colors": {
            "palette": "dashboard",
            "primary": "#28a745",  # Success green
            "secondary": "#dc3545",  # Alert red
            "grid": "#dee2e6"
        },
        "layout": {
            "margins": {"left": 0.05, "right": 0.03, "top": 0.03, "bottom": 0.05},
            "grid": {"alpha": 0.2, "linewidth": 0.3}
        }
    },
    
    "infographic": {
        "version": "1.0",
        "metadata": {
            "name": "Infographic",
            "description": "Colorful style for infographics",
            "category": "presentation",
            "use_case": "Infographics and visual communications"
        },
        "figure": {
            "size": {"width": 8.0, "height": 10.0},  # Portrait orientation
            "dpi": 150,
            "background": "white"
        },
        "fonts": {
            "family": "Open Sans",
            "size": {"default": 13, "title": 20, "label": 11, "caption": 10},
            "weight": "bold"
        },
        "colors": {
            "palette": "vibrant",
            "primary": "#FF5733",  # Vibrant orange
            "secondary": "#3498DB",  # Vibrant blue
            "grid": "#ecf0f1"
        },
        "layout": {
            "margins": {"left": 0.06, "right": 0.04, "top": 0.04, "bottom": 0.06},
            "grid": {"alpha": 0.15, "linewidth": 0.2}
        }
    },
    
    "web_display": {
        "version": "1.0",
        "metadata": {
            "name": "Web Display",
            "description": "Optimized for web display and social media",
            "category": "presentation",
            "use_case": "Web graphics and social media posts"
        },
        "figure": {
            "size": {"width": 8.0, "height": 8.0},  # Square format
            "dpi": 72,  # Web resolution
            "background": "white"
        },
        "fonts": {
            "family": "Roboto",
            "size": {"default": 12, "title": 16, "label": 10, "caption": 9},
            "weight": "normal"
        },
        "colors": {
            "palette": "web_safe",
            "primary": "#007bff",  # Bootstrap blue
            "secondary": "#6c757d",  # Bootstrap gray
            "grid": "#e9ecef"
        },
        "layout": {
            "margins": {"left": 0.08, "right": 0.05, "top": 0.05, "bottom": 0.08},
            "grid": {"alpha": 0.2, "linewidth": 0.3}
        }
    }
}