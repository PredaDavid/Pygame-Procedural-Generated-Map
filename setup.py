from setuptools import setup, find_packages

setup(
    name='pygame_procedural_generated_map',
    version='0.1',
    packages=['pygame_procedural_generated_map'],
    # packages=find_packages(),
    install_requires=[
        'pygame',
        'numpy',
    ],
)