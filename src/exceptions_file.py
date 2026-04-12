try:
    with open("missing_file.csv", "r") as f: # Attempt to open a file with lower cases
        data = f.read()
except FileNotFoundError:
    with open("MISSING_FILE.csv", "r") as f: # Attempt to open the file again with upper cases
        data = f.read()
    print("File NOT Found: Pipeline cannnot proceed")  
finally:
    print("cleanup complete") # This block will execute whether an exception was raised or not, ensuring that any necessary cleanup is performed.