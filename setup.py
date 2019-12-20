
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='LexNer',
    version='0.1.0',
    description='LexNer: a lexical analysis and named entity recognition library for Python',
    long_description=readme,
    author='Ahmed Nabhan',
    author_email='ahmed.nabhan@gmail.com',
    url='https://github.com/arnabhan/lexner',
    license=license,
    install_requires=['tqdm'],
    packages=find_packages(exclude=('tests', 'docs'))
)

