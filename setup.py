import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'pydicom',
    'pyaml',
    'lxml',
    'pillow',
    'nibabel',
    'yaxil',
    'retry',
    'natsort'
]

about = dict()
with open(os.path.join(here, 'morphometry', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    include_package_data=True,
    package_data={
        '': [
            'xnat/morph3/mapping.yml'
        ]   
    },
    packages=find_packages(),
    scripts=[
        'scripts/surpher.py'
    ],
    install_requires=requires
)
