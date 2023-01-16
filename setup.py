import os

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()

setup(
    name="turn_alerts_client",
    version="0.0.3",
    description="Client library for connecting with Turn notifications microservice.",
    long_description=README,
    long_description_content_type="text/markdown",
    license="",
    author="Amir Canto",
    author_email="",
    install_requires=["marshmallow>=3.19.0", "requests>=2.28.1"],
    dependency_links=[],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
    ],
)
