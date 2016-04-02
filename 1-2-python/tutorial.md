# Week 1: Python Tutorial


### Table of Contents

TODO

### Introduction
---

This tutorial covers all the basics you need to know to work with Python
on the machines in the computer rooms. All material for this course was based largely on the
[original material](http://ai.berkeley.edu/project_overview.html) from the University of California, Berkeley.

#### Assignment submissions

Submissions of assignments will happen using the usual Blackboard
assignment submission system, where for each assignment you should
upload the .py file(s) containing your assignment solution. Make sure
that **only one member** of your group submits your assignment. 

When you submit your assignment, you must make sure that **the names and student numbers (including prefix-s) of all members** are present in the assignment files, as comments. For example:

```python
# Bobby Tables (s123456)
# Guidum van Rosso (s654321)
```

For this assignment, you will need to hand in the file `buyLotsOfFruit.py` after completing it for Problem 1.

### Getting started
---

The programming assignments in this course will be written in
[Python](http://www.python.org/about/), an interpreted, object-oriented
language. This tutorial will walk through the primary syntactic
constructions in Python, using short examples. Python code files end in the extension `.py`.

You may find the [Troubleshooting](#Troubleshooting) section helpful if
you run into problems. It contains a list of some problems previous students
have frequently encountered when following this tutorial.

Like languages such as Lisp, Scheme and Prolog, Python is an interpreted
language: it can execute source code commands directly, without having
to be compiled first. It can therefore be used in two modes: either by
executing a source file (called a *script* in Python), or
*interactively* by typing in commands one-by-one and having Python
execute them directly. In the exercises below, we will first use the
Python interpreter interactively, then move to writing scripts.

But before we can start on the exercises, you should be able to invoke
and use both the Python interpreter itself, and the Integrated
Development Environment (IDE) PyCharm that we will use for writing and
executing scripts.

#### Invoking the Interpeter

To invoke the interactive **Python Interpreter** outside of an IDE, you
first need to start a *command-prompt*. In Windows you find this by opening
the Start Menu and typing `Command Prompt` or `cmd`, or on older versions,
under `Start -> Accessories -> System Tools -> Command Prompt`.

This will open a window like this:

![](images/cmdprompt.gif)

From the 'command-prompt', you start the Python interpreter by typing
the command 'python'.

Alternatively, you can also open the python interpreter from within the IDE PyCharm by
selecting `Run Python Console ...` from the `Tools` menu. See the
next section for more on the PyCharm IDE.

Either way you will be presented with a message looking something like
the following (the actual numbers may vary depending on the python
version installed and operating system you are running on):

```
Python 3.4.0 (v3.4.0:04f714765c13, Mar 15 2014, 23:02:41) [GCC 3.4.6] on win64
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

#### Using PyCharm

[PyCharm](http://www.jetbrains.com/pycharm/documentation/) is an
Integrated Development Environment for developing Python programs. On
the Windows computers used for our exercises you can start PyCharm from
`Start -> All Programs -> JetBrains -> PyCharm`.

Note that double-clicking on a `.py` file will probably open a different IDE
(namely IDLE) by default, which can also be used, but is not as good. In that
case, you have to set the default application for opening files with .py
extension to PyCharm.

When you start PyCharm for the first time, you have to tell it which
version of Python to use. `Configure -> Preferences -> Project interpreter -> Python interpreters ` will show a window where you can click the `+` at the top right to select a Python version. **Be sure to select a version of Python 3 (such as 3.4 or 3.5).**

When PyCharm is started for the first time, it will open without a
project. If you already have a folder with the relevant files for a
project, you can use `File -> Open Directory...` to make PyCharm use that
as a project: after loading you will see all files in the folder listed
on the left side.

If you don't already have a project-folder, you can get PyCharm to make
(an empty) one within the PycharmProjects folder with the menu option
`File -> New Project...`. You can then add (empty) `.py` files from within
PyCharm with the menu option `File->New...`, or copy existing `.py` files
to the project-folder from outside PyCharm.

For information on how to run the `.py` files you've written or edited,
see the section [Executing Scripts](#Executing%20Scripts).

At any point, you can open an interactive Python interpreter window with
`Tools -> Run Python Console...`

### Python Basics
---

For this first part, we will use the interactive Python interpreter (see
above).

#### Operators

The Python interpeter can be used to evaluate expressions, for example
simple arithmetic expressions. If you enter such expressions, they will be evaluated and the result wil be
returned on the next line.

```python
>>> 1 + 1
2
>>> 2 * 3
6
```

Boolean operators also exist in Python to manipulate the primitive
`True` and `False` values.

```python
>>> 1==0
False
>>> not (1==0)
True
>>> (2==2) and (2==3)
False 
>>> (2==2) or (2==3)
True
```

#### Strings

Like Java, Python has a built in string type. The `+` operator
is overloaded to do string concatenation on string values.

```python
>>> 'artificial' + 'intelligence'
'artificialintelligence'
```

There are many built-in methods which allow you to manipulate strings.

```python
>>> 'artificial'.upper()
'ARTIFICIAL'
>>> 'AI'.lower()
'ai'
>>> len('three')
4
```

Notice that we can use either single quotes `' '` or double
quotes `" "`{.western} to surround string. This allows for using quotes
within strings:

```python
>>> print( "It's a mad world")
It's a mad world
```

We can also store expressions into variables.

```python
>>> s = 'hello world'
>>> s
'hello world'
>>> print(s)
hello world
>>> s.upper()
'HELLO WORLD'
>>> num = len(s.upper())
>>> num
11
>>> num = num + 2.5
>>> print(num)
13.5
```

In Python, you do not have to declare variables before you assign to
them, as in Java and C++.

**Exercise 1:** Start by typing the following commands into the command line.

```python
>>> r = 'robots'
>>> s = ' '
>>> t = 'rule'
```

Then use only string manipulations on `r`, `s` and `t` to create a new variable `u` which contains the string `robots RULE`. Print this `u` and then print the length of `u`.

#### `dir` and `help`

To see what methods Python provides for a datatype, use the
`dir` and `help` commands:

```python
>>> s = 'abc'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__','__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__','__repr__', '__rmod__', '__rmul__', '__setattr__', '__str__', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'replace', 'rfind','rindex', 'rjust', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(s.find)
Help on built-in function find:
    
find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within s[start,end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

>>> s.find('b')
1
```

Note that another great resource on information about methods
and datatypes is [the officual Python documentation](https://docs.python.org/3.4/).
Often if you use Google to find information about something, you will end up there.
For example, take a look at [the built-in functions that exist in Python](https://docs.python.org/3.4/library/functions.html).

**Exercise 2:** Try out some of the string functions listed in `dir` (ignore
those with underscores around the `__method-name__`, they are internal
private helper functions). Then, try to see if you can find what method name to put
in place of `???` so that the below code returns `True` in the interpreter.

```python
>>> s = 'hair'
>>> s.title().???() == 'hAIR'
True
```

#### Built-in Data Structures

Python comes equipped with some useful built-in data structures, broadly
similar to Java's collections package.

---

**Lists** store a sequence of mutable items with indices starting at 0:

```python
>>> fruits = ['apple','orange','pear','banana']
>>> fruits[0]
'apple'
```

We can use the `+` operator to do list concatenation:

```python
>>> otherFruits = ['kiwi','strawberry']
>>> fruits + otherFruits
['apple', 'orange', 'pear', 'banana', 'kiwi', 'strawberry']
```

Python also allows negative-indexing from the back of the list. For instance,
`fruits[-1]` will access the last element, `'banana'`.

```python
>>> fruits[-2]
'pear'
>>> fruits.pop()
'banana'
>>> fruits
['apple', 'orange', 'pear']
>>> fruits.append('grapefruit')
>>> fruits
['apple', 'orange', 'pear', 'grapefruit']
>>> fruits[-1] = 'pineapple'
>>> fruits
['apple', 'orange', 'pear', 'pineapple']
```

We can also index multiple adjacent elements using the slice operator.
For instance `fruits[1:3]` will return a list containing the
elements at position 1 and 2. In general `fruits[start:stop]`
will get the elements with indices `start, start+1, ..., stop-1`. We can
also do `fruits[start:]` which returns all elements starting
from the `start` index, and `fruits[:end]` will
return all elements before the element at position `end`.

```py
>>> fruits[0:2]
['apple', 'orange']
>>> fruits[:3]
['apple', 'orange', 'pear']
>>> fruits[2:]
['pear', 'pineapple']
```

The items stored in lists can be any Python data type. So for instance we
can have lists of lists.

```py
>>> lstOfLsts = [['a', 'b', 'c'], [1, 2, 3], ['one', 'two', 'three']]
>>> lstOfLsts[1][2]
3
>>> lstOfLsts[0].pop()
'c'
>>> lstOfLsts
[['a', 'b'], [1, 2, 3], ['one', 'two', 'three']]
```

**Exercise 3:** Start by typing the following commands into the command line.

```py
>>> lst = ['Vader', 'Luke', 'Leia', 'Han', 'R2-D2',  'ChewBacca', 'Obi-Wan']
```

Then use only list manipulations to change the list so that it looks as follows.

```py
>>> lst
['Vader', 'R2-D2', 'Obi-Wan', 'Luke', 'Leia', 'Han', 'ChewBacca']
```

Tip: look at the first letter of each string. Remember that you can find the
methods you can call on an object using `dir` and get
information about them using `help`.

---

A data structure similar to the list is the **tuple**, which is like a
list except that it is immutable (i.e. once it is created, you cannot
change its content anymore). Note that tuples are surrounded with
parentheses while lists have square brackets.

```py
>>> pair = (3,5)
>>> pair[0]
3
>>> x,y = pair
>>> x
3
>>> y
5
>>> pair[1] = 6
TypeError: 'tuple' object does not support item assignment
```

The attempt to modify an immutable structure raised an exception. Exceptions
indicate errors. 'Index out of bounds', 'type error' , and so on, will
all report exceptions in this way.

---

A **set** is a data structure that serves as an unordered list with
no duplicate items. Below, we show how to create a set, add things to
the set, test if an item is in the set, and perform common set
operations (difference, intersection, union). We also introduce
the `in` operator below, which can be used to check whether an element
is part of a collection - be it a set, a list or something else.

```py
>>> shapes = ['circle','square','triangle','circle']
>>> setOfShapes = set(shapes)
>>> setOfShapes
set(['circle','square','triangle'])
>>> setOfShapes.add('polygon')
>>> setOfShapes
set(['circle','square','triangle','polygon'])
>>> 'circle' in setOfShapes
True
>>> 'rhombus' in setOfShapes
False
>>> setOfFavoriteShapes = set(['circle','triangle','hexagon'])
>>> setOfShapes - setOfFavoriteShapes # difference
set(['square','polygon'])
>>> setOfShapes & setOfFavoriteShapes # intersection
set(['circle','triangle'])
>>> setOfShapes | setOfFavoriteShapes # union
set(['circle','square','triangle','polygon','hexagon'])
```

Note that the objects in a set are unordered; you cannot assume that their
traversal or print order will be the same across machines or program executions.
This also means that sets cannot be indexed in the usual manner (e.g. `setOfShapes[0]`
results in an error), but they can only be iterated over. More on this later.

---

The last built-in data structure we will discuss is the **dictionary** which stores a map
from one type of object (the `key`) to another (the `value`). Here 'map' does not mean a
geographical map, but instead a one-to-one relation between the key and value.This means
that a dictionary is basically a list that can use other types of indices besides integers.
The key (index) must be an immutable type (string, number, or tuple).
The value can be any Python data type. Note that as with sets, maps are unordered.
As with nested lists, you can also create dictionaries of dictionaries.

```py
>>> studentIds = {'knuth': 42.0, 'turing': 56.0, 'nash': 92.0 }
>>> studentIds['turing']
56.0
>>> studentIds['nash'] = 'ninety-two'
>> studentIds
{'knuth': 42.0, 'turing': 56.0, 'nash': 'ninety-two'}
>>> del studentIds['knuth'] # delete
>>> studentIds
{'turing': 56.0, 'nash': 'ninety-two'}
>>> studentIds['knuth'] = [42.0,'forty-two']
>>> studentIds
{'knuth': [42.0, 'forty-two'], 'turing': 56.0, 'nash': 'ninety-two'}
>>> studentIds.keys()
dict_keys(['knuth', 'turing', 'nash'])
>>> studentIds.values()
dict_values([[42.0, 'forty-two'], 56.0, 'ninety-two'])
>>> studentIds.items()
dict_items([('knuth',[42.0, 'forty-two']), ('turing',56.0), ('nash','ninety-two')])
>>> len(studentIds)
3
```

**Exercise 4:** Start by typing the following commands into the command line.

```py
>>> parents = {'Catelyn': 'female', 'Eddard': 'male'}
>>> children = {'Robb': 'male', 'Sansa': 'female', 'Arya': 'female', 'Bran': 'male'}
```

Then use only dictionary manipulations to create a *new* dictionary `all` from the above that looks as follows.

```py
>>> all
{'Eddard': 'male', 'Arya': 'female', 'Robb': 'male', 'Sansa': 'female', 'Catelyn': 'female', 'Jon': 'male', 'Bran': 'male'}
```

Note the addition of the key `'Jon'`, and note also that the order in which the
entries are displayed may be different for you. Remember that you can find the
methods you can call on an object using `dir` and get
information about them using `help`.

### Executing Scripts
---

In the next section you will learn about writing scripts. 
There are 2 main ways to execute a `.py` file that you have written.

#### Executing .py files from PyCharm

Any `.py` file that is open in the PyCharm editor window can be executed
by selecting the menu option `Run -> Run...` and clicking on the name
of the file (shown without the `.py` bit) that you want to run.

#### Executing `.py` files from the command prompt

You can also invoke Python directly to execute your `.py` file from
outside PyCharm. To do so you need to first start a command prompt.
To execute your `.py` file you then need to change directory to the
directory where your file exists. You do this using the 'cd' command.

So if, for example, your file `example.py` was saved in

`C:\Documents and Settings\user\PycharmProjects\pythonTutorial`

you would first do

`cd C:\Documents and Settings\user\PycharmProjects\pythonTutorial`

Now you can run your `.py` file by typing `python example.py`.

You can also execute your file with command line options by simply
adding them to the above line. For example to add 2 options 'option1' and 'option2' use
`python example.py option1 option2`.

### Writing Scripts
---

Now that you've got a handle on how to use Python interactively and how
to invoke Python on scripts, let's write a simple Python script that
demonstrates Python's `for` loop. Create a file and fill it with the following code.
Run this file (using either the command line or PyCharm) and see what happens.
Try to understand why the script produces the output that you see.

```py
# This is what a comment looks like 
fruits = ['apples','oranges','pears','bananas']
for fruit in fruits:
    print(fruit + ' for sale')

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}
for fruit, price in fruitPrices.items():
    if price < 2.00:
        print('%s cost %f a pound' % (fruit, price))
    else:
        print(fruit + ' are too expensive!')
```

The above code uses `for` to loop directly over a list. You can use `range` to generate a sequence of integers, which is sometimes useful for generating traditional `for` loops.

```py
for index in range(len(lst)):
    print(lst[index])
```
    
Although in most cases you will want to loop directly over the list.

```py
for element in lst:
    print(element)
```

These two pieces of code have exactly the same effect. If you want to have both the index and the element available, there's an easy way to do that, too.

```py
for index, element in enumerate(lst):
    print('element ' + element + ' at index ' + index)
```

Now create a new script file and fill it with the following code. Run it and try to understand the results.
The statements on lines 2 and 4 contain so-called *list-comprehensions*. These create new lists based on existing lists.

```py
nums = [1,2,3,4,5,6]
oddNums = [x for x in nums if x % 2 == 1]
print(oddNums)
oddNumsPlusOne = [x+1 for x in nums if x % 2 ==1]
print(oddNumsPlusOne)
```

**Exercise 5:** Write a new script file in which a list is created containing some strings,
with at least some letters in uppercase. Then a list comprehension is performed which, from that list, generates
a lowercased version of each string that has length greater than five.

#### Beware of Indentation

Unlike many other languages, Python uses the indentation in the source
code for interpretation. So for instance, the following script

```py
if 0 == 1: 
    print('We live in a world of arithmetic pain')
print('Math is not broken, all is well') 
```

will output `Math is not broken, all is well`. But if we had written the script as

```py
if 0 == 1: 
    print('We are in a world of arithmetic pain')
    print('Thank you for playing')
```

there would be no output at all. The moral of the story: be careful how you
indent!

#### Writing Functions

As in most languages, in Python you can define your own functions:

```py
fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75}

def buyFruit(fruit, numPounds):
    if fruit not in fruitPrices:
        print("Sorry we don't have %s" % (fruit))
    else:
        cost = fruitPrices[fruit] * numPounds
        print("That'll be %f please" % (cost))
   
buyFruit('apples',2.4)
buyFruit('coconuts',2)        
```

Save this script as a file and run it. Look at the output and try to understand it.

**Problem 1 (for submission):** Complete the `buyLotsOfFruit(orderList)` function in
`buyLotsOfFruit.py` which takes a list of `(fruit, weightInPounds)` tuples and returns the cost of the given list.
If there is some `fruit` in the list which doesn't appear in
`fruitPrices` it should return `None` (which is like `null` in Java).
Do not change the `fruitPrices` variable.

If you implemented the function correctly the script should output the following. Note that we will also test it for different orderlists.

```
Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25`
```

**Advanced Exercise:** Write a `quickSort` function in
Python using list comprehensions. Use the first element as the pivot.
