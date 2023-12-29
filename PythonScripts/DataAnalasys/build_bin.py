import rawpy
import numpy as np

def calculate_photons(dng_file, gain, offset, quantum_efficiency):
    with rawpy.imread(dng_file) as raw:
        raw_data = raw.raw_image_visible

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

        return photons_red, photons_green_1, photons_green_2, photons_blue

def compare_images(image1, image2, gain, offset, quantum_efficiency):
    photons_image1 = calculate_photons(image1, gain, offset, quantum_efficiency)
    photons_image2 = calculate_photons(image2, gain, offset, quantum_efficiency)

    comparison = []
    for color_channel in range(4):
        comparison.append(np.greater(photons_image1[color_channel], photons_image2[color_channel]).astype(int))

    return comparison

# Example usage
image1 = 'full.dng'
image2 = 'full2.dng'

# Hypothetical sensor data (replace with actual data)
gain = 1
offset = 0
quantum_efficiency = {'red': 0.8, 'green': 0.95, 'blue': .9}

comparison = compare_images(image1, image2, gain, offset, quantum_efficiency)

# Write results to a binary file
with open('comparison.bin', 'wb') as bin_file, open('metadata.txt', 'w') as meta_file:
    total_bytes = 0
    total_ones = 0
    total_zeros = 0
    for channel in comparison:
        for row in channel:
            for value in row:
                bin_file.write(int(value).to_bytes(1, byteorder='big'))
                total_bytes += 1
                if value == 1:
                    total_ones += 1
                else:
                    total_zeros += 1

    # Write metadata
    meta_file.write(f"Total Bytes: {total_bytes}\n")
    meta_file.write(f"Total 1s: {total_ones}\n")
    meta_file.write(f"Total 0s: {total_zeros}\n")

print("Comparison and metadata files have been created.")

