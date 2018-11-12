from setuptools import setup, find_packages

setup(
	name = 'some_package',
	description = 'Demonstrate packaging and distribution',
	version = '1.0',
	author = 'Siyu Xiang',
	author_email = 'siyu.xiang@cgu.edu',
	packages = find_packages(where = 'src'),
	package_dir = {'':'src'},
	)