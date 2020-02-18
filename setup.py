from distutils.core import setup

long_description = open("README.rst").read()

setup(
    name="python-serpente",
    version="1.0.1",
    description="Roman numeral encoder and decoder",
    long_description=long_description,
    platforms=["any"],
    license="BSD License",
    author="Jeremy Carbaugh",
    author_email="jeremy@jcarbaugh.com",
    url="http://github.com/jcarbaugh/python-serpente/",
    py_modules=["serpente"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
