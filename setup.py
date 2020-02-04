try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import glob
import os
import sys

def package_files(package_dir,subdirectory):
    # walk the input package_dir/subdirectory
    # return a package_data list
    paths = []
    directory = os.path.join(package_dir, subdirectory)
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            path = path.replace(package_dir + '/', '')
            paths.append(os.path.join(path, filename))
    return paths
#data_files = package_files('src','data')

setup_args = {
    'name': 'chatAI',
    'author': 'Shall not be named',
    'package_dir': {'chatter': 'src'},
    'packages': ['chatter'],
    'scripts': glob.glob('scripts/*'),
    'version': '0.0.1',
}


if __name__ == '__main__':
    setup(**setup_args)
