import os
import re


def rename_files_in_directory(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    for file_name in files:
        # Check if the file is a regular file
        if os.path.isfile(os.path.join(directory, file_name)):
            # Extract file extension
            base_name, extension = os.path.splitext(file_name)
            
            # Convert file name from camel case to snake case using regex
            new_base_name = re.sub('(?<=[a-z])(?=[A-Z])', '_', base_name).lower().replace(' ', '_')
            
            # Create new file name
            new_file_name = new_base_name + extension
            
            # Rename the file
            os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))
            print(f'Renamed: {file_name} -> {new_file_name}')

# Example usage:
rename_files_in_directory('dataset')
