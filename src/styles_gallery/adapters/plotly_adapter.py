"""Plotly adapter for universal style format"""

from typing import Dict, Any, Optional, Union
import plotly.graph_objects as go
import plotly.io as pio
from ..formats.common_format import UniversalStyleFormat


class PlotlyAdapter:
    """Adapter to apply universal styles to plotly figures"""
    
    def __init__(self, style_format: Optional[UniversalStyleFormat] = None):
        self.style_format = style_format or UniversalStyleFormat()
    
    def get_layout_config(self) -> Dict[str, Any]:
        """Generate plotly layout configuration from universal style"""
        
        figure_config = self.style_format.schema["figure"]
        font_config = self.style_format.get_font_config()
        color_config = self.style_format.get_color_config()
        layout_config = self.style_format.get_layout_config()
        
        # Convert size from inches to pixels (assuming 96 dpi for web)
        width_px = int(figure_config["size"]["width"] * 96)
        height_px = int(figure_config["size"]["height"] * 96)
        
        layout = {
            'width': width_px,
            'height': height_px,
            'paper_bgcolor': figure_config["background"],
            'plot_bgcolor': figure_config["background"],
            'font': {
                'family': font_config["family"],
                'size': font_config["size"]["default"],
                'color': 'black'
            },
            'title': {
                'font': {'size': font_config["size"]["title"]}
            },
            'xaxis': {
                'title': {'font': {'size': font_config["size"]["label"]}},
                'showgrid': True,
                'gridcolor': color_config["grid"],
                'gridwidth': layout_config["grid"]["linewidth"],
                'zeroline': False
            },
            'yaxis': {
                'title': {'font': {'size': font_config["size"]["label"]}},
                'showgrid': True,
                'gridcolor': color_config["grid"],
                'gridwidth': layout_config["grid"]["linewidth"],
                'zeroline': False
            },
            'margin': {
                'l': int(layout_config["margins"]["left"] * width_px),
                'r': int(layout_config["margins"]["right"] * width_px),
                't': int(layout_config["margins"]["top"] * height_px),
                'b': int(layout_config["margins"]["bottom"] * height_px)
            }
        }
        
        return layout
    
    def get_color_palette(self) -> list:
        """Get color palette for plotly"""
        color_config = self.style_format.get_color_config()
        
        if color_config["palette"] == "viridis":
            return ['#440154', '#31688e', '#35b779', '#fde725']
        else:
            return [color_config["primary"], color_config["secondary"]]
    
    def apply_style(self, fig: go.Figure) -> go.Figure:
        """Apply universal style to plotly figure"""
        
        layout_config = self.get_layout_config()
        fig.update_layout(**layout_config)
        
        # Apply color palette to traces
        colors = self.get_color_palette()
        for i, trace in enumerate(fig.data):
            if hasattr(trace, 'marker'):
                trace.marker.color = colors[i % len(colors)]
            elif hasattr(trace, 'line'):
                trace.line.color = colors[i % len(colors)]
        
        return fig
    
    def create_figure(self, figure_type: str = 'scatter') -> go.Figure:
        """Create a new plotly figure with universal style applied"""
        
        if figure_type == 'scatter':
            fig = go.Figure()
        elif figure_type == 'bar':
            fig = go.Figure()
        else:
            fig = go.Figure()
        
        return self.apply_style(fig)
    
    def save_figure(self, fig: go.Figure, filename: str, format: str = 'png', 
                   quality: str = 'high', metadata: Optional[Dict[str, Any]] = None) -> None:
        """Save plotly figure with universal settings"""
        
        # Determine file extension
        if not filename.lower().endswith(f'.{format}'):
            filename = f"{filename}.{format}"
        
        # Set image parameters
        width = self.style_format.schema["figure"]["size"]["width"]
        height = self.style_format.schema["figure"]["size"]["height"]
        dpi = self.style_format.get_dpi()
        
        # Convert inches to pixels
        width_px = int(width * dpi)
        height_px = int(height * dpi)
        
        if format.lower() in ['png', 'jpg', 'jpeg', 'svg', 'pdf']:
            fig.write_image(
                filename,
                format=format,
                width=width_px,
                height=height_px,
                scale=1 if quality == 'high' else 0.5
            )
        elif format.lower() == 'html':
            fig.write_html(filename)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def create_subplot_figure(self, rows: int = 1, cols: int = 1) -> go.Figure:
        """Create plotly subplot figure with universal style"""
        from plotly.subplots import make_subplots
        
        fig = make_subplots(rows=rows, cols=cols)
        return self.apply_style(fig)