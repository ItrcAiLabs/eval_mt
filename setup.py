import codecs
import os



from setuptools import setup, find_packages

setup(
    name="evaluation-machine-translation", 
    version="0.1.0",
    author="Alireza Parvaresh",
    author_email="parvvaresh@gmail.com",
    description="common methods used to evaluate machine translation,",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ItrcAiLabs/eval_mt",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
