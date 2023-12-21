#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2023 Edwin.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import itertools
import os.path
import sys

try:
    xrange  # Python 2
except NameError:
    xrange = range  # Python 3


def main():
    # (alias, full, allow_when_oneof, incompatible_with)
    cmds = [('tf', 'terraform', None, None)]

    ops = [
        ('i', 'init', None, ['p', 'a', 'ws', 'o', 'st', 'imp']),
        ('p', 'plan', None, ['i', 'a', 'ws', 'o', 'st', 'imp']),
        ('a', 'apply', None, ['p', 'i', 'ws', 'o', 'st', 'imp']),
        ('ws', 'workspace', None, ['p', 'a', 'i', 'o', 'st', 'imp']),
        ('o', 'output', None, ['p', 'a', 'i', 'ws', 'st', 'imp']),
        ('imp', 'import', None, ['p', 'a', 'i', 'ws', 'o', 'st']),
        ('st', 'state', None, ['p', 'a', 'i', 'ws', 'o', 'imp']),

    ]

    res = [
        ('ls', 'list', ['ws', 'st'], None),
        ('se', 'select', ['ws'], None),
        ('del', 'delete', ['ws', 'st'], None),
        ('rm', 'rm', ['st'], None),
        ('nw', 'new', ['ws'], None),
        ('sh', 'show', ['ws', 'st'], None),
        ('mv', 'mv', ['st'], None),
        ('rp', 'replace-provider', ['st'], None),
        ('push', 'push', ['st'], None),
        ('pull', 'pull', ['st'], None),
    ]
    res_types = [r[0] for r in res]

    args = [
        ('des', '-destroy', ['p', 'a'], ['ref', 'a']),
        ('ref', '-refresh-only', ['p'], ['des']),
        ('aa', '-auto-approve', ['a'], None),
        ('lf', '-lock=false', ['p', 'a'], None),
        ('up', '--upgrade', ['i'], None),
    ]
    
    # these accept a value, so they need to be at the end and
    # mutually exclusive within each other.
    positional_args = [
        ('noc', '-no-color', ['p', 'a'], None)
    ]

    # [(part, optional, take_exactly_one)]
    parts = [
        (cmds, False, True),
        (ops, True, True),
        (res, True, True),
        (args, True, False),
        (positional_args, True, True),
    ]

    shellFormatting = {
        "bash": "alias {}='{}'",
        "zsh": "alias {}='{}'",
        "fish": "abbr --add {} \"{}\"",
    }

    shell = sys.argv[1] if len(sys.argv) > 1 else "bash"
    if shell not in shellFormatting:
        raise ValueError("Shell \"{}\" not supported. Options are {}"
                         .format(shell, [key for key in shellFormatting]))

    out = gen(parts)

    # prepare output
    if not sys.stdout.isatty():
        header_path = \
            os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         'license_header')
        with open(header_path, 'r') as f:
            print(f.read())

    for cmd in out:
        print(shellFormatting[shell].format(''.join([a[0] for a in cmd]),
              ' '.join([a[1] for a in cmd])))


def gen(parts):
    out = [()]
    for (items, optional, take_exactly_one) in parts:
        orig = list(out)
        combos = []

        if optional and take_exactly_one:
            combos = combos.append([])

        if take_exactly_one:
            combos = combinations(items, 1, include_0=optional)
        else:
            combos = combinations(items, len(items), include_0=optional)

        # permutate the combinations if optional (args are not positional)
        if optional:
            new_combos = []
            for c in combos:
                new_combos += list(itertools.permutations(c))
            combos = new_combos

        new_out = []
        for segment in combos:
            for stuff in orig:
                if is_valid(stuff + segment):
                    new_out.append(stuff + segment)
        out = new_out
    return out


def is_valid(cmd):
    for i in xrange(0, len(cmd)):

        # check at least one of requirements are in the cmd
        requirements = cmd[i][2]
        if requirements:
            found = False
            for r in requirements:
                for j in xrange(0, i):
                    if cmd[j][0] == r:
                        found = True
                        break
                if found:
                    break
            if not found:
                return False

        # check none of the incompatibilities are in the cmd
        incompatibilities = cmd[i][3]
        if incompatibilities:
            found = False
            for inc in incompatibilities:
                for j in xrange(0, i):
                    if cmd[j][0] == inc:
                        found = True
                        break
                if found:
                    break
            if found:
                return False

    return True


def combinations(a, n, include_0=True):
    l = []
    for j in xrange(0, n + 1):
        if not include_0 and j == 0:
            continue
        l += list(itertools.combinations(a, j))
    return l


def diff(a, b):
    return list(set(a) - set(b))


if __name__ == '__main__':
    main()
