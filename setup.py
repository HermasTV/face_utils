from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()


setup(
    name="face-utils",
    version="0.0.1",
    author="Hermas",
    author_email="a7medhermas@gmail.com",
    description="This is the ultimate face utils library ",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'cmake',
        'opencv-python',
        'face-recognition'
    ],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: MIT",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence :: Face Recognition "
    ],
    keywords="hermas digified python face utils test datection "
)