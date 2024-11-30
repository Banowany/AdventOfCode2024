def read_file_lines(file_path):
    """
    Reads the content of a file and returns a list of its lines.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        list: A list containing each line of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")


# Example usage (if run as a script)
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python file_reader.py <file_path>")
    else:
        try:
            file_path = sys.argv[1]
            lines = read_file_lines(file_path)
            print("\n".join(lines))
        except Exception as e:
            print(f"Error: {e}")