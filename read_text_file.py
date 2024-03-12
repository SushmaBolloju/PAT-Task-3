def read_text_file(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Display the content in the console
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Test the function with a file name
file_name = "/Users/sushu/Downloads/file_2024-03-13_00-31-35.txt"  
# Pass the name of the text file to read the content.
# Have to pass full path if file is present in different directory(folder).
read_text_file(file_name)