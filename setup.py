from setuptools import setup, find_packages
import re

version = ''
with open('pyroom/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Version is not set')

readme = 'See https://github.com/Dalloriam/pyroom for README.'

setup(
    name='pyroom',
    author='Dalloriam',
    url='https://github.com/Dalloriam/pyroom',
    version=version,
    packages=find_packages(),
    license='MIT',
    description='Quick & dirty Adobe Lightroom catalog manager',
    long_description=readme,
    install_requires=[]
)
