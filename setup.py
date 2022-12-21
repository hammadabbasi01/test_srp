from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in test_srp/__init__.py
from test_srp import __version__ as version

setup(
	name="test_srp",
	version=version,
	description="This is for testing purpose",
	author="SRP Global",
	author_email="info@srp.ai",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
