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
