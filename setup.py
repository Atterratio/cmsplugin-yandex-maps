from setuptools import setup, find_packages
from cmsplugin_yandex_maps import __version__

REQUIREMENTS = [
    'django-cms>=3.0.0',
	'django>=1.7',
]


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='cmsplugin-yandex-maps',
    version=__version__,
    url='https://github.com/Atterratio/cmsplugin-yandex-maps',
    license='MIT',
    author='Aeternus Atterratio',
    author_email='atterratio@gmail.com',
    description='Rich functionality Yandex Maps plugin for Django-CMS',
    long_description=open('README.rst').read(),
    install_requires=REQUIREMENTS,
	classifiers=CLASSIFIERS,
    keywords='Django Django-CMS Yandex Map',
    packages=find_packages(),
    include_package_data=True,
)
