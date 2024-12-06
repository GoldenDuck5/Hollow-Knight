#
#
# file_management_functions.py
# Author -> GoldenDuck5 (github)
# Code Parsing and Refactoring -> TheVigilante51 (github)
#
#

import os


def search_file(file_name, directory):
    try:
        for root, dirs, files in os.walk(directory):
            if file_name in files:
                return os.path.join(root, file_name)
        return "File not found."
    except Exception as e:
        return f"Error searching for the file: {e}"

def delete_file(file_path):
    try:
        os.remove(file_path)
        return "File deleted successfully."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error deleting file: {e}"

def list_files(directory):
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return "Directory not found."
    except Exception as e:
        return f"Error listing files: {e}"
