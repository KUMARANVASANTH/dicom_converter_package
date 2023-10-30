from setuptools import setup, find_packages
setup(
    name='dicom_converter_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pydicom',
        'Pillow',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
