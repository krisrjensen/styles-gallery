"""Demo-compliant style templates for immediate use"""

# DEMO STANDARD TEMPLATES - IMMEDIATE USE FOR DEMO
DEMO_TEMPLATES = {
    "demo_scientific": {
        "version": "1.0",
        "metadata": {
            "name": "Demo Scientific",
            "description": "Demo-compliant scientific style",
            "category": "demo",
            "use_case": "All demo scientific plots",
            "demo_compliant": True
        },
        "figure": {
            "size": {"width": 6.4, "height": 4.8},
            "dpi": 150,
            "background": "#ffffff"
        },
        "fonts": {
            "family": "Arial",
            "size": {"default": 10, "title": 12, "label": 10, "caption": 9},
            "weight": "normal"
        },
        "colors": {
            "palette": "demo",
            "primary": "#1f77b4",
            "secondary": "#ff7f0e",
            "grid": "#cccccc"
        },
        "layout": {
            "margins": {"left": 0.1, "right": 0.05, "top": 0.05, "bottom": 0.1},
            "grid": {"alpha": 0.3, "linewidth": 0.5}
        }
    },
    
    "demo_presentation": {
        "version": "1.0",
        "metadata": {
            "name": "Demo Presentation",
            "description": "Demo-compliant presentation style",
            "category": "demo",
            "use_case": "All demo presentations and slides",
            "demo_compliant": True
        },
        "figure": {
            "size": {"width": 8.0, "height": 6.0},
            "dpi": 150,
            "background": "#ffffff"
        },
        "fonts": {
            "family": "Arial",
            "size": {"default": 12, "title": 16, "label": 11, "caption": 10},
            "weight": "normal"
        },
        "colors": {
            "palette": "demo",
            "primary": "#1f77b4",
            "secondary": "#ff7f0e",
            "grid": "#cccccc"
        },
        "layout": {
            "margins": {"left": 0.08, "right": 0.05, "top": 0.05, "bottom": 0.08},
            "grid": {"alpha": 0.3, "linewidth": 0.5}
        }
    },
    
    "demo_web_interface": {
        "version": "1.0",
        "metadata": {
            "name": "Demo Web Interface",
            "description": "Demo-compliant web interface style",
            "category": "demo",
            "use_case": "All demo web interfaces and dashboards",
            "demo_compliant": True
        },
        "figure": {
            "size": {"width": 10.0, "height": 6.0},
            "dpi": 150,
            "background": "#ffffff"
        },
        "fonts": {
            "family": "Arial",
            "size": {"default": 11, "title": 14, "label": 10, "caption": 9},
            "weight": "normal"
        },
        "colors": {
            "palette": "demo",
            "primary": "#1f77b4",
            "secondary": "#ff7f0e",
            "grid": "#cccccc"
        },
        "layout": {
            "margins": {"left": 0.06, "right": 0.04, "top": 0.04, "bottom": 0.06},
            "grid": {"alpha": 0.3, "linewidth": 0.5}
        }
    },
    
    "demo_analysis": {
        "version": "1.0",
        "metadata": {
            "name": "Demo Analysis",
            "description": "Demo-compliant analysis and ML plots",
            "category": "demo",
            "use_case": "Worker 4 analysis outputs",
            "demo_compliant": True
        },
        "figure": {
            "size": {"width": 8.0, "height": 6.0},
            "dpi": 150,
            "background": "#ffffff"
        },
        "fonts": {
            "family": "Arial",
            "size": {"default": 10, "title": 12, "label": 10, "caption": 9},
            "weight": "normal"
        },
        "colors": {
            "palette": "demo",
            "primary": "#1f77b4",
            "secondary": "#ff7f0e",
            "success": "#2ca02c",
            "grid": "#cccccc"
        },
        "layout": {
            "margins": {"left": 0.1, "right": 0.05, "top": 0.05, "bottom": 0.1},
            "grid": {"alpha": 0.3, "linewidth": 0.5}
        }
    },
    
    "demo_verification": {
        "version": "1.0",
        "metadata": {
            "name": "Demo Verification",
            "description": "Demo-compliant verification and distance plots",
            "category": "demo",
            "use_case": "Worker 5 verification outputs",
            "demo_compliant": True
        },
        "figure": {
            "size": {"width": 7.0, "height": 5.0},
            "dpi": 150,
            "background": "#ffffff"
        },
        "fonts": {
            "family": "Arial",
            "size": {"default": 10, "title": 12, "label": 10, "caption": 9},
            "weight": "normal"
        },
        "colors": {
            "palette": "demo",
            "primary": "#1f77b4",
            "secondary": "#ff7f0e",
            "grid": "#cccccc"
        },
        "layout": {
            "margins": {"left": 0.1, "right": 0.05, "top": 0.05, "bottom": 0.1},
            "grid": {"alpha": 0.3, "linewidth": 0.5}
        }
    }
}

# DEMO QUICK-APPLY FUNCTIONS
def get_demo_matplotlib_config():
    """Get matplotlib configuration for demo compliance"""
    return {
        'figure.figsize': (6.4, 4.8),
        'figure.dpi': 150,
        'figure.facecolor': '#ffffff',
        'axes.facecolor': '#ffffff',
        'axes.edgecolor': '#333333',
        'axes.linewidth': 0.8,
        'font.family': 'Arial',
        'font.size': 10,
        'axes.titlesize': 12,
        'axes.labelsize': 10,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'legend.fontsize': 9,
        'grid.alpha': 0.3,
        'grid.linewidth': 0.5,
        'grid.color': '#cccccc',
        'axes.prop_cycle': 'color: #1f77b4, #ff7f0e, #2ca02c, #d62728'
    }

def get_demo_css_styles():
    """Get CSS styles for demo compliance"""
    return """
    /* DEMO STANDARD CSS - Apply to all web interfaces */
    * {
        font-family: Arial, sans-serif !important;
    }
    
    body {
        background-color: #ffffff !important;
        color: #333333 !important;
        margin: 0;
        padding: 0;
    }
    
    .demo-header {
        background-color: #1f77b4 !important;
        color: white !important;
        padding: 10px 20px;
        font-weight: bold;
    }
    
    .demo-button {
        background-color: #1f77b4 !important;
        color: white !important;
        border: none !important;
        padding: 8px 16px !important;
        border-radius: 4px !important;
        cursor: pointer;
        font-family: Arial, sans-serif;
    }
    
    .demo-button:hover {
        background-color: #ff7f0e !important;
    }
    
    .demo-form-input {
        border: 1px solid #cccccc !important;
        padding: 8px !important;
        font-family: Arial, sans-serif !important;
        border-radius: 4px;
    }
    
    .demo-navigation {
        background-color: #1f77b4 !important;
        color: white !important;
        display: flex;
        padding: 0;
    }
    
    .demo-nav-item {
        padding: 10px 15px;
        cursor: pointer;
        border-right: 1px solid rgba(255,255,255,0.2);
    }
    
    .demo-nav-item:hover {
        background-color: #ff7f0e !important;
    }
    
    .demo-content {
        padding: 20px;
        background-color: #ffffff;
    }
    
    .demo-error {
        background-color: #d62728 !important;
        color: white !important;
        padding: 10px;
        border-radius: 4px;
        margin: 10px 0;
    }
    
    .demo-success {
        background-color: #2ca02c !important;
        color: white !important;
        padding: 10px;
        border-radius: 4px;
        margin: 10px 0;
    }
    """

def apply_demo_matplotlib_style():
    """Apply demo-compliant matplotlib styling immediately"""
    try:
        import matplotlib.pyplot as plt
        
        config = get_demo_matplotlib_config()
        plt.rcParams.update(config)
        
        # Set color cycle properly
        from cycler import cycler
        plt.rcParams['axes.prop_cycle'] = cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
        
        print("✅ Demo matplotlib styling applied")
        return True
        
    except ImportError:
        print("⚠️ matplotlib not available")
        return False

def get_demo_color_constants():
    """Get demo color constants for use in code"""
    return {
        'PRIMARY': '#1f77b4',
        'SECONDARY': '#ff7f0e', 
        'SUCCESS': '#2ca02c',
        'WARNING': '#ffbb78',
        'ERROR': '#d62728',
        'BACKGROUND': '#ffffff',
        'TEXT': '#333333',
        'GRID': '#cccccc'
    }

# EMERGENCY DEMO FIXES
EMERGENCY_MATPLOTLIB_FIX = """
# EMERGENCY MATPLOTLIB FIX - Copy/paste this to any plotting code
import matplotlib.pyplot as plt
plt.rcParams.update({
    'figure.facecolor': '#ffffff',
    'axes.facecolor': '#ffffff',
    'font.family': 'Arial',
    'font.size': 10,
    'axes.prop_cycle': plt.cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c']),
    'grid.alpha': 0.3,
    'grid.color': '#cccccc'
})
"""

EMERGENCY_CSS_FIX = """
/* EMERGENCY CSS FIX - Add to any HTML template */
<style>
* { font-family: Arial, sans-serif !important; }
body { background-color: #ffffff !important; color: #333333 !important; }
button { background-color: #1f77b4 !important; color: white !important; border: none !important; padding: 8px 16px !important; }
.header { background-color: #1f77b4 !important; color: white !important; padding: 10px; }
</style>
"""