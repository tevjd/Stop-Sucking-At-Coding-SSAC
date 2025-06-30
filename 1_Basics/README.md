## Basics

This is the first chapter of this project, here I will try to explain some basics you need if you want to understand how to write Python code. 

### Shebang
A very basic Python file need something called a `shebang`. But what is this strange thing?
A `shebang` looks like this: `#!/usr/bin/env python3`. When ze write code the next step is too execute it. And for that we need to tell to the operating system HOW to execute it. And to do that we need to tell to the OS that our program is a python file and then it need a python interpreter to execute. 

In Python we need something called an `interpreter` and not a `compiler` like in C or C++. Because Python is a programming language where the interpreter reads and executes the code line by line. 

And don't forget to make the file executable if you want to execute it. Do to that you need one of the following command to chnage the permission of execution on your file: 
```
chmod u+x myscript.py #only the owner
chmod ug+x myscript.py #group + owner
chmod a+x myscript.py or chmod +x myscript.py #all
```
### Pylint

If one of your objectif is to write clear and good code you need to have some convention. A good start is to use a tool called `pytlint`. This tool doesn't execute your code but give some advice on what you need to chnage to have good programming convention. 

There is a VS Code extension for Pylint so we can correct our code in real-tiome when ze are coding. 

### Interesting function in Python? 

Here are some functions which can help you when you program something. 

`input()` = get the data from the stdint (standard input) = the keyboard in our case.
`ord()` = take an ASCII char and return the number associated.
`chr()` = take a number and return the ASCII char associated. 

### What is a module? 

A module in python is a way to factorize some piece of code or functions. In python a module is a `.py` file and we can import a module by putting at the top of the program an `import module_name`. 

### Tuple

A tuple is a special data structure in Python, it is like a list that CAN'T be changed. This is an immutable data structure. 
Example of tuple: 
```
coordinates = (3, 4)
colors = ("red", "yellow", "green")
single = (42,)
mixed = (1, "hello", 3.14, True)
```

In tuple the order is important and it allows duplication of the same data. 
When we return multiple elements in a function, the result is a tuple of those elements. 
We can use two methods on tuples: `tuple.count()` and `tuple.index()`. 

### Open and Write in a file

There is different approach to do that. You can use the `open` function like this: 
```
myfile = open()
myfile.close()
```
Note that we need to properly close the file here. If we want to be managed automatically we can use `with`: `with open() as myfile:`. This is safer because in case of an error occuring the with method will automatically close the file properly. 

### F-string ? 

In Python there is different ways to construct a string. But if we want to directly include some variable, integer or others strings a simple solution is to use something called a `f-string` = Formated string. This is a powerful and readable way to format strings in Python (introduced in Python 3.6). 

Example of use: 
```
print(f"Hello, my name is {name} and I'm {age} years old.")
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
```
In the last expression we tell the format some specific rules. The `.` = decimal point indicator and the `2` means we want to show exaclty 2 digits after the decimal point. The `f` means we want to use the format as a floating-point = decimal number. 

### SVG = Scalable Vector Graphics

This is a web standard for creating graphics using code. It's useful for logos, icons, simple illustrations and interactive graphics. It is using mathematical descriptions of shapes and so it scales perfectly at any size. 

### I have a bug...

When you will start program more and more complex projects, you will have something called bugs. A bug is simply when your program is doing something that you didn't expected. For example, a behavior or a variable that is not what you expected when you program it. Sometimes bugs are easy to correct, we call this a fix. But sometimes the story isn't the same. 

Hopefully there is a very nice tool called a `debugger`. This kind of program helps you execute your code step by step and understand what is going on by displaying your variable content or more. A simple debugger in python is `pdb`, here is a link to the documentation: https://docs.python.org/3/library/pdb.html. And you can use it like that: 

```
python3 -m pdb file.py
In that case -m dpb tell to the interpreter to find the module named pdb and use it like a script. In that case file.py is an argument for the debugger. 
```
