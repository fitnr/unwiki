from setuptools import setup

version = '0.1.0'

try:
    long_desc = open('README.rst').read()
except IOError:
    long_desc = ''

setup(
    name='unwiki',
    version=version,
    description='Python module to remove wiki markup',
    long_description=long_desc,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords="wiki",
    author="Neil Freeman",
    author_email='contact@fakeisthenewreal.org',
    url='https://github.com/fitnr/unwiki',
    license='GPL',
    test_suite='tests',
    packages=['unwiki']
)
