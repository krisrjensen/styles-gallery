"""Plotting library adapters for universal style format"""

# Optional imports for plotting library adapters
__all__ = []

try:
    from .matplotlib_adapter import MatplotlibAdapter
    __all__.append("MatplotlibAdapter")
except ImportError:
    MatplotlibAdapter = None

try:
    from .plotly_adapter import PlotlyAdapter
    __all__.append("PlotlyAdapter")
except ImportError:
    PlotlyAdapter = None

try:
    from .bokeh_adapter import BokehAdapter
    __all__.append("BokehAdapter")
except ImportError:
    BokehAdapter = None