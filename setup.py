from setuptools import setup, find_packages

print find_packages()
setup(name='python_file_utils',
    version='0.0.3',
    description='common file functions',
    author='lynzt',
    url='https://github.com/lynzt/python_file_utils',
    packages=['file_utils'],
    )
