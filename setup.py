from setuptools import setup, find_packages

setup(
    name='hypervenn',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
        'scipy',
    ],
    author='Darshan',
    description='Create beautiful Venn diagrams with up to 10 sets',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/darshandodamani/HyperVenn',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
