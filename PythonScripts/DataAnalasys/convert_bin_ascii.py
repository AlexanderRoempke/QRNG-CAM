def bin_to_ascii(bin_file_path, ascii_file_path):
    try:
        with open(bin_file_path, 'rb') as bin_file, open(ascii_file_path, 'w') as ascii_file:
            while True:
                byte = bin_file.read(1)
                if not byte:
                    break

                # Process each bit in the byte
                byte_value = ord(byte)
                for i in range(7, -1, -1):
                    bit = (byte_value >> i) & 1
                    ascii_file.write(str(bit))
    except IOError as e:
        print(f"Error accessing file: {e}")

# Call the function with your file paths
bin_to_ascii('comparison.bin', 'comparison_ascii.txt')
