try:
    file = open("output.txt", "r")  # Open the file in read mode
    content = file.read()  # Read the content of the file
    file.close()  # Close the file after reading
    print("Content of output.txt:")
    print(content)  # Print the content
except FileNotFoundError:
    print("File 'output.txt' not found.")