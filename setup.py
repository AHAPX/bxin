import setuptools
from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
  name='bxinth',
  packages=['bxinth'],
  package_dir={'bxinth': 'src/'},
  version='0.1.2',
  description='Python lib for bx.in.th market',
  long_description=long_description,
  license='MIT',
  author='AHAPX',
  author_email='anarchy.b@gmail.com',
  url='https://github.com/AHAPX/bxin',
  download_url='https://github.com/AHAPX/bxin/archive/v0.1.1.tar.gz',
  install_requires=[
    'pyotp==2.2.6',
    'requests==2.20.0'
  ],
  keywords=['crypto', 'bx', 'bitcoin'],
  classifiers=[],
)
