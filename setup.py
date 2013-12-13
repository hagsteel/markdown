import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="markdown",
    version="0.1.0",
    author="Jonas Hagstedt",
    author_email="hagstedt@gmail.com",
    description=("Markdown template tag"),
    license="BSD",
    keywords="django markdown template tag",
    url = "https://github.com/jonashagstedt/markdown",
    packages=['hs_markdown', ],
    long_description=read('README.md'),
    install_requires=[
        "Django >= 1.4",
        "markdown"
    ],
    classifiers=[
        "Development Status :: Beta",
        "Topic :: Markdown",
        "License :: OSI Approved :: BSD License",
    ],
)
