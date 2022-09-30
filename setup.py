# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name="a_utils",
    version="0.0.1",
    author="huihui",
    author_email="sunjiehuimail@foxmail.com",
    description="async utils",
    url="https://github.com/JiehuiSun/a-utils.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "aioamqp==0.15.0"
    ],
    python_requires=">=3.9"
)
