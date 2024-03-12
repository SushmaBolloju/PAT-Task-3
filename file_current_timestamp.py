import datetime

def create_text_file_with_timestamp():
    # Get the current timestamp
    current_time = datetime.datetime.now()

    # Format the timestamp
    timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")

    # Create a filename with the timestamp
    filename = f"file_{timestamp}.txt"

    # Write some content to the file
    content = f"This file was created at {current_time}."

    # Write the content to the file
    with open(filename, 'w') as file:
        file.write(content)
        file.close()

    print(f"Text file '{filename}' created with the current timestamp.")

# Call the function to create the text file
create_text_file_with_timestamp()
