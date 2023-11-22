# Pygame Procedural Generated Map

Welcome to the Pygame Procedural Generated Map repository! This module is designed to provide a simple tool for generating procedurally generated maps using perlin noise.

## Features:

- **Procedural Generation:** Create maps using perlin noise.
- **Map Visualizer:** The module come with a map visualizer which can also exports maps as pngs.
- **Pygame UI Module:** An extra UI module was introduce for the map visualizer.
- **Customization:** Fine-tune the generation process with customizable parameters to suit your specific needs.
- **Seamless Integration:** Easily integrate the module into your Pygame projects.

## Getting Started:

1. **Installation:**
- Don't forget to activate your virtual enviroment.
   ```bash
   pip install -e .
   ```

2. **Usage:**
    You can import the module in any project.
   ```python
    from pygame_procedural_generated_map.map_generator import NoiseMap

    noise_map = NoiseMap()

    noise_map.generate_map()

    noise_map.draw_map(view_scale = 4)
    # view_scale = how many pixels a cell will occupy

   ```
   Or for faster testing run the main.py app which has integrated UI for testing.

3. **Customization:**
   Adjust the generation parameters such as octaves, res, persistence, lacunarity to achieve the desired result.


## Contributing:

Contributions are welcome! If you encounter any issues, have ideas for improvements, or want to contribute new features, please open an issue or submit a pull request.

## License:

This project is licensed under the MIT License - see the LICENSE file for details.