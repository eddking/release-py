#!/usr/bin/env python

"""Usage: release.py
       [--major  | --minor | --patch]
       [--help]

  This script will help you perform a software release

--help       show this
--major      increment the major version
--minor      increment the minor version
--patch      increment the patch version
"""

from pkg_resources import parse_version
import subprocess
from docopt import docopt
import sys
import time

def assert_clean():
    output = subprocess.check_output(["git", "status", "--porcelain"])
    dirty_files = sum(1 for line in output)
    if dirty_files > 0:
        print "The repository is not in a clean state. please commit, stash or ignore files before continuing"
        sys.exit(1)

def get_version():
    try:
        output = subprocess.check_output(['git', 'describe'])
    except:
        print "could not obtain a version using git describe, maybe you need to tag (release) the project first?"
        sys.exit(1)
    return output.strip()

def _intOrZero(value):
    try:
        return int(value)
    except:
        return 0

def _parse_current_version():
    try:
        output = subprocess.check_output(['git', 'describe'])
    except:
        print 'Warning, no current version tag found, assuming this is the first release'
        return [0, 0, 0]
    parts = list(parse_version(output))

    major = _intOrZero(parts[0])
    minor = _intOrZero(parts[1])
    patch = _intOrZero(parts[2])

    return [major, minor, patch]

def _version_to_string(version):
    return '.'.join([str(num) for num in version])

def _readYN(prompt):
    while True:
        val = raw_input(prompt).lower().strip()
        if val == "y":
            return True
        if val == "n":
            return False
        print "Couldnt parse your response, please answer 'y' or 'n'"

def main():
    assert_clean()
    args = docopt(__doc__)
    major = args.get('--major')
    minor = args.get('--minor')
    patch = args.get('--patch')

    #Default is patch
    if patch:
        increment = 2
    elif minor:
        increment = 1
    elif major:
        increment = 0
    else:
        print "please specify whether you are releasing a major minor or patch version"
        sys.exit(1)

    words = ['major', 'minor', 'patch']
    print 'Releasing a {} version'.format(words[increment])

    version = _parse_current_version()
    print 'The current version is: ' + _version_to_string(version)

    version[increment] = version[increment] + 1
    if increment < 1:
        version[1] = 0
    if increment < 2:
        version[2] = 0

    print 'The released version will be: ' + _version_to_string(version)
    yes = readYN('Is this correct? (y/n)\n')

    if not yes:
        print 'Aborting'
        sys.exit(0)

    version_str = _version_to_string(version)
    print 'Tagging new version'
    command = ['git', 'tag', version_str, '-a', '-m', 'Release ' + version_str + ' ' + time.strftime("%d/%m/%Y %H:%M:%S")]
    print ' '.join(command)
    code = subprocess.check_call(command)
    if code != 0:
        print 'git returned non 0 exit code'
        print 'failed!'
        sys.exit(1)

    print 'Success!'
    print 'If eveything is in order then you should share this release! do a "git push --tags"'

if __name__ == '__main__':
    main()
