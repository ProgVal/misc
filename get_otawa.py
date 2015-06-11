#!/usr/bin/env python3
import os
import shutil
import tempfile
import subprocess
import multiprocessing
from io import StringIO

PREFIX = os.path.expanduser('~/.local/')

def build_with_cmake(path):
    os.chdir(path)
    try:
        subprocess.call(['cmake', '.', '-DCMAKE_INSTALL_PREFIX=%s' % PREFIX])
        subprocess.call(['make', '-j', str(multiprocessing.cpu_count())])
        subprocess.call(['make', 'install'])
    finally:
        os.chdir('../')

modules = ('gliss2', 'armv5t', 'ppc2-vle', 'sparc', 'gel', 'elm', 'otawa',
        'frontc', 'oRange')
for module in modules:
    print('Cloning %s.' % module)
    subprocess.call(['hg', 'clone',
      'https://anon:ok@wwwsecu.irit.fr/hg/TRACES/%s/trunk' % module,
      module],
      stdout=subprocess.DEVNULL)

# gliss2
subprocess.call(['make', '-C', 'gliss2/'])
subprocess.call(['make', '-C', 'gliss2/', 'install', 'PREFIX=%s' % PREFIX])

# armv5
subprocess.call(['make', '-C', 'armv5t/'])
# no install?

# ppc2-vle
# source code not available…

# sparc
subprocess.call(['make', '-C', 'sparc/'])
# no install?

# gel
build_with_cmake('gel')

# elm
build_with_cmake('elm')

# otawa
subprocess.call(['wget', 'http://www.irit.fr/bugzilla/attachment.cgi?id=56',
    '-O', 'cmakelists_lpsolve.diff', '-c'])
with open('cmakelists_lpsolve.diff') as fd:
    subprocess.call(['patch', 'otawa/CMakeLists.txt'], stdin=fd)
build_with_cmake('otawa')

# frontc
subprocess.call(['make', '-C', 'frontc/'])
subprocess.call(['make', '-C', 'frontc/', 'install', 'PREFIX=%s' % PREFIX])
