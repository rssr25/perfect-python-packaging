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

## Classifiers make life easier. :heart:
We need to set-up some classifiers so that people searching on PyPi can find our package based on a criteria. For example, a programmer searching for some package may write a classifer to search for it to run on Python 3.7, etc. You can provide this information in classifiers.

```python
setup( 
    ... #other arguments to setup() :)
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLV2+)!",
        "Operating System :: OS Independent",
    ],
)
```
To know more about classifiers, head to [Classifers](https://pypi.org/classifiers). There are a bunch of classifiers, try them and apply all the useful classifiers to your project.

## Documentation is your :massage:
Before we jump onto documenting the code, we need to know in which format you want to write the documentation. There are generally two choices at the moment.


|  ReStructured Text | Markdown         |
|--------------------|------------------|
| Pythonic           | More widespread  |
|  Powerful          | Simpler          |
|  Can use Sphinx    | Can use MkDocs   |

ReStructured Text is written in Python and widely used in the Python community. It is a Python solution. If you have a project that uses code from multiple languages then probably you are more familiar with MarkDown. It is more simpler but also less powerful. Both of these are supported by [readthedocs.org](https://readthedocs.org) :)

Once we have decided from the two choices above, we need to have soem sections in the document that are more or less quite general to any documentation. They are as follows (we use markdown for example here)

1. A `readme.md` file that has:
    - Title: the title of the project and a small paragraph describing what the project does. 

        ```markdown
        # Hello World
        This is an example project demonstrating how to publish a Python module to PyPi.
        ```
    - Installation: A section telling how to install the project
        ```markdown
        ## Installation
        Run the following to install:
           pip install helloworld
    
    - Some example code to tell how to use the code

        ```markdown
        from helloworld import say_hello
        # Generate "Hello, World!"
        say_hello ()
        # Generate "Hello, Everybody!"
        say_hello("Everybody")
        ```
2. Other stuff that you want the developers to pay attention to.

Once we have written this, we would also like to publish this on PyPi. It will be really nice to make this readme.md as the official description of the project on PyPi. Now, PyPi can use markdown directly to incorporate your .md readme(s) directly into the package.

```python
from setuptools import setup

with open ("READMEmd", "r") as fh:
    long_description = fh.read ()

setup(
    ... #other stuff written before
    long_description=long_description,
    long_description_content_type="text/markdown",
)
```

## Add your Library dependencies
You must have seen in a lot of python projects there are dependencies that make your project work. You can add the dependencies directly in the `setup()` function like below.

```python
setup(
    install_requires = [
        "blessings ~= 1.7", #this is an example of a dependency
    ],
)
```

Add the dependency in your `setup.py` and check if it installs everything using `pip install -e .`

## Test with `pytest`
To ensure that everything is working fine, after installation, it makes sense to run some tests. But, we don't have any tests with us and it makes no sense to check every function randomly in your package to make sure the things work.

For testing `pytest` is a good recommendation. But in order to run some tests using `pytest` we need more dependencies. This time they are not library dependencies as discussed in the previous section, but they are <b>development dependencies</b>. 

In order to add these development dependencies in `setup()` function, add them as extras. A lot of people use `requirements.txt` for these development dependencies, well you can directly add them to your package setup.

```python
setup(
    ... #previously written stuff
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
)
```
Now we want to tell people how to use it, again we update the `readme.md`.

```markdown
# Developing Hello World 
To install helloworld, along with the tools you need to develop and run tests, run the following in your virtualenv:

$ pip install -e .[dev]
```
This is how you install the development dependencies so that you can run the tests. The `.[dev]` says "we are installing the current module with the dev extras".

<p style="text-align: center;"> ---------- A small detour ---------- </p>
<b> Question 1: </b> What is the difference between install_requires and extras_requires?

<b>install requires</b>
- is for production dependencies (Flask, Click, Numpy, Pandas)
- versions should be as relaxed as possible ( >3.0, <4.0 ) to not lock your users.

<b>extras_require</b>
- is for optional requirements: (Pytest, Mock, Coverage.y)
- versions should be as specific as possible

<br>

<b>Question 2: </b> What about `requirements.txt`? <br>
It still has a place but it:

- is for Apps being deployed on machines you control.
- Uses fixed version numbers, eg: requests==2.22.0
- Is generated with pip freeze > requirements.txt

<p style="text-align: center;"> ---------- A small detour that ended ---------- </p>

Now we can write tests. Here we use `test_helloworld.py`

```python
#test_helloworld.py
def test_helloworld_no_params ():
    assert say_hello () == "Hello, World!"

def test_helloworld_with_param ():
    assert say_hello ("Everyone") == "Hello, Everyone!"
```

To run the test just write `pytest` in console:

```bash
$ pytest 
============== test session starts ===========: 
platform darwin -- Python 3.6.3, pytest-3.7.2, 
py-1.5.4, pluggy-0.7.1
rootdir: /path/to/helloworld, inifile:
collected 2 items
test_helloworld.py ..                    [100%]
========= 2 passed in 0.02 seconds ===========
```