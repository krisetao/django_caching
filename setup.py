# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django_caching',
    version='0.1.1',
    keywords=('django', 'cache', 'caching'),
    description='A easy using django cache manager.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    license='Apache License',
    install_requires=['django>=1.8'],

    author='NineChapter',
    author_email='daniel48@126.com',

    packages=find_packages(),
    platforms='any',
)
