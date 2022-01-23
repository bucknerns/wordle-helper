import os

from setuptools import find_namespace_packages, setup

import versioneer

os.chdir(os.path.abspath(os.path.dirname(__file__)))

setup(
    name="wordle-helper",
    version=versioneer.get_version(),
    description="Wordle Helper",
    long_description="{0}".format(open("README.md").read()),
    author="None",
    author_email="None",
    url="git@github.com:bucknerns/wordle-helper.git",
    packages=find_namespace_packages("src"),
    python_requires=">=3.8.0",
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: Other/Proprietary License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python"],
    package_dir={"": "src"},
    entry_points={"console_scripts": []},
    cmdclass=versioneer.get_cmdclass())
