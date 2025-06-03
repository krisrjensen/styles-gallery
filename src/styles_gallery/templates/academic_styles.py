"""Academic publication style templates"""

ACADEMIC_STYLES = {
    "ieee_standard": {
        "version": "1.0",
        "metadata": {
            "name": "IEEE Standard",
            "description": "IEEE publication standard style",
            "category": "academic",
            "use_case": "IEEE journal submissions"
        },
        "figure": {
            "size": {"width": 3.5, "height": 2.625},  # Single column IEEE
            "dpi": 300,
            "background": "white"
        },
        "fonts": {
            "family": "serif",
            "size": {"default": 8, "title": 10, "label": 8, "caption": 7},
            "weight": "normal"
        },
        "colors": {
            "palette": "grayscale",
            "primary": "#000000",
            "secondary": "#666666",
            "grid": "#cccccc"
        },
        "layout": {
            "margins": {"left": 0.12, "right": 0.05, "top": 0.05, "bottom": 0.12},
            "grid": {"alpha": 0.3, "linewidth": 0.5}
        }
    },
    
    "nature_style": {
        "version": "1.0",
        "metadata": {
            "name": "Nature Journal",
            "description": "Nature journal publication style",
            "category": "academic",
            "use_case": "Nature journal submissions"
        },
        "figure": {
            "size": {"width": 5.2, "height": 4.0},  # Nature single column
            "dpi": 300,
            "background": "white"
        },
        "fonts": {
            "family": "Arial",
            "size": {"default": 7, "title": 9, "label": 7, "caption": 6},
            "weight": "normal"
        },
        "colors": {
            "palette": "colorbrewer_set1",
            "primary": "#1f77b4",
            "secondary": "#ff7f0e",
            "grid": "#e0e0e0"
        },
        "layout": {
            "margins": {"left": 0.1, "right": 0.05, "top": 0.05, "bottom": 0.1},
            "grid": {"alpha": 0.2, "linewidth": 0.3}
        }
    },
    
    "acs_journal": {
        "version": "1.0",
        "metadata": {
            "name": "ACS Journal",
            "description": "American Chemical Society journal style",
            "category": "academic",
            "use_case": "ACS journal submissions"
        },
        "figure": {
            "size": {"width": 3.25, "height": 2.5},  # ACS single column
            "dpi": 300,
            "background": "white"
        },
        "fonts": {
            "family": "Times",
            "size": {"default": 8, "title": 10, "label": 8, "caption": 7},
            "weight": "normal"
        },
        "colors": {
            "palette": "viridis",
            "primary": "#2E86AB",
            "secondary": "#A23B72",
            "grid": "#d3d3d3"
        },
        "layout": {
            "margins": {"left": 0.15, "right": 0.05, "top": 0.05, "bottom": 0.15},
            "grid": {"alpha": 0.25, "linewidth": 0.4}
        }
    },
    
    "thesis_style": {
        "version": "1.0",
        "metadata": {
            "name": "Thesis Standard",
            "description": "Standard thesis/dissertation style",
            "category": "academic",
            "use_case": "PhD thesis and dissertations"
        },
        "figure": {
            "size": {"width": 6.0, "height": 4.5},  # Larger for thesis
            "dpi": 300,
            "background": "white"
        },
        "fonts": {
            "family": "serif",
            "size": {"default": 11, "title": 14, "label": 10, "caption": 9},
            "weight": "normal"
        },
        "colors": {
            "palette": "tab10",
            "primary": "#1f77b4",
            "secondary": "#ff7f0e",
            "grid": "#cccccc"
        },
        "layout": {
            "margins": {"left": 0.1, "right": 0.05, "top": 0.05, "bottom": 0.1},
            "grid": {"alpha": 0.3, "linewidth": 0.5}
        }
    },
    
    "conference_poster": {
        "version": "1.0",
        "metadata": {
            "name": "Conference Poster",
            "description": "Style for conference poster figures",
            "category": "academic",
            "use_case": "Conference posters and presentations"
        },
        "figure": {
            "size": {"width": 8.0, "height": 6.0},  # Large for posters
            "dpi": 150,  # Lower DPI for posters
            "background": "white"
        },
        "fonts": {
            "family": "sans-serif",
            "size": {"default": 14, "title": 18, "label": 12, "caption": 11},
            "weight": "bold"
        },
        "colors": {
            "palette": "bright",
            "primary": "#E31A1C",
            "secondary": "#1F78B4",
            "grid": "#888888"
        },
        "layout": {
            "margins": {"left": 0.08, "right": 0.05, "top": 0.05, "bottom": 0.08},
            "grid": {"alpha": 0.4, "linewidth": 0.8}
        }
    }
}