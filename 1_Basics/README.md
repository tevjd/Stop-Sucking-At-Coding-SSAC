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

`input` = get the data from the stdint (standard input) = the keyboard in our case. 

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

