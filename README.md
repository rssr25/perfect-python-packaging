# How to package python packages (perfectly).
This is a text version of the youtube video: [Publishing (Perfect) Python Packages on PyPi](https://www.youtube.com/watch?v=GIF3LaRqgXo)

This guide assumes that you have some useful python code that is general enough to publish. :)

1. Create a directory with the name of your package. In the example above we have `helloworld`

2. Create `helloworld/src` source directory where your modules (the functionality (code) you want to package for other developers) sit. Each module is a `.py` file.

3. Create `helloworld/setup.py` write the following:
```python

from setuptools import setup

setup(
        name= 'helloworld', 
        version='0.0.1', 
        description='Say hello!', 
        py_modules=["module1"],
        package_dir={'': 'src'},
    ) 

```
Notice that we are using `setuptools` here, which is not a third-party dependency anymore. Think of the above code as a configuration for now. The arguments of this function tells `pip` how to install your package. This is the bare minumum information that you provide.

`name`: the package name you want people to use when they run the command `pip install name_of_package`

`version`: 0.0.x indicates an unstable version. When you upload a package for the first time you are likely to make mistakes. It is safer to have 0.0.1 for now.

`description`: self-explanatory

`py_modules`: the modules that the package uses, usually they sit in `src` dir.

`package_dir`: tells `setuptools` where our code is.

4. Let's check if the package has been correctly created. Build the package using `python setup.py bdist_wheel`. You should have the following new stuff.

- `\helloworld\build` directory which contains two more folders. The `build\lib` directory contains our modules.
- `\helloworld\dist` which constains our python wheel for distribuition.
- `\src\helloword.egg-info`

5. Check if the package is installing correctly using `pip install -e .` where `.` is the current directory where `setup.py` file is. The `-e` flag prevents the installation of this package in your system Python distribution.

6. You can now check the installation of the package in your Python interpreter:

```python
$ python
>>> from helloworld import hello_world
>>> hello_world("Rahul")
Hello Rahul!
>>> 
```

Congratulations! You have created your first package which you can upload to the PyPI. However, this guide is about uploading a "perfect" python package. So let's perfect it!
