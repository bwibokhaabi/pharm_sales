#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirement_file:
    requirements_list = requirement_file.readlines()
    requirements_list = [lib.replace('\n', '') for lib in requirements_list]

requirements = requirements_list

test_requirements = []

setup(
    author="Daisy Okacha",
    author_email="daisyokacha9@gmail.com",
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta-Release',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="10 Academy Time-Series Project.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='scripts',
    name='scripts',
    packages=find_packages(include=['scripts', 'scripts.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bwibokhaabi/pharm_sales',
    version='1.0.0',
    zip_safe=False,
)