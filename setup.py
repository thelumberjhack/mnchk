from setuptools import setup


def readme():
    with open('README.rst') as fh:
        return fh.read()


setup(
    name='mnchk',
    version='0.1',
    description='Filter files based on the user provided Magic number.',
    long_description=readme(),
    classifiers=[
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
      'Programming Language :: Python :: 2.7',
      'Topic :: Utilities',
    ],
    keywords='afl testcases corpus magic number filter',
    url='http://github.com/yformaggio/mnchk',
    author='Yannick Formaggio',
    author_email='yannick@thelumberjhack.org',
    license='GPLv3+',
    packages=['mnchk'],
    entry_points={
        'console_scripts': ['mnchk=mnchk.command_line:main'],
    },
    include_package_data=True,
    zip_safe=False
)
