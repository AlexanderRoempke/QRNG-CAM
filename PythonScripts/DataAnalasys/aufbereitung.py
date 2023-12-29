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

        # Convert electrons to photons for each color
        photons_red = electrons_red / quantum_efficiency['red']
        photons_green_1 = electrons_green_1 / quantum_efficiency['green']
        photons_green_2 = electrons_green_2 / quantum_efficiency['green']
        photons_blue = electrons_blue / quantum_efficiency['blue']

        # Print photons for each pixel
        for i in range(photons_red.shape[0]):
            for j in range(photons_red.shape[1]):
                print(f"Red pixel at ({i*2},{j*2}): {int(photons_red[i, j])} photons")
                print(f"Green pixel at ({i*2},{j*2+1}): {int(photons_green_1[i, j])} photons")
                print(f"Green pixel at ({i*2+1},{j*2}): {int(photons_green_2[i, j])} photons")
                print(f"Blue pixel at ({i*2+1},{j*2+1}): {int(photons_blue[i, j])} photons")

# Example usage
dng_file = 'full.dng'  # Replace with your DNG file path

# Hypothetical sensor data (replace with actual data)
gain = 1.0
offset = 0
quantum_efficiency = {'red': 0.8, 'green': 0.95, 'blue': 0.9}

calculate_and_print_photons_per_pixel(dng_file, gain, offset, quantum_efficiency)

