from setuptools import setup, find_packages

setup(
    name='Pycharm',
    version='1.0',
    author='anonim',
    packages=find_packages(include=['Pycharm', 'Pycharm.*']),
    install_requires=['django',
                      'pytz',
                      'djangorestframework',
                      'pytest'
                      ]
)
