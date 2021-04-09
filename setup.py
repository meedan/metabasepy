import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
	reqs = f.read()
    
setuptools.setup(
    name="metabasepy",
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
	install_requires=reqs.strip().split('\n'),
	packages=setuptools.find_packages(),
    python_requires=">=3.6"
)
