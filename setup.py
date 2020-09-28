import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bunnyplot",
    version="0.1.0",
    author="Jerome Twell",
    author_email="jtwell1@gmail.com",
    description="A utility for producting GraphML from RabbitMQ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jerometwell/bunnyplot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click",
        "networkx",
        "aiohttp",
        "async_timeout"
    ],
    entry_points = {
        'console_scripts': ['bunnyplot=bunnyplot.cli:cli'],
    },
    python_requires='>=3.6',
)