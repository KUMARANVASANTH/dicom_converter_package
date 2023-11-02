from setuptools import setup, find_packages
setup(
    name='dicom_converter_package',
    version='0.1',
    author="Vasantharan K",
    author_email="vasantharank.learn@gmail.com",
    description="A package which converts all the images in a folder to JPEG file",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independant",
    ],
    install_requires=[
        'pydicom',
        'Pillow',
    ],
)
