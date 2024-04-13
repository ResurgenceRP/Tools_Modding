import re
import os
from datetime import datetime

def find_class_names_in_cpp(cpp_filename):
    class_pattern = re.compile(r'class\s+([\w_]+)\s*:\s*')
    class_names = []
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

def read_existing_classes(output_path):
    existing_classes = set()
    try:
        with open(output_path, 'r') as file:
            content = file.read()
            existing_classes.update(re.findall(r'type name="([\w_]+)"', content))
    except FileNotFoundError:
        print(f"No existing file found at {output_path}. A new one will be created.")
    return existing_classes

def write_to_xml_format(new_classes, output_paths):
    current_date = datetime.now().strftime("%Y-%m-%d")
    for output_path in output_paths:
        existing_classes = read_existing_classes(output_path)
        to_write_classes = [cls for cls in new_classes if cls not in existing_classes]
        
        if to_write_classes:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'a') as file:
                file.write("\n")
                file.write(f"//////UPDATE {current_date}//////\n")
                for name in to_write_classes:
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
    cpp_filename = input("Please enter the path to the C++ file: ")
    cpp_filename = cpp_filename.replace('"', '')

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
