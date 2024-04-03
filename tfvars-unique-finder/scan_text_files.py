import os

def scan_files(directory):
    """
    Scan text files in the specified directory.
    """
    text_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                text_files.append(os.path.join(root, file))
    return text_files

def find_unique_values(files):
    """
    Find unique values after "similar variable A:" across multiple files.
    """
    unique_values = set()
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                if line.startswith("similar variable A:"):
                    value = line.split(":")[1].strip()
                    unique_values.add(value)
    return unique_values

def main():
    directory = input("Enter directory containing text files: ")
    files = scan_files(directory)
    if files:
        unique_values = find_unique_values(files)
        if unique_values:
            print("Unique values found after 'similar variable A:' in the specified files:")
            for value in unique_values:
                print(value)
        else:
            print("No unique values found after 'similar variable A:' in the specified files.")
    else:
        print("No text files found in the specified directory.")

if __name__ == "__main__":
    main()
