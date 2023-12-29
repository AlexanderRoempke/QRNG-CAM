def format_text(file_path, line_length):
    # Read the original text from the file
    with open(file_path, 'r') as file:
        original_text = file.read()

    # Remove all newlines and spaces from the original text
    cleaned_text = original_text.replace('\n', '').replace(' ', '')

    # Initialize a list to store formatted lines
    lines = []

    # Process each line
    for i in range(0, len(cleaned_text), line_length):
        # Extract a segment of the text
        line = cleaned_text[i:i+line_length]

        # Add three leading spaces to the line
        line = '   ' + line

        # Add the processed line to the list
        lines.append(line)

        # Stop processing if the maximum line count is reached
        if len(lines) == 40196:
            break

    # Ensure the first line is 24 characters long (excluding spaces)
    lines[0] = lines[0][:27]  # 24 characters + 3 spaces

    # Ensure the last line is 8 characters long (excluding spaces)
    lines[-1] = lines[-1][:11]  # 8 characters + 3 spaces

    return '\n'.join(lines)

# File path of your original text file
file_path = 'comparison_ascii.txt'  # Replace with your file path

# Desired format: specify the line length
line_length = 25  # Replace with your desired line length

# Format the text
formatted_text = format_text(file_path, line_length)

# Write the formatted text to a new file
with open('ready.txt', 'w') as file:
    file.write(formatted_text)

print("Text has been formatted and written to formatted_text_corrected.txt")

