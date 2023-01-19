from setuptools import setup

setup(  name= 'helloworld', 
        version='0.0.1', 
        description='Say hello!', 
        py_modules=["helloworld"],
        package_dir={'': 'src'},
        install_requires = ["blessings ~= 1.7"],
        extras_require={
            "dev": [
                "pytest>=3.7",
            ],
        },
    )