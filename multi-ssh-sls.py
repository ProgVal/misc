#!/usr/bin/env python3

import sys

def main(fd):
    command = None
    for line in fd:
        if not line or line.startswith('#'):
            continue
        elif line.startswith('$'):
            command = line[1:].strip()
        else:
            (from_, to) = line.strip().split(' ', 1)
            assert ' ' not in to, repr(to)
            this_command = command.format(id=to)
            print('ssh slsu0-{id}.dsi-ext.ens-lyon.fr "{command}" &'.format(
                id=from_,
                command=this_command)
                )

if __name__ == '__main__':
    with open(sys.argv[1]) as fd:
        main(fd)
