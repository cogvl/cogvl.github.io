#!/usr/bin/env python3
"""
Script to remove black background from workshop-logo.png and convert to SVG.
Uses PIL for image processing.
"""

import subprocess
import sys

def install_package(package):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])

# Ensure required packages are installed
try:
    from PIL import Image
except ImportError:
    install_package("Pillow")
    from PIL import Image

try:
    import numpy as np
except ImportError:
    install_package("numpy")
    import numpy as np

def remove_black_background(input_path, output_path, threshold=253):
    """
    Remove black background from an image and save as PNG with transparency.
    
    Args:
        input_path: Path to input image
        output_path: Path to output PNG with transparency
        threshold: Pixels with R, G, B all below this value are considered black
    """
    # Open image and convert to RGBA
    img = Image.open(input_path).convert("RGBA")
    data = np.array(img)
    
    # Get RGB channels
    r, g, b, a = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]
    
    # Create mask for black pixels (all channels below threshold)
    black_mask = (r < threshold) & (g < threshold) & (b < threshold)
    
    # Set alpha to 0 for black pixels
    data[:, :, 3] = np.where(black_mask, 0, 255)
    
    # Save the result
    result = Image.fromarray(data)
    result.save(output_path, "PNG")
    print(f"Saved transparent PNG to: {output_path}")
    return output_path


def create_color_svg(png_path, svg_path):
    """
    Create an SVG that embeds the transparent PNG as a base64 image.
    This preserves all colors and details.
    """
    import base64
    
    # Read the PNG file
    with open(png_path, 'rb') as f:
        png_data = f.read()
    
    # Get image dimensions
    img = Image.open(png_path)
    width, height = img.size
    
    # Encode as base64
    b64_data = base64.b64encode(png_data).decode('utf-8')
    
    # Create SVG with embedded image
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{width}" height="{height}" 
     viewBox="0 0 {width} {height}">
  <image width="{width}" height="{height}" 
         xlink:href="data:image/png;base64,{b64_data}"/>
</svg>'''
    
    with open(svg_path, 'w') as f:
        f.write(svg_content)
    
    print(f"Saved color SVG (with embedded transparent PNG) to: {svg_path}")
    return svg_path


def main():
    import os
    
    # Paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "static/images/workshop-logo.png")
    transparent_png_path = os.path.join(script_dir, "static/images/workshop-logo-transparent.png")
    svg_path = os.path.join(script_dir, "static/images/workshop-logo.svg")
    
    print(f"Processing: {input_path}")
    
    # Step 1: Remove black background
    remove_black_background(input_path, transparent_png_path, threshold=200)
    
    # Step 2: Create color SVG with embedded transparent PNG
    create_color_svg(transparent_png_path, svg_path)
    
    print("\nDone! Created:")
    print(f"  - {transparent_png_path} (PNG with transparent background)")
    print(f"  - {svg_path} (SVG with embedded transparent PNG - preserves colors)")


if __name__ == "__main__":
    main()
