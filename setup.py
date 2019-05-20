import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-digifinex",   # My package name
    version="0.0.1",
    author="Abhisek Roy",
    author_email="abhisekroy.cse@gmail.com",
    description="Digifinex APIs in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhisek1985/python-digifinex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)