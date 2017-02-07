from codecs import open
from os import path

from setuptools import setup, find_packages
from cmsplugin_yandex_maps import __version__

here = path.abspath(path.dirname(__file__))

setup(
    name='cmsplugin-yandex-maps',
    version=__version__,
    url='https://github.com/Atterratio/cmsplugin-yandex-maps',
    license='MIT',
    author='Aeternus Atterratio',
    author_email='atterratio@gmail.com',
    description='Rich functionality Yandex Maps plugin for Django-CMS',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='Django Django-CMS Yandex Map',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django>=1.7', 'django-cms>=3'],
)
