#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup

requires = [
    'celery[redis]==4.1.0',
    'requests-celery-adapters==2.0.4',
    'six>=1.11.0'
            ]

extras_require = {
    'test': [
        'pytest>=3.2.2'
    ],
}


setup(name='celery-crossover',
      version='1.1.0',
      description='Celery Crossover aims to make it really easy to execute tasks in another service.',
      author='Daniel Debonzi',
      author_email='debonzi@gmail.com',
      install_requires=requires,
      extras_require=extras_require,
      url='https://github.com/debonzi/celery_crossover',
      packages=['crossover', 'examples'],
      )
