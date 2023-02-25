from setuptools import setup

setup(
    name="NumeraiUtils",
    version="1.0",
    packages=['NumeraiUtils'],
     install_requires=[
         'pandas',
         'numpy',
         'scipy',
         'halo',
         'tqdm',
     ],
)
