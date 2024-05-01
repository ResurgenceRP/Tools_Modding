import re
import os
import random
from datetime import datetime

def find_class_names_in_cpp(cpp_filename):
    """ Extract class names from a C++ file that match the 'class <name> :' pattern. """
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
    """ Read existing classes from an XML file and return them as a set. """
    existing_classes = set()
    type_pattern = re.compile(r'type name="([\w_]+)"')
    try:
        with open(output_path, 'r') as file:
            content = file.read()
            existing_classes.update(type_pattern.findall(content))
    except FileNotFoundError:
        print(f"No existing file found at {output_path}. A new one will be created.")
    return existing_classes

def determine_category(class_name, category_cache):
    """ Determine the category of the class based on its name or from a cache. """
    categories = ["weapons", "clothes", "food", "tools", "containers", "industrialfood", "explosives", "vehicleparts"]
    category_rules = {
        "flag": "tools",
        "armband": "clothes"
    }
    for key, value in category_rules.items():
        if key in class_name:
            return value
    # Check if already determined
    if class_name in category_cache:
        return category_cache[class_name]
    else:
        print(f"Please select a category for {class_name}:")
        print(", ".join([f"{i+1} - {cat}" for i, cat in enumerate(categories)]))
        choice = int(input("Enter the number corresponding to the category: ")) - 1
        category_cache[class_name] = categories[choice]
        return categories[choice]

def write_to_xml_format(new_classes, output_paths, category_cache):
    """ Append new classes to an XML file if they do not already exist, with header inclusion handled per file. """
    current_date = datetime.now().strftime("%Y-%m-%d")
    type_template = '''
    <type name="{name}">
        <nominal>0</nominal>
        <lifetime>{lifetime}</lifetime>
        <restock>0</restock>
        <min>0</min>
        <quantmin>-1</quantmin>
        <quantmax>-1</quantmax>
        <cost>100</cost>
        <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="1" deloot="0" />
        <category name="{category}" />
    </type>
    '''
    for output_path in output_paths:
        existing_classes = read_existing_classes(output_path)
        to_write_classes = [cls for cls in new_classes if cls not in existing_classes]
        
        if to_write_classes:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'a') as file:
                file.write("\n")
                file.write(f"//////UPDATE {current_date}//////\n")
                for name in to_write_classes:
                    category = determine_category(name, category_cache)
                    lifetime = random.randint(4500, 14500)
                    file.write(type_template.format(name=name, lifetime=lifetime, category=category))

def main():
    cpp_filenames = input("Please enter the path to C++ files (separated by commas): ").replace('"', '').split(',')
    output_paths = [
        'P:\\OUTPUTS\\@ResurgenceRP_Dev\\types.txt',
        'P:\\OUTPUTS\\@ResurgenceRP\\types.txt'
    ]

    all_class_names = set()
    category_cache = {}
    for cpp_filename in cpp_filenames:
        class_names = find_class_names_in_cpp(cpp_filename.strip())
        all_class_names.update(class_names)

    if all_class_names:
        write_to_xml_format(list(all_class_names), output_paths, category_cache)
        for path in output_paths:
            print(f"Updated data has been appended to {path}")
    else:
        print("No class names extracted. Check if the files are correct and contain the required patterns.")

# Commented out the call to main to prevent execution in this context
if __name__ == "__main__":
    main()

