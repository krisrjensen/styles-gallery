"""Setup script for styles-gallery package"""

from setuptools import setup, find_packages

setup(
    name="styles-gallery",
    version="20250602_000000_0_1_0_2",
    author="Worker 2",
    description="Universal plotting style management across matplotlib, plotly, and bokeh",
    long_description="Universal style format and image save engine for consistent plotting across all major Python plotting libraries",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[
        "matplotlib>=3.0.0",
        "plotly>=4.0.0", 
        "bokeh>=2.0.0",
    ],
    extras_require={
        "dev": ["pytest>=6.0", "pytest-cov", "black", "flake8"],
        "full": ["selenium", "chromedriver-binary"]  # For bokeh PNG export
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)