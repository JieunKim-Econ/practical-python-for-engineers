from pathlib import Path # Standard library for object-oriented file system paths

# Get the absolute path of the current file, then navigate two levels up to the project root
base_path = Path(__file__).resolve().parent.parent 

# Construct the target path using the '/' operator (path joining)
data_path = base_path /'data'/'raw'   

# Print the final resolved directory path for data storage
print(data_path)
# Return: C:\Users\jieun\python-de\data\raw

current_file = Path(__file__).resolve()
print(f"1. location of the current file: {current_file}")

src_folder = current_file.parent
print(f"2. location of the src folder: {src_folder}")

root_folder = src_folder.parent
print(f"3. location of the project root: {root_folder}")