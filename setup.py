import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metabasepy-pkg-meedan", # Replace with your own username
    version="0.0.1",
    author="Scott Hale",
    author_email="scott@meedan.com",
    description="A simple wrapper for metabase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meedan/metabasepy",
    project_urls={
        "Bug Tracker": "https://github.com/meedan/metabasepy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "metabasepy"},
    packages=setuptools.find_packages(where="metabasepy"),
    python_requires=">=3.6",
)
