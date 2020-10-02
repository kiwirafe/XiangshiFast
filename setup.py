import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="XiangshiFast", # Replace with your own username
    version="1.1.2",
    author="kiwirafe",
    author_email="kiwirafe@gmail.com",
    description="相识极速版本",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiwirafe/xiangshi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'jieba',
    ],
    python_requires='>=3.4',
)
