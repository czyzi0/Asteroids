import pathlib

from setuptools import setup, find_packages


with open(pathlib.Path(__file__).parent / 'README.md', 'r') as long_desc_file:
    LONG_DESCRIPTION = long_desc_file.read()

setup(
    name='Asteroids',
    version='0.0.0',
    description='Clone of 1979 Atari game',
    long_description=LONG_DESCRIPTION,
    author='czyzi0',
    author_email='czyznikiewicz.mateusz@gmail.com',
    url='https://github.com/czyzi0/Asteroids',
    license='MIT',
    keywords='asteroids game pygame',
    packages=find_packages(),
    package_data={'Asteroids': ['assets/**/*']},
    python_requires='>=3.6.0',
    install_requires=['pygame>=1.9.4']
)
