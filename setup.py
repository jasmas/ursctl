import setuptools
import ursctl

with open('README.rst', 'r') as fh:
        long_description = fh.read()

setuptools.setup(
    name=ursctl.__name__,
    version=ursctl.__version__,
    url=ursctl.__url__,
    packages=setuptools.find_packages(),
    author=ursctl.__author__,
    author_email=ursctl.__email__,
    description=ursctl.__description__,
    long_description=long_description,
    license=ursctl.__license__,
    keywords='',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['ursctl = ursctl.__main__:run',],},
)

