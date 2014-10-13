from setuptools import setup, find_packages

setup(
    name = "pymuxinator",
    version = "0.0.1",
    author = "Caleb Mingle",
    author_email = "caleb@mingle.cm",
    description = "Python version of Tmuxinator",
    url = "http://caleb.io",
    packages = find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pymuxinator = pymuxinator:main',
        ],
    },
    tests_require=[
        "nose>=1.0",
        "mock>=1.0",
    ],
    install_requires=[
        "pyyaml>=1.0",
        "Jinja2>=1.0",
    ],
    test_suite = "nose.collector"
)
