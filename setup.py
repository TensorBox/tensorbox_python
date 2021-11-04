import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tensorboxsdk",
    version="1.0.2",
    author="TensorBox",
    author_email="gettensorbox@gmail.com",
    description="Pytnon bindings for the TensorBox API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tensorbox/python_sdk",
    project_urls={
        "Bug Tracker": "https://github.com/tensorbox/python_sdk/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
