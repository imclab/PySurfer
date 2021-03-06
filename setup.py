#! /usr/bin/env python
#
# Copyright (C) 2011 Alexandre Gramfort <gramfort@nmr.mgh.harvard.edu>
#                    Michael Waskom <mwaskom@mit.edu>
#                    Scott Burns <sburns@nmr.mgh.harvard.edu>

descr = """PySurfer: Python / FreeSurfer / Mayavi2 for brain imaging"""

import os
# deal with MPL sandbox violations during easy_install
os.environ['MPLCONFIGDIR'] = '.'

# get the version, don't import surfer here so setup works on headless systems
version = None
with open(os.path.join('surfer', '__init__.py'), 'r') as fid:
    for line in (line.strip() for line in fid):
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('"')
            break
if version is None:
    raise RuntimeError('Could not determine version')

DISTNAME = 'pysurfer'
DESCRIPTION = descr
LONG_DESCRIPTION = descr
MAINTAINER = 'Michael Waskom'
MAINTAINER_EMAIL = 'mwaskom@stanford.edu'
URL = 'http://pysurfer.github.com'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/nipy/PySurfer'
VERSION = version

from setuptools import setup

if __name__ == "__main__":
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    setup(name=DISTNAME,
        maintainer=MAINTAINER,
        include_package_data=True,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        long_description=LONG_DESCRIPTION,
        zip_safe=False,  # the package can run out of an .egg file
        classifiers=['Intended Audience :: Science/Research',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved',
                     'Programming Language :: Python',
                     'Topic :: Software Development',
                     'Topic :: Scientific/Engineering',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'
                     ],
         platforms='any',
         packages=['surfer', 'surfer.tests'],
         scripts=['bin/pysurfer'],
    )
