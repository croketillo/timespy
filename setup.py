from setuptools import setup, find_packages

setup(
    name="timespy",
    version="1.0.0",
    description="Timespy is a lightweight Python decorator that measures the execution time of functions, providing an easy way to analyze and optimize performance.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Croketillo",
    author_email="croketillo@gmail.com",
    url="https://github.com/croketillo/timespy", 
    license="GPL-3.0-or-later",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
