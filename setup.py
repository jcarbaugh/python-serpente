from distutils.core import setup
from serpente import __version__

long_description = open('README.rst').read()

setup(
    name='python-serpente',
    version=__version__,
    description='Roman numeral encoder and decoder',
    long_description=long_description,
    platforms=["any"],
    license='BSD License',
    author='Jeremy Carbaugh',
    author_email='jeremy@200ok.net',
    url='http://github.com/jcarbaugh/python-serpente/',
    py_modules=['serpente'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)