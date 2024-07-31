def write_repeated_text(filename, text, repetitions):
    try:
        with open(filename, 'w') as file:
            for _ in range(repetitions):
                file.write(text + '\n')
        print(f"{repetitions} repetitions of the text written to {filename}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
output_filename = 'lab6-username-wordlist.txt'  # Replace with your desired output file name
text_to_write = "wiener\ncarlos\ncarlos"
repetitions = 50

write_repeated_text(output_filename, text_to_write, repetitions)
