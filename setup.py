from setuptools import setup

setup(
    name='Chess-Magic-Card',
    version='0.1',
    packages=['CMC'],
    url='',
    license='',
    author='Nguyen Hoang Viet, Tran Doan Thanh Vuong',
    author_email='',
    description='',
    include_package_data=True,
    entrypoints={"console_scripts": ["Chess-Magic-Card=CMC.main:game_intro"]},
)
