# dicom_converter_package

# dicom_converter

Convert DICOM files to JPEG format using Python.

## Installation

You can install `dicom_converter_package` from GitHub using `pip`:

```bash
pip install git+https://github.com/your-username/dicom_converter_package.git


from dicom_converter import converter

# Specify input and output paths
folder_path = "/path/to/input_files"
output_path = "/path/to/output_files"

# Convert DICOM to JPEG
converter.convert(folder_path, output_path)
