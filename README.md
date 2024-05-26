# Tools_Modding
Additional modding tools developed in-house to assist with development of mod.

<details>
<summary>DayZ types.xml Generator</summary>
  
## Types.xml generator

This Python tool automatically extracts class names from a C++ file that match the Dayz item pattern (`class {className} : {base_class}`) and appends them in a structured XML format to specified output files.

### Requirements

Before running the script, ensure you have the following requirements installed:

- **Python**: The script is compatible with Python 3.x. You can download and install Python from [python.org](https://www.python.org/downloads/).

-**Regex** and **Enum** packages: these packages generally come preinstalled with Python3 but if needed they can be installed with:

```pip
pip install regex
pip install enum
```

- **Access Permissions**: Ensure you have write permissions to the directories where the output files will be saved.

### Installation

1. **Clone the Repository**:
   Clone this repository to your local machine using Git:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```
   Navigate to the cloned directory:
   ```bash
   cd yourrepository
   ```

### Configuration

To configure the script to work with your project, you will need to modify the output paths where the XML-formatted class names will be saved.

#### Modifying Output Paths

The script has predefined output paths set to:
- `P:\\OUTPUTS\\@ResurgenceRP_Dev\\types.txt`
- `P:\\OUTPUTS\\@ResurgenceRP\\types.txt`

To change these paths, open the `main()` function in the script and locate the following lines:
```python
output_paths = [
    'P:\\OUTPUTS\\@ResurgenceRP_Dev\\types.txt',
    'P:\\OUTPUTS\\@ResurgenceRP\\types.txt'
]
```

Replace these paths with your desired file locations. Ensure the new directories exist or that the script has permission to create them.

## Running the Tool

To run the tool, navigate to the directory containing the script and run:
```bash
python dayz_types.py
```

When prompted, enter the full path to the C++ file you wish to process. Quotation marks if present will be stripped

## Contributing

Contributions to this project are welcome. You can contribute by:
- Submitting a pull request with improvements.
- Reporting bugs or requesting new features by creating an issue.
</details>

<details>
<summary>DayZ Image Resizer and Converter</summary>

## DayZ Image Resizer and Converter

This Python tool automatically and looselessly resisizes images to 2048x1024 (Powers of two) which in turn is automatically converted to PAA file format using BI Studio tools. Processed PAA files will be saved in PROCESSED subfolder in source folder.

This tool was made mostly because i was anooyed at having to manually resize images while making loading screens

### Requirements

Before running the script, ensure you have the following requirements installed:

- **Python**: The script is compatible with Python 3.x. You can download and install Python from [python.org](https://www.python.org/downloads/).

-**Pillow** package: This package is required to resize images, you can install it with:

```pip
pip install pillow
```

- **DayZ Tools** - This script is designed with default DayZ tools in mind as it uses ImageToPaa executable from them

- **Access Permissions**: Ensure you have write permissions to the directories where the output files will be saved.

### Installation

1. **Clone the Repository**:
   Clone this repository to your local machine using Git:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```
   Navigate to the cloned directory:
   ```bash
   cd yourrepository
   ```

### Configuration

To configure the script to work with your project, you will need to modify following paths and settings:

```py
image_folder_path = r"PATH TO FOLDER WITH IMAGES"

image_to_paa_path = r"PATH TO IMAGETOPAA.EXE FILE"
```

In addition you can also adjust following settings:
```py
processed_folder_path = os.path.join(image_folder_path, "PROCESSED")

target_width, target_height = 2048, 1024
```

Where processed_folder_path is output location for PAA files (By default ``image_folder_path\PROCESSED``) and target_width, target_height are dimensions for output image

> [!CAUTION]
> target_width, target_height **MUST** be powers of 2 (i.e 512, 1024, 2048 and so on)

## Running the Tool

To run the tool, navigate to the directory containing the script and run:
```bash
python ImageResizeToPAA.py
```

## Contributing

Contributions to this project are welcome. You can contribute by:
- Submitting a pull request with improvements.
- Reporting bugs or requesting new features by creating an issue.
</details>