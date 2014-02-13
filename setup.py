#!/usr/bin/env python

from distutils.core import setup
import os

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('unsubscribe'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[12:] # Strip "newmanutils" or "newmanutils"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(name='Django Unsubscribe',
      version='0.01',
      description='Django Unsubscribe make it menial to attach the proper '\
                'unsubscribe methods to newsletter-type e-mails.',
      author='Michael Newman',
      author_email='newmaniese@gmail.com',
      packages=packages,
      package_data={'newmanutils': data_files},
)
