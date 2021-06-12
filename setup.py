from setuptools import setup, find_packages

VERSION = "1"
DESCRIPTION = "BMI Calculator"
LONG_DESCRIPTION = "BMI Calculator"

setup(
    name="bmi_calculator",
    author="Rushikesh Samantra",
    author_email="rushikeshsamantra328@gmail.com",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'first package'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ]
)