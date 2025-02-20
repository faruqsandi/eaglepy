from setuptools import setup, find_packages

setup(
    name="eaglepy",
    version="0.1.2",
    packages=find_packages(),
    description="Eagle API Wrapper for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Faruq Sandi",
    author_email="faruqsandi@gmail.com",
    url="https://github.com/faruqsandi/eaglepy",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    python_requires='>=3.6',
)
