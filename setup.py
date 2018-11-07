from setuptools import setup, find_packages

setup(
    name='n4j_movies',
    version='0.1',
    description='Simple app to work with the neo4j movie database',
    url='https://github.com/ruffyleaf/n4j_movies',
    author='ruffyleaf',
    author_email='ruffyleaf@hotmail.com',
    packages=find_packages(),
    zip_safe=False
)