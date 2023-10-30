from setuptools import setup, find_packages
setup(
    name='dicom_converter_package',
    version='0.1',
    descriptions = """The dicom_converter_package is a Python package designed to facilitate the conversion of DICOM files to JPEG format. This package leverages the capabilities of the pydicom and Pillow libraries, making it easy to handle DICOM medical imaging files and convert them to the widely supported JPEG format.""",
    long_description_content_type='text/markdown',
    long_description=README,
    url="https://github.com/KUMARANVASANTH/dicom_converter_package",
    author="Vasantharan K",
    classifiers=["License :: Apache License 2.0",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.8"],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'pydicom',
        'Pillow',
    ],
)
