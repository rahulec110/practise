"""
Install pytest using pip (pip3 install pytest)

##### Naming Conventions of PyTest ###########
1) File name should start with "test_PytestExample1.py"
2) Method name should start with "test_methodA"

######## 3 Ways of executing the code in pytest #############

py.test -v -s files_path    # run all tests in specific files_path
py.test -v -s test_mod.py py.  # run tests in module or in test file
py.test -v -s test_module.py::test_method  # only run test_method in test_module.py

-v : verbose (verbose is an argument which is used to report more information about an operation in your program )
-s : to print statements
"""

def test_methodA():
    print('This is methos A')

def test_methodB():
    print('This is method B')


"""
1. go to the Pytest_Concept directory :
   py.test : all files will executed without printed values/content
   py.test -v -s : whatever the data is available under methods will also print. 
2. To print particular file
   >> Go to the particular directory
   py.test -v -s test_Example1.py
3. Tp run single method of any particular file
   py.test -v -s test_Example1.py::test_methodA
"""