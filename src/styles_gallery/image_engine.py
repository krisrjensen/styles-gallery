"""Universal image save engine for all plotting libraries"""

from typing import Dict, Any, Optional, Union
import os
from pathlib import Path
from datetime import datetime

from .formats.common_format import UniversalStyleFormat
from .adapters.matplotlib_adapter import MatplotlibAdapter
from .adapters.plotly_adapter import PlotlyAdapter
from .adapters.bokeh_adapter import BokehAdapter


class UniversalImageEngine:
    """Universal image saving engine across all plotting libraries"""
    
    def __init__(self, style_format: Optional[UniversalStyleFormat] = None):
        self.style_format = style_format or UniversalStyleFormat()
        self.matplotlib_adapter = MatplotlibAdapter(self.style_format)
        self.plotly_adapter = PlotlyAdapter(self.style_format)
        self.bokeh_adapter = BokehAdapter(self.style_format)
    
    def detect_figure_type(self, figure) -> str:
        """Detect the type of plotting library used for the figure"""
        
        figure_type = type(figure).__module__
        
        if 'matplotlib' in figure_type:
            return 'matplotlib'
        elif 'plotly' in figure_type:
            return 'plotly'
        elif 'bokeh' in figure_type:
            return 'bokeh'
        else:
            raise ValueError(f"Unsupported figure type: {type(figure)}")
    
    def save_image(self, figure, filename: str, format: str = 'png', 
                  quality: str = 'high', metadata: Optional[Dict[str, Any]] = None,
                  auto_timestamp: bool = False) -> str:
        """Universal image saving across all plotting libraries
        
        Args:
            figure: Figure object from any supported plotting library
            filename: Output filename (with or without extension)
            format: Image format ('png', 'svg', 'pdf', 'html', etc.)
            quality: Image quality ('high', 'medium', 'low')
            metadata: Optional metadata to embed in image
            auto_timestamp: Whether to add timestamp to filename
            
        Returns:
            str: Final filename of saved image
        """
        
        # Detect figure type
        figure_type = self.detect_figure_type(figure)
        
        # Process filename
        final_filename = self._process_filename(filename, format, auto_timestamp)
        
        # Ensure output directory exists
        output_dir = os.path.dirname(final_filename)
        if output_dir:
            Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Add default metadata
        if metadata is None:
            metadata = {}
        
        metadata.update({
            'created_by': 'Universal Image Engine',
            'style_version': self.style_format.schema['version'],
            'figure_type': figure_type,
            'timestamp': datetime.now().isoformat()
        })
        
        # Save using appropriate adapter
        if figure_type == 'matplotlib':
            self.matplotlib_adapter.save_figure(figure, final_filename, format, quality, metadata)
        elif figure_type == 'plotly':
            self.plotly_adapter.save_figure(figure, final_filename, format, quality, metadata)
        elif figure_type == 'bokeh':
            self.bokeh_adapter.save_figure(figure, final_filename, format, quality, metadata)
        else:
            raise ValueError(f"Unsupported figure type: {figure_type}")
        
        return final_filename
    
    def _process_filename(self, filename: str, format: str, auto_timestamp: bool) -> str:
        """Process filename with format and timestamp"""
        
        # Remove existing extension if present
        base_name = os.path.splitext(filename)[0]
        
        # Add timestamp if requested
        if auto_timestamp:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = f"{base_name}_{timestamp}"
        
        # Add format extension
        final_filename = f"{base_name}.{format}"
        
        return final_filename
    
    def save_multiple(self, figures: list, base_filename: str, format: str = 'png',
                     quality: str = 'high', metadata: Optional[Dict[str, Any]] = None) -> list:
        """Save multiple figures with numbered filenames
        
        Args:
            figures: List of figure objects
            base_filename: Base filename (numbers will be appended)
            format: Image format
            quality: Image quality
            metadata: Optional metadata
            
        Returns:
            list: List of saved filenames
        """
        
        saved_files = []
        
        for i, figure in enumerate(figures, 1):
            # Create numbered filename
            base_name = os.path.splitext(base_filename)[0]
            numbered_filename = f"{base_name}_{i:03d}"
            
            saved_file = self.save_image(
                figure, numbered_filename, format, quality, metadata
            )
            saved_files.append(saved_file)
        
        return saved_files
    
    def get_supported_formats(self, figure_type: str = None) -> Dict[str, list]:
        """Get supported formats for each figure type"""
        
        formats = {
            'matplotlib': ['png', 'pdf', 'svg', 'eps', 'ps', 'jpg', 'jpeg'],
            'plotly': ['png', 'jpg', 'jpeg', 'svg', 'pdf', 'html'],
            'bokeh': ['png', 'svg', 'html']
        }
        
        if figure_type:
            return formats.get(figure_type, [])
        
        return formats
    
    def batch_save(self, figures_dict: Dict[str, Any], output_dir: str = 'output',
                  format: str = 'png', quality: str = 'high') -> Dict[str, str]:
        """Batch save multiple figures with custom names
        
        Args:
            figures_dict: Dictionary mapping names to figure objects
            output_dir: Output directory
            format: Image format
            quality: Image quality
            
        Returns:
            dict: Mapping of names to saved filenames
        """
        
        saved_files = {}
        
        for name, figure in figures_dict.items():
            filename = os.path.join(output_dir, name)
            saved_file = self.save_image(figure, filename, format, quality)
            saved_files[name] = saved_file
        
        return saved_files


def save_image(figure, filename: str, format: str = 'png', 
               quality: str = 'high', metadata: Optional[Dict[str, Any]] = None) -> str:
    """Convenience function for universal image saving
    
    Args:
        figure: Figure object from any supported plotting library
        filename: Output filename
        format: Image format ('png', 'svg', 'pdf', 'html', etc.)
        quality: Image quality ('high', 'medium', 'low')
        metadata: Optional metadata to embed in image
        
    Returns:
        str: Final filename of saved image
    """
    
    engine = UniversalImageEngine()
    return engine.save_image(figure, filename, format, quality, metadata)