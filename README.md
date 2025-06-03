# Styles Gallery

Universal plotting style management across matplotlib, plotly, and bokeh.

## Features

- **Universal Style Format**: JSON-based style schema that works across all plotting libraries
- **Library Adapters**: Native adapters for matplotlib, plotly, and bokeh
- **Image Save Engine**: Consistent image saving with format detection and metadata support
- **Style Templates**: Pre-built scientific publication styles

## Quick Start

```python
from styles_gallery import UniversalStyleFormat, save_image
import matplotlib.pyplot as plt

# Create figure with universal style
style = UniversalStyleFormat()
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 2])

# Save with universal engine (auto-detects matplotlib)
save_image(fig, "output", format="png", quality="high")
```

## Library-Specific Usage

### Matplotlib
```python
from styles_gallery.adapters import MatplotlibAdapter

adapter = MatplotlibAdapter()
fig, ax = adapter.create_figure()
ax.plot([1, 2, 3], [1, 4, 2])
adapter.save_figure(fig, "matplotlib_plot.png")
```

### Plotly
```python
from styles_gallery.adapters import PlotlyAdapter
import plotly.graph_objects as go

adapter = PlotlyAdapter()
fig = adapter.create_figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 2]))
adapter.save_figure(fig, "plotly_plot.png")
```

### Bokeh
```python
from styles_gallery.adapters import BokehAdapter

adapter = BokehAdapter()
fig = adapter.create_figure()
fig.line([1, 2, 3], [1, 4, 2])
adapter.save_figure(fig, "bokeh_plot.png")
```

## Universal Style Schema

```json
{
  "version": "1.0",
  "figure": {
    "size": {"width": 6.4, "height": 4.8},
    "dpi": 300,
    "background": "white"
  },
  "fonts": {
    "family": "serif",
    "size": {"default": 12, "title": 14, "label": 10}
  },
  "colors": {
    "palette": "viridis",
    "primary": "#1f77b4",
    "secondary": "#ff7f0e"
  }
}
```

## Installation

```bash
pip install styles-gallery

# With development dependencies
pip install styles-gallery[dev]

# With full bokeh PNG export support
pip install styles-gallery[full]
```

## Version: 20250602_000000_0_1_0_2