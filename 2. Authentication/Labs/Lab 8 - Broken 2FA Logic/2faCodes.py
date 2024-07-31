codes = [f"{i:04}" for i in range(10000)]

# Specify the filename
filename = 'codes.txt'

# Write the codes to the file
with open(filename, 'w') as file:
    for code in codes:
        file.write(code + '\n')

print(f"All codes have been written to {filename}")