from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()


setup(
    name="face-utils",
    version="0.1.0",
    include_package_data=True,
    author="Hermas",
    author_email="a7medhermas@gmail.com",
    url="https://github.com/HermasTV/face_utils",
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
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence "
    ],
    keywords="face_utils face-utils hermas digified python face utils datection"
)
