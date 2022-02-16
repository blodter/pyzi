from setuptools import setup

setup(
	name='PyZI',
	version='0.1.0',
	description='Python wrapper for ZoomInfo\'s API.',
	url='https://github.com/blodter/pyzi',
	author='Brayden Lodter',
	author_email='blodter@gmail.com',
	install_requires=[
		'cachetools==5.0.0',
		'fuzzywuzzy==0.18.0',
		'python-dateutil==2.8.2',
		'requests==2.27.1',
		'zi-api-auth-client==1.0.2',
	],
	zip_safe=False
)
