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
        py_modules=["helloworld"],
        package_dir={'': 'src'},
    ) 

```
Notice that we are using `setuptools` here, which is not a third-party dependency anymore. Think of the above code as a configuration for now. The arguments of this function tells `pip` how to install your package. This is the bare minumum information that you provide.

`name`: the package name you want people to use when they run the command `pip install name_of_package`

`version`: `0.0.x` indicates an unstable version. When you upload a package for the first time you are likely to make mistakes. It is safer to have `0.0.1` for now.

`description`: self-explanatory

`py_modules`: the modules that the package uses, usually they sit in `src` dir.

`package_dir`: tells `setuptools` where our code is.

<br>

4. Let's check if the package has been correctly created. Build the package using `python setup.py bdist_wheel`. You should have the following new stuff.

    - `\helloworld\build` directory which contains two more folders. The `build\lib` directory contains our modules.
    - `\helloworld\dist` which constains our python wheel for distribuition.
    - `\src\helloword.egg-info`

<br>

5. Check if the package is installing correctly using `pip install -e .` where `.` is the current directory where `setup.py` file is. The `-e` flag prevents the installation of this package in your system Python distribution.

<br>

6. You can now check the installation of the package in your Python interpreter:

```python
$ python
>>> from helloworld import hello_world
>>> hello_world("Rahul")
Hello Rahul!
>>> 
```

Congratulations! You have created your first package which you can upload to the PyPI. However, this guide is about uploading a "perfect" python package. So let's perfect it!

<hr>

## Cleaning up a little
Let's clean-up our project a little. We see that we have created some files that are not necessary to push on github. Head to [gitignore.io](https://www.gitignore.io) and search for `python`. It will spit out a text that we will put in a `.gitignore` file which does some housekeeping for the files that are not necessary to push on GitHub.

Create a `.gitignore` file for your repository and paste the output of your search on `gioignore.io`.

## License?
If you are going to publish your code, you need to license it. Without a license we haven't given permission to distribute our code. People can look at it but not copy it yet! So we need a `license.txt` file. If you don't know ins and outs of licenses [ChooseALicense](https://choosealicense.com) is a good place to understand the permissions and restrictions of different licenses.

## Classifiers
TBC