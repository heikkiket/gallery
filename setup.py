import setuptools

setuptools.setup(
    name='gallery',
    version='0.1.0',
    install_requires=["tomli"],
    entry_points={
        "console_scripts": ["gallery=gallery:main"],
    }
)
