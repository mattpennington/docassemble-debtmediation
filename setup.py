import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.debtmediation',
      version='0.1',
      description=('Onboarding tool for debt mediation'),
      long_description='# docassemble.debtmediation\r\n\r\n## Author\r\n\r\nMatt Pennington - [Tonic Workflows](https://workflow.tonic.works/)\r\n\r\n## Overview\r\n\r\nA docassemble demo interview for Debt Mediation Onboarding that uses a combination of Multi-User Interviews + SMS + Email.\r\n\r\n## Notice\r\n\r\nThis is not intended as a finished interview - it\'s a working example to showcase one way that SMS and Email can be used to implement a Multi-User Interview in a vaguely "real world" scenario.\r\n## Requirements\r\n\r\nYour Docassemble Server will need configuring with:\r\n\r\n* A [Twilio](https://www.twilio.com/) Account (a [trial project](https://www.twilio.com/console/projects/create) is sufficient providing you have two unique mobile numbers you can add to it for the purposes of running this demo ^) - [configuration instructions](https://docassemble.org/docs/config.html#twilio) and [more about Twilio trial accounts](https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account)\r\n* The ability to send emails out - [configuration instructions](https://docassemble.org/docs/config.html#mail)\r\n\r\n^as an alternative if you only have access to one mobile number you can disable the *debtor.mobile_number == applicant.mobile_number* validation code.\r\n## Preview\r\n\r\n[Watch on youtube](https://youtu.be/l_9kGOIzx2U)\r\n',
      long_description_content_type='text/markdown',
      author='Matt Pennington',
      author_email='mp@tonic.works',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/debtmediation/', package='docassemble.debtmediation'),
     )

