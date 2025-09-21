from setuptools import setup, find_packages

setup(
    name="vexaauth",
    version="0.1.0",
    description="Discord global verification bot with MongoDB Cloud and OAuth2",
    author="Tanisha",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "discord.py>=2.4.0",
        "pymongo>=4.9.0"
    ],
    python_requires=">=3.9",
)
