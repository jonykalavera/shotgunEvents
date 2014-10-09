from setuptools import setup, find_packages

setup(
    version='0.9',
    description='shotgun-events',
    long_description=open('README.mkd').read(),
    author='Shotgun Software',
    author_email='info@shotgunsoftware.com',
    name='shotgun_events',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
)

