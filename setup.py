from setuptools import setup, find_packages

# Read requirements.txt
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="ml_project",
    version="0.1.0",
    author="Sai",
    description="Machine Learning project",
    packages=find_packages(),
    install_requires=requirements,
)
