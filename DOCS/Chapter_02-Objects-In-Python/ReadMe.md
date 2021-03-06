# Chapter 02 | Objects in Python #

## Hello World Python Classes ##

````python
class MyFirstClass:
    pass

# initiate the class
a = MyFirstClass()
b = MyFirstClass()
````

* The above is a most basic class in python.
* `class` : keyword defines the start of class.
* Class names follows a conventions in Python.
    - Class name should comprise of number, letters or underscore.
    - Class name should use CamelCase naming convention.
    - The first letter of a class name should be capital, as when creating object we can differentiate between a function call or Object initialization.
* Object Creation:-
    - We can create the objects of a new class as shown in the code above.
    - The only difference in creating object and calling function is that, creating function has the first character as capitalized.
* `python -i hello.py` : runs the code, and then enters into python shell loading the class.

### Attributes ###
* Attribute in Python classes can be set even outside class definition.
* Attribute added in 1 object does not automatically adds it into the other object.

````python
class Point:
    pass


p1 = Point()
p2 = Point()

# Adding x,y attribute to Point P1
p1.x = 5
p1.y = 4

# Adding x,y attribute to Point P1
p2.x = 3
p2.y = 6

print(p1.x, " ", p1.y)
print(p2.x, " ", p2.y)

````
* As shown above example, when we add `p1.x` and `p1.y`, adds `x` and `y` attribute to th `Point` Class.
* This `x` and `y` is not accessible in the other object called `p2`, we have to individually add these attribute to that object.
* We use the syntax `<object>.<attribute> = <value>` to assign values to an attribute of an object.

### Methods ###
* There is no point in writing Object if we cannot show the interaction between them. The interaction between them is possible using methods.

```python
class Point:
    # Move method
    def move(self, x, y):
        self.x = x
        self.y = y

    # self is a manditory name.
    def reset(self):
        self.move(0, 0)

    # Calculate distance
    def calculate_distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))

p1 = Point()
p1.reset()
point2.move(5, 0)
```

* A **method** is just a function inside class. 
* Every method have a mandatory method called `self` as an arguments. This name `self` is by convention.
* The `self` is just a reference to the object used to invoke the method.
* The `self` is not passed while calling the method, as shown by `p1.reset()`, it is implicitly passed by the interpretor.
* `Point.reset(p1)` is another alternate way of calling the method.
* Python interpreter gives an error `TypeError` if we do not use `self` as an arguments.
* We can pass multiple argument to a function shown below, 
    - `def move(self, x, y)`
* Calling the above `move` function is very similar `point2.move(5, 0)`, `self` is not passed explicitly

### Object Initialization ###
* If we access an attribute of a class before it is initialized we get a `AttributeError`.
* Python also a concept of `constructor` and an `initializer`, in-place of just a `constructor`.
* The Python `initializer` is called `__init__`, the `__` before and after the name signifies this is a special function used by Python interpreter.
* We should never name our methods with `__`, which is called dunder.


```python

class Point:
    # passing default aguments to we never have empty point attributes.
    def __init__(self, x = 0, y = 0):
        self.move(x, y)

    # Move method
    def move(self, x, y):
        self.x = x
        self.y = y
```

* The above code initialize all the attributes of class `point`. 
* We can also pass default argument to the `__init__` function, making sure that the object always have initialized attributes.
    - `x = 0, y = 0`, passed as argument above is a default value, if no value is passed with initializing the object.
* The constructor is called `__new__`, and not `__init__`,  
    - it accepts only 1 argument, the class which is being created,
    -  and returns the newly created object.

### DocString ###
* Documentation is a the most important function of a programmer's life.
* Python supports through `docstrings`. There are 3 ways to document the code using `docstring`
    - `' '` : single quotes, for single line docstring having which finishes in 1 line, can have `""` in the string.
    - `" "` : double quotes, for single line docstring having `''` as part of the string.
    - `""" """` : triple quotes, this is used for multi line doc string.
* We can see the docstring of a class, method by using the `help()` in-built function.


## Modules and packages ##
* Each Python class is a module. This concept of module's helps in working with multiple class in a projects.
* `import` is used to access the functionality of different python class. 
* Consider we have these files and following classes in file.
    - `database.py` has class **Database**, and **Query**.
    - `products.py` is using the above classes.
* There are 3 different way to import python modules.

```python
import database
db = database.Database()
```

* The above code imports the database modules, and then use the dot notation for accessing class in the module.
* Every time we have to use any class inside the database file, we have give the full dot notation.
    - `<module>.<class>`


```python
from database import Database
db = Database()
```

* We can use the above syntax to just import the Class directly.
* The above syntax can cause issues if we have same class name like `Database` in the importing file.
* We can also use the above syntax to import multiple classes.
    - `from database import Database, Query`


```python
from database import Database as DB
db = DB()
```

* To solve the issues mentioned in the above code snippet, we can import a class and provide it a name.
* This should never be done.
    - `from database import *`
        + The above code is very inefficient.
        + The above code bring each and every class, variable, function inside the present class without any indication from where it came.
        + IDE gets confused while doing code completion based on the above.
        + The `*` syntax will also bring some of the imported class also to the current name space.

### Packages ###
* We can put multiple python files in a separate folder and call it a **package**.
* The package name is the name of the folder.
* presence of a special file called `__init__.py` creates a packages.
* We can understand relative and absolute imports based on this folder structure.

![Tree of the module](img/tree_module.png "Tree of the module")


* Based on the above folder action, all the below code happen in `main.py`, and we run the `main.py`
* We can import by using the absolute dot notation.
    - `import ecommerce.products`
* Within the modules, we can use relative imports.
    - `from .database import Database` for importing database inside the modules.
    - `.` : one dot to go back 1 folder.
    - `..` : two dot to go back 2 folder.
* When we import any module, and code not inside function are invoked immediately.
    - This may cause delay in start-up of application.
    - All the code in the python packages should be inside function.
* We can use this code to separate if the code is executed manually of through imports.
    - `if __name__ == "__main__":` when the module is invoke manually the name is `__main__`
    - if imported it is the module name.
* We can also define classes inside function.


## Data Access ##
* Most of the OOP language have a concept of data abstraction. Some attribute and methods are not accessible from other object.
    - These are either marked private or protected.
* Python do not have such strict data abstraction, its abstraction is more based on convention than enforced.
* We can start an attribute or a method with a `_`, by convention this should not accessed directly.
    - We can access these variables directly from outside the class.
* We can also start an attribute or a method name with a `__`, this cannot be accessed from outside the object.
    - we can still access it by using this `<object_name>._<class_name><__variablename>`
    - There is no explicit data hiding.


## References ##
1. [Python Modules and Packages - An Introduction ](https://realpython.com/python-modules-packages/)
2. [Corey Schafer | Python OOP Tutorials - Working with Classes ](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
3. [SentDex | Intermediate Python Programming ](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_)
4. [ImportError: attempted relative import with no known parent package](https://napuzba.com/a/import-error-relative-no-parent)
