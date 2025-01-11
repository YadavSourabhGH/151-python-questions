#write in a file

text = input("Enter a string to write to the file: ")  # Prompt user for input
file = open("output.txt", "w")  # Open the file in write mode
file.write(text)  # Write the input text to the file
file.close()  # Close the file after writing
print("Text has been written to output.txt")