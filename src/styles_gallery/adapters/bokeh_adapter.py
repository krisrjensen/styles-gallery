"""Bokeh adapter for universal style format"""

from typing import Dict, Any, Optional, Union
from bokeh.plotting import figure, Figure
from bokeh.models import Range1d
from bokeh.io import export_png, export_svgs
import bokeh.palettes as palettes
from ..formats.common_format import UniversalStyleFormat


class BokehAdapter:
    """Adapter to apply universal styles to bokeh figures"""
    
    def __init__(self, style_format: Optional[UniversalStyleFormat] = None):
        self.style_format = style_format or UniversalStyleFormat()
    
    def get_figure_config(self) -> Dict[str, Any]:
        """Generate bokeh figure configuration from universal style"""
        
        figure_config = self.style_format.schema["figure"]
        font_config = self.style_format.get_font_config()
        color_config = self.style_format.get_color_config()
        layout_config = self.style_format.get_layout_config()
        
        # Convert size from inches to pixels (assuming 96 dpi for web)
        width_px = int(figure_config["size"]["width"] * 96)
        height_px = int(figure_config["size"]["height"] * 96)
        
        config = {
            'width': width_px,
            'height': height_px,
            'background_fill_color': figure_config["background"],
            'border_fill_color': figure_config["background"],
            'title': None,  # Will be set separately
            'toolbar_location': None,
            'outline_line_color': None
        }
        
        return config
    
    def get_color_palette(self) -> list:
        """Get color palette for bokeh"""
        color_config = self.style_format.get_color_config()
        
        if color_config["palette"] == "viridis":
            return palettes.Viridis[8]
        else:
            return [color_config["primary"], color_config["secondary"]]
    
    def apply_style(self, fig: Figure) -> Figure:
        """Apply universal style to bokeh figure"""
        
        font_config = self.style_format.get_font_config()
        color_config = self.style_format.get_color_config()
        layout_config = self.style_format.get_layout_config()
        
        # Set title style if exists
        if fig.title:
            fig.title.text_font_size = f"{font_config['size']['title']}pt"
            fig.title.text_font = font_config["family"]
        
        # Set axis styles
        for axis in [fig.xaxis, fig.yaxis]:
            axis.axis_label_text_font_size = f"{font_config['size']['label']}pt"
            axis.axis_label_text_font = font_config["family"]
            axis.major_label_text_font_size = f"{font_config['size']['default']}pt"
            axis.major_label_text_font = font_config["family"]
        
        # Set grid styles
        fig.grid.grid_line_color = color_config["grid"]
        fig.grid.grid_line_alpha = layout_config["grid"]["alpha"]
        fig.grid.grid_line_width = layout_config["grid"]["linewidth"]
        
        return fig
    
    def create_figure(self, plot_type: str = 'line', **kwargs) -> Figure:
        """Create a new bokeh figure with universal style applied"""
        
        config = self.get_figure_config()
        config.update(kwargs)
        
        fig = figure(**config)
        return self.apply_style(fig)
    
    def save_figure(self, fig: Figure, filename: str, format: str = 'png', 
                   quality: str = 'high', metadata: Optional[Dict[str, Any]] = None) -> None:
        """Save bokeh figure with universal settings"""
        
        # Determine file extension
        if not filename.lower().endswith(f'.{format}'):
            filename = f"{filename}.{format}"
        
        if format.lower() == 'png':
            # Set high DPI for quality
            dpi = self.style_format.get_dpi() if quality == 'high' else 150
            
            # Note: bokeh export_png requires selenium and chromedriver
            try:
                export_png(fig, filename=filename)
            except Exception as e:
                print(f"PNG export failed: {e}")
                print("Note: PNG export requires selenium and chromedriver")
                # Fallback to HTML
                fig.output_to_static_html(filename.replace('.png', '.html'))
        
        elif format.lower() == 'svg':
            try:
                export_svgs(fig, filename=filename)
            except Exception as e:
                print(f"SVG export failed: {e}")
                # Fallback to HTML
                fig.output_to_static_html(filename.replace('.svg', '.html'))
        
        elif format.lower() == 'html':
            from bokeh.plotting import output_file, save
            output_file(filename)
            save(fig)
        
        else:
            raise ValueError(f"Unsupported format for bokeh: {format}")
    
    def set_color_palette(self, fig: Figure, num_colors: int = 8) -> list:
        """Set color palette for bokeh figure"""
        colors = self.get_color_palette()
        
        # Extend palette if needed
        if len(colors) < num_colors:
            if self.style_format.get_color_config()["palette"] == "viridis":
                colors = palettes.Viridis[max(num_colors, 3)]
            else:
                # Cycle through available colors
                colors = colors * (num_colors // len(colors) + 1)
        
        return colors[:num_colors]
    
    def create_multi_figure(self, nrows: int = 1, ncols: int = 1) -> list:
        """Create multiple bokeh figures arranged in grid"""
        figures = []
        
        for i in range(nrows * ncols):
            fig = self.create_figure()
            figures.append(fig)
        
        return figures