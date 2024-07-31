def add_peter_at_intervals(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
        
        # Initialize the output list with "peter" as the first entry
        modified_lines = ["peter\n"]
        
        # Add the lines from the original file, inserting "peter" at every third position
        for i, line in enumerate(lines):
            modified_lines.append(line)
            if (i + 1) % 2 == 0:
                modified_lines.append("peter\n")
        
        with open(output_filename, 'w') as file:
            file.writelines(modified_lines)
        
        print(f"Modified file saved as {output_filename}")
        
    except FileNotFoundError:
        print(f"The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
input_filename = 'password-wordlist.txt'  # Replace with your actual input file name
output_filename = 'lab6-password-wordlist.txt'
add_peter_at_intervals(input_filename, output_filename)