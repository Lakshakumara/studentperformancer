from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# Version read from file.
version_file = open(os.path.join(here, 'studentperformancer', 'VERSION'))
VERSION = version_file.read().strip()
DESCRIPTION = 'Students performance for Moodle LMS'

# Setting up
setup(
    name="studentperformancer",
    version=VERSION,
    author="YML kumara",
    author_email="<lakshakumara@gmail.com>",
    description=DESCRIPTION,
    
    # Choose your license
    license='GPLv3',

    packages=find_packages(),
    package_data={
        'performancer': ['VERSION']
    },
    install_requires=['numpy'],
    keywords=['python', 'moodle', 'analytics'],
    classifiers=[
        "Development Status :: 1 - Alpa",
        "Intended Audience :: OUSL",
        'Topic :: Learn OUSL',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)