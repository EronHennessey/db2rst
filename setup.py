#!/usr/bin/env python
from distutils.core import setup

script_names = [ 'scripts/db2rst' ]

setup(name = 'db2rst',
      author = 'Eron Hennessey',
      author_email = 'eron@abstrys.com',
      description = 'Convert DocBook to reStructuredText',
      requires = [ 'lxml' ],
      scripts = script_names,
      url = 'https://github.com/EronHennessey/db2rst',
      version = '0.5')

