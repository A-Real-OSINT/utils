import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utils",
    version="0.3",
    description="Utilities such as helperclasses and loggers for a real OSINT project",
    long_description=long_description,
    install_requires=[
        "pika",
        "real_dataclasses @ git+https://github.com/a-real-osint/real_dataclasses.git@main",
    ],
    long_description_content_type="text/markdown",
    url="https://github.com/a-real-osint/utils",
    packages=["utils"])
