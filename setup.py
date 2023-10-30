from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='dicom_converter_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pydicom',
        'Pillow',
    ],
    long_description=long_description,
    long_description_content_type='text/x-rst',
)
