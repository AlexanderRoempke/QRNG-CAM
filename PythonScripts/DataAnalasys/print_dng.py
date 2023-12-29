import rawpy
import numpy as np

def calculate_and_print_photons_per_pixel(dng_file, gain, offset, quantum_efficiency):
    # Load DNG file
    with rawpy.imread(dng_file) as raw:
        # Access the raw data
        raw_data = raw.raw_image_visible
        print(raw_data)
        # Extract R, G, and B components from the Bayer pattern
        red_pixels = raw_data[::2, ::2]
        green_pixels_1 = raw_data[::2, 1::2]
        green_pixels_2 = raw_data[1::2, ::2]
        blue_pixels = raw_data[1::2, 1::2]

        # Convert DN to number of electrons for each color
        electrons_red = (red_pixels - offset) / gain
        electrons_green_1 = (green_pixels_1 - offset) / gain
        electrons_green_2 = (green_pixels_2 - offset) / gain
        electrons_blue = (blue_pixels - offset) / gain
        print(electrons_red)
        print(electrons_green_1)
        print(electrons_green_2)
        print(electrons_blue)

# Example usage
dng_file = 'full.dng'  # Replace with your DNG file path

# Hypothetical sensor data (replace with actual data)
gain = 1.0
offset = 0
quantum_efficiency = {'red': 0.8, 'green': 0.95, 'blue': 0.9}

calculate_and_print_photons_per_pixel(dng_file, gain, offset, quantum_efficiency)

