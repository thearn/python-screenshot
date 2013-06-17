
from setuptools import setup, find_packages

setup(name='python-screenshot',
    version='0.1',
    install_requires=['PIL'],
    description="Python library to make screen captures and save the images to the cwd",
    author='Tristan Hearn',
    author_email='tristanhearn@gmail.com',
    url='https://github.com/thearn/python-screenshot',
    license='Apache 2.0',
    packages=['screenshot'],
)
