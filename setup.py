from setuptools import setup, find_packages

setup(name='python_file_utils',
    version='0.0.5',
    description='common file functions',
    author='lynzt',
    url='https://github.com/lynzt/python_file_utils',
    packages=['file_utils'],
    install_requires=[
        'urllib3==1.26.5',
    ],
)
