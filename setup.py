from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()


setup(
    name="face-utils",
    version="0.0.1",
    include_package_data=True,
    author="Hermas",
    author_email="hermas@digified.io",
    description="opensource wrapper library for face detection algorithms and other utilities",
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
    keywords="face_utils face-utils hermas digified python face utils datection"
)