import re
from setuptools import setup, find_packages
import sys

if sys.version_info.major != 3:
    print('This Python is only compatible with Python 3, but you are running '
          'Python {}. The installation will likely fail.'.format(sys.version_info.major))


extras = {
    'test': [
        'filelock',
        'pytest',
        'pytest-forked',
        'atari-py',
        'matplotlib',
        'pandas'
    ],
    'mpi': [
        'mpi4py'
    ]
}

all_deps = []
for group_name in extras:
    all_deps += extras[group_name]

extras['all'] = all_deps

setup(name='baselines_merl',
      packages=[package for package in find_packages()
                if package.startswith('baselines_merl')],
      install_requires=[
          'gym>=0.10.0, <1.0.0',
          'scipy',
          'tqdm',
          'joblib',
          'cloudpickle',
          'click',
          'opencv-python',
          'seaborn',
          'tensorflow==1.14.0'
      ],
      extras_require=extras,
      description='OpenAI baselines: high quality implementations of reinforcement learning algorithms',
      author='OpenAI',
      url='https://github.com/openai/baselines',
      author_email='gym@openai.com',
      version='0.1.5')

