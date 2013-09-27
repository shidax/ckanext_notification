from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-notification',
	version=version,
	description="Twitter notification plugin",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Takahiro Shida',
	author_email='shida@intellilink.co.jp',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.notification'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	notification=ckanext.notification.plugin:TwitterNotificationPlugin
	""",
)
