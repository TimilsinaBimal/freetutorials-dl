import setuptools

with open("README.md", 'r+') as f:
    print("opened")
    long_desc = f.read()

setuptools.setup(
    name="freetutorials-dl",
    version="1.1",
    author="Timilsina Bimal",
    license="MIT",
    keywords=["freetutorialsdl", "downloader",
              "freetutorials", "fts-dl"],
    description="Downloader for freetutorials.ca",
    long_description=long_desc,
    url="https://github.com/TimilsinaBimal/freetutorials-dl",
    long_description_content_type="text/markdown",
    download_url="https://github.com/TimilsinaBimal/freetutorials-dl/archive/freetutorials-dlv1.0.tar.gz",
    install_requires=[
        'youtube-dl',
        'requests',
        'lxml',
        'bs4',
        'click',
    ],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    packages=['freetutorials_dl'],
    entry_points={
        'console_scripts': [
            'fts-dl=freetutorials_dl.cli:fts'
        ]
    },
    python_requires='>=3.6'
)
