from setuptools import setup, find_packages

setup(name='python_file_utils',
    version='0.0.5',
    description='common file functions',
    author='lynzt',
    url='https://github.com/lynzt/python_file_utils',
    packages=['file_utils'],
    dependency_links=[
      'git+git://github.com/lynzt/python_utils.git',
    ],
)
