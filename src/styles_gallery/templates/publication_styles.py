"""Publication and report style templates"""

PUBLICATION_STYLES = {
    "scientific_report": {
        "version": "1.0",
        "metadata": {
            "name": "Scientific Report",
            "description": "General scientific report style",
            "category": "publication",
            "use_case": "Scientific reports and technical documentation"
        },
        "figure": {
            "size": {"width": 6.4, "height": 4.8},
            "dpi": 300,
            "background": "white"
        },
        "fonts": {
            "family": "Computer Modern",
            "size": {"default": 10, "title": 12, "label": 9, "caption": 8},
            "weight": "normal"
        },
        "colors": {
            "palette": "scientific",
            "primary": "#1f77b4",
            "secondary": "#ff7f0e",
            "grid": "#cccccc"
        },
        "layout": {
            "margins": {"left": 0.1, "right": 0.05, "top": 0.05, "bottom": 0.1},
            "grid": {"alpha": 0.3, "linewidth": 0.5}
        }
    },
    
    "book_chapter": {
        "version": "1.0",
        "metadata": {
            "name": "Book Chapter",
            "description": "Style for book chapters and textbooks",
            "category": "publication",
            "use_case": "Academic books and textbook chapters"
        },
        "figure": {
            "size": {"width": 5.0, "height": 3.75},
            "dpi": 300,
            "background": "white"
        },
        "fonts": {
            "family": "Times New Roman",
            "size": {"default": 9, "title": 11, "label": 8, "caption": 7},
            "weight": "normal"
        },
        "colors": {
            "palette": "monochrome",
            "primary": "#000000",
            "secondary": "#666666",
            "grid": "#dddddd"
        },
        "layout": {
            "margins": {"left": 0.12, "right": 0.05, "top": 0.05, "bottom": 0.12},
            "grid": {"alpha": 0.25, "linewidth": 0.4}
        }
    },
    
    "technical_manual": {
        "version": "1.0",
        "metadata": {
            "name": "Technical Manual",
            "description": "Style for technical manuals and documentation",
            "category": "publication",
            "use_case": "Technical manuals and user guides"
        },
        "figure": {
            "size": {"width": 6.0, "height": 4.0},
            "dpi": 200,
            "background": "white"
        },
        "fonts": {
            "family": "Helvetica",
            "size": {"default": 10, "title": 12, "label": 9, "caption": 8},
            "weight": "normal"
        },
        "colors": {
            "palette": "technical",
            "primary": "#2E4057",  # Dark blue-gray
            "secondary": "#048A81",  # Teal
            "grid": "#e0e0e0"
        },
        "layout": {
            "margins": {"left": 0.1, "right": 0.05, "top": 0.05, "bottom": 0.1},
            "grid": {"alpha": 0.3, "linewidth": 0.5}
        }
    },
    
    "white_paper": {
        "version": "1.0",
        "metadata": {
            "name": "White Paper",
            "description": "Professional white paper style",
            "category": "publication",
            "use_case": "Business white papers and research reports"
        },
        "figure": {
            "size": {"width": 7.0, "height": 5.0},
            "dpi": 300,
            "background": "white"
        },
        "fonts": {
            "family": "Calibri",
            "size": {"default": 11, "title": 14, "label": 10, "caption": 9},
            "weight": "normal"
        },
        "colors": {
            "palette": "professional",
            "primary": "#17365D",  # Professional navy
            "secondary": "#5B9BD5",  # Professional blue
            "grid": "#d6d6d6"
        },
        "layout": {
            "margins": {"left": 0.08, "right": 0.05, "top": 0.05, "bottom": 0.08},
            "grid": {"alpha": 0.25, "linewidth": 0.4}
        }
    },
    
    "patent_figure": {
        "version": "1.0",
        "metadata": {
            "name": "Patent Figure",
            "description": "Style for patent application figures",
            "category": "publication",
            "use_case": "Patent applications and IP documentation"
        },
        "figure": {
            "size": {"width": 6.5, "height": 8.5},  # Patent page size
            "dpi": 300,
            "background": "white"
        },
        "fonts": {
            "family": "Arial",
            "size": {"default": 8, "title": 10, "label": 7, "caption": 6},
            "weight": "normal"
        },
        "colors": {
            "palette": "patent",
            "primary": "#000000",  # Black only for patents
            "secondary": "#000000",
            "grid": "#000000"
        },
        "layout": {
            "margins": {"left": 0.15, "right": 0.1, "top": 0.1, "bottom": 0.15},
            "grid": {"alpha": 0.5, "linewidth": 0.8}
        }
    },
    
    "high_impact_journal": {
        "version": "1.0",
        "metadata": {
            "name": "High Impact Journal",
            "description": "Style for high-impact scientific journals",
            "category": "publication",
            "use_case": "Science, Cell, Nature-level publications"
        },
        "figure": {
            "size": {"width": 4.5, "height": 3.375},  # Compact high-impact
            "dpi": 300,
            "background": "white"
        },
        "fonts": {
            "family": "Helvetica Neue",
            "size": {"default": 6, "title": 8, "label": 6, "caption": 5},
            "weight": "normal"
        },
        "colors": {
            "palette": "high_contrast",
            "primary": "#000000",
            "secondary": "#E74C3C",  # High-impact red
            "grid": "#f0f0f0"
        },
        "layout": {
            "margins": {"left": 0.12, "right": 0.05, "top": 0.05, "bottom": 0.12},
            "grid": {"alpha": 0.2, "linewidth": 0.3}
        }
    }
}