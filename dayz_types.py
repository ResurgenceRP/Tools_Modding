import re
import os
from datetime import datetime

def find_class_names_in_cpp(cpp_filename):
    # Regular expression to match the class pattern
    class_pattern = re.compile(r'class\s+([\w_]+)\s*:\s*')

    # List to store extracted class names
    class_names = []

    # Read the .cpp file
    try:
        with open(cpp_filename, 'r') as file:
            for line in file:
                match = class_pattern.search(line)
                if match:
                    class_names.append(match.group(1))
    except FileNotFoundError:
        print(f"Error: The file '{cpp_filename}' does not exist. Please check the path and try again.")
        return []

    return class_names

def write_to_xml_format(class_names, output_paths):
    # Get the current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")

    for output_path in output_paths:
        # Ensure directory exists before writing to it
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Open the file in append mode
        with open(output_path, 'a') as file:
            file.write("\n")  # Start with a newline
            file.write(f"//////UPDATE {current_date}//////\n")
            for name in class_names:
                file.write(f'<type name="{name}">\n')
                file.write('    <nominal>0</nominal>\n')
                file.write('    <lifetime>14400</lifetime>\n')
                file.write('    <restock>0</restock>\n')
                file.write('    <min>0</min>\n')
                file.write('    <quantmin>-1</quantmin>\n')
                file.write('    <quantmax>-1</quantmax>\n')
                file.write('    <cost>100</cost>\n')
                file.write('    <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="1" deloot="0" />\n')
                file.write('    <category name="clothes" />\n')
                file.write('  </type>\n')

def main():
    # Ask the user to provide the path to the C++ source file
    cpp_filename = input("Please enter the path to the C++ file: ")
    cpp_filename = cpp_filename.replace('"', '')
    
    # Output file paths
    output_paths = [
        'P:\\OUTPUTS\\@ResurgenceRP_Dev\\types.txt',
        'P:\\OUTPUTS\\@ResurgenceRP\\types.txt'
    ]

    class_names = find_class_names_in_cpp(cpp_filename)
    if class_names:
        write_to_xml_format(class_names, output_paths)
        for path in output_paths:
            print(f"Updated data has been appended to {path}")
    else:
        print("No class names extracted. Check if the file is correct and contains the required patterns.")

if __name__ == "__main__":
    main()
