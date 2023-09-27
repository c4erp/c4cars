from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in c4cars/__init__.py
from c4cars import __version__ as version

setup(
	name="c4cars",
	version=version,
	description="Car Service Center",
	author="Connect 4 Systems",
	author_email="connect4system@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
