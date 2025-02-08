import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()

install_requires = []
with open("requirements.txt", "r") as fp:
    for line in fp.readlines():
        if line.strip():
            install_requires.append(line.strip())

setuptools.setup(
    name="rawdog_django_orm",
    version="0.0.5",
    author="George3d6",
    description="Utilities for using the django orm outside of django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/orgs/trysimpler/rawdog_django_orm",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
