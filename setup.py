from setuptools import setup, find_packages

setup(
    name="dss_homework_2",
    version="0.1.0",
    author="shalu shajan",
    author_email="shalu.shajan@fau.de",
    description="Maths quiz application",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/shalu-007-git/dsss_homework_2",
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
