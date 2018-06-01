from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(name='priorityscheduler',
      version='0.2',
      description='Priority Queue to schedule custom jobs',
      url='https://github.com/TomOrth/Priority-Queue-Job-Scheduler',
      download_url='https://github.com/atf1999/executioner/tarball/0.2',
      author='Tom Orth',
      author_email='torth212@gmail.com',
      license='MIT',
      packages=['priorityscheduler'])