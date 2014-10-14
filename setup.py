from distutils.core import setup
import subprocess
import sys

def assert_clean():
    output = subprocess.check_output(["git", "status", "--porcelain"])
    dirty_files = sum(1 for line in output)
    if dirty_files > 0:
        print "The repository is not in a clean state. please commit, stash or ignore files before building"
        sys.exit(1)

def get_version():
    try:
        output = subprocess.check_output(['git', 'describe'])
    except:
        print "could not obtain a version using git describe, maybe you need to tag (release) the project first?"
        sys.exit(1)
    return output.strip()

assert_clean()

setup(name='foo',
      version=get_version(),
      py_modules=['foo'],
      )
