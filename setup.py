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
    version="0.0.2",
    author="YML Kumara",
    author_email="<lakshakumara@gmail.com>",
    description=DESCRIPTION,
    
    # Choose your license
    license='GPLv3',

    packages=find_packages(),
    package_data={
        'studentperformancer': ['VERSION']
    },
    install_requires=[
        'matplotlib>=1.5.0',
        'numpy>=1.11.0',
        'scikit-learn>=0.17.0',
        'scipy>=0.17.0',
        'tensorflow>=1.0.0',
    ],
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
    ],
    )
    # token pypi-AgEIcHlwaS5vcmcCJGY5Yzg3MzI1LWI4ZjYtNGUwYy04MzIzLTQxZDdlZTUyZWUyZgACKlszLCIyZTA0NjYyMC0xNzJkLTQ5ODEtYjllYS1jMjJkYjY5OGJiNTciXQAABiAVGI2lE8m8J8UWFClv4VoRHXLmlCcT-g_y5mSAdVxmQg