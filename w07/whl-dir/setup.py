import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="example-pkg-maxlaimon",
    version="0.0.1",
    author="maxlaimon",
    author_email="nikitmk@yandex.ru",
    description="A small example package",
#    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxlaimon/rep/w7",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)