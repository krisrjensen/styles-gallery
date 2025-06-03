"""Matplotlib adapter for universal style format"""

from typing import Dict, Any, Optional
import matplotlib.pyplot as plt
import matplotlib as mpl
from ..formats.common_format import UniversalStyleFormat


class MatplotlibAdapter:
    """Adapter to apply universal styles to matplotlib figures"""
    
    def __init__(self, style_format: Optional[UniversalStyleFormat] = None):
        self.style_format = style_format or UniversalStyleFormat()
    
    def apply_style(self, fig: Optional[plt.Figure] = None, ax: Optional[plt.Axes] = None) -> None:
        """Apply universal style to matplotlib figure/axes"""
        
        # Apply to current figure if none provided
        if fig is None:
            fig = plt.gcf()
        if ax is None:
            ax = plt.gca()
        
        # Set figure properties
        figure_config = self.style_format.schema["figure"]
        fig.set_size_inches(figure_config["size"]["width"], figure_config["size"]["height"])
        fig.set_dpi(figure_config["dpi"])
        fig.patch.set_facecolor(figure_config["background"])
        
        # Set font properties
        font_config = self.style_format.get_font_config()
        plt.rcParams.update({
            'font.family': font_config["family"],
            'font.size': font_config["size"]["default"],
            'axes.titlesize': font_config["size"]["title"],
            'axes.labelsize': font_config["size"]["label"],
            'font.weight': font_config["weight"]
        })
        
        # Set color properties
        color_config = self.style_format.get_color_config()
        ax.set_facecolor(figure_config["background"])
        
        # Set grid properties
        layout_config = self.style_format.get_layout_config()
        if "grid" in layout_config:
            ax.grid(True, alpha=layout_config["grid"]["alpha"], 
                   linewidth=layout_config["grid"]["linewidth"],
                   color=color_config["grid"])
        
        # Set margins
        margins = layout_config["margins"]
        fig.subplots_adjust(
            left=margins["left"],
            right=1-margins["right"],
            top=1-margins["top"],
            bottom=margins["bottom"]
        )
    
    def set_color_palette(self, palette_name: Optional[str] = None) -> None:
        """Set color palette for matplotlib"""
        color_config = self.style_format.get_color_config()
        palette = palette_name or color_config["palette"]
        
        # Set default color cycle
        if palette == "viridis":
            colors = plt.cm.viridis([0.1, 0.3, 0.5, 0.7, 0.9])
            plt.rcParams['axes.prop_cycle'] = plt.cycler('color', colors)
        else:
            # Set custom colors
            colors = [color_config["primary"], color_config["secondary"]]
            plt.rcParams['axes.prop_cycle'] = plt.cycler('color', colors)
    
    def create_figure(self) -> tuple:
        """Create a new figure with universal style applied"""
        size = self.style_format.get_figure_size()
        dpi = self.style_format.get_dpi()
        
        fig, ax = plt.subplots(figsize=size, dpi=dpi)
        self.apply_style(fig, ax)
        self.set_color_palette()
        
        return fig, ax
    
    def save_figure(self, fig: plt.Figure, filename: str, format: str = 'png', 
                   quality: str = 'high', metadata: Optional[Dict[str, Any]] = None) -> None:
        """Save matplotlib figure with universal settings"""
        
        save_kwargs = {
            'format': format,
            'dpi': self.style_format.get_dpi() if quality == 'high' else 150,
            'bbox_inches': 'tight',
            'facecolor': self.style_format.schema["figure"]["background"],
            'edgecolor': 'none'
        }
        
        if metadata:
            save_kwargs['metadata'] = metadata
        
        fig.savefig(filename, **save_kwargs)