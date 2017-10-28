# vim:fileencoding=utf8
from distutils.core import setup
import os
README = os.path.join(os.path.dirname(__file__),'PKG-INFO')
long_description = open(README).read() + "\n"

setup(name="vbcode",
      version='0.2.0',
      py_modules=['vbcode'],
      description="Variable byte codes",
      author="utahta",
      author_email = "labs.ninxit@gmail.com",
      long_description=long_description,
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: Python Software Foundation License",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Natural Language :: Japanese"
                   ],
      url="https://github.com/utahta/pyvbcode",
      license="MIT"
      )
