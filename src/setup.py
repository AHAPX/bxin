from distutils.core import setup


setup(
  name = 'bxinth',
  packages = ['bxinth'],
  version = '0.1',
  description = 'Python lib for bx.in.th market',
  author = 'AHAPX',
  author_email = 'anarchy.b@gmail.com',
  url = 'https://github.com/AHAPX/bxin',
  download_url = 'https://github.com/AHAPX/bxin/archive/0.1.tar.gz',
  install_requires=[
    'pyotp==2.2.6',
    'requests==2.20.0'
  ],
  keywords = ['crypto', 'bx', 'bitcoin'],
  classifiers = [],
)
