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
"""
print('Downloading lp_solve5')
subprocess.call(['wget', 'http://downloads.sourceforge.net/project/lpsolve/lpsolve/5.5.2.0/lp_solve_5.5.2.0_source.tar.gz', '-c'], stdout=subprocess.DEVNULL)
subprocess.call(['tar', 'xzf', 'lp_solve_5.5.2.0_source.tar.gz'])
shutil.rmtree('lp_solve5', ignore_errors=True)
os.rename('lp_solve_5.5', 'lp_solve5')
"""

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

# lp_solve5
# local install does not work for me
"""
os.chdir('lp_solve5/lpsolve55')
print('Compiling lpsolve')
subprocess.call(['sh', 'ccc'])
os.chdir('../../')
shutil.copyfile('lp_solve5/lpsolve55/bin/ux64/liblpsolve55.so',
    'lp_solve5/lpsolve55/liblpsolve55.so')
shutil.copyfile('lp_solve5/lpsolve55/bin/ux64/liblpsolve55.a',
    'lp_solve5/lpsolve55/liblpsolve55.a')
"""

# otawa
subprocess.call(['wget', 'http://www.irit.fr/bugzilla/attachment.cgi?id=56',
    '-O', 'cmakelists_lpsolve.diff', '-c'])
with open('cmakelists_lpsolve.diff') as fd:
    subprocess.call(['patch', 'otawa/CMakeLists.txt'], stdin=fd)
build_with_cmake('otawa')

## fix local lpsolve install
#shutil.copyfile(PREFIX + '/lib/otawa/ilp/lp_solve5.so',
#    PREFIX + '/lib/liblpsolve55.so')

# frontc
subprocess.call(['make', '-C', 'frontc/'])
subprocess.call(['make', '-C', 'frontc/', 'install', 'PREFIX=%s' % PREFIX])
