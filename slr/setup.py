from setuptools import setup
setup(
    name = 'slr',
    version = '0.1.0',
    packages = ['slr'],
    entry_points = {
        'console_scripts': [
            'slr = slr.__main__:main'
        ]
    })