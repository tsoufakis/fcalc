from setuptools import setup

setup(
    name='fcalc',
    packages=['fcalc'],
    install_requires=[
        'Flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
