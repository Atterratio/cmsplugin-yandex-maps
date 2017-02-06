from codecs import open
from os import path

from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cmsplugin-yandex-maps',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/Atterratio/cmsplugin-yandex-maps',
    license='MIT',
    author='Aeternus Atterratio',
    author_email='atterratio@gmail.com',
    description='Rich functionality Yandex Maps plugin for Django-CMS',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='Django Django-CMS Yandex Map',
    include_package_data=True,
    install_requires=['Django>=1.7', 'django-cms>=3'],
)
