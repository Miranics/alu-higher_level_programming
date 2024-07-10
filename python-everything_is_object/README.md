#!/usr/bin/python3
Python Objects and Variables Exploration
Background Context
This project dives deep into understanding how Python works with different types of objects, emphasizing the nuances between mutable and immutable objects. It challenges the traditional approach of simply testing code in the interpreter by encouraging thoughtful analysis and peer collaboration before verification.

Have you ever inadvertently modified a variable? Consider these scenarios:

python
Copy code
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
And what about this:

python
Copy code
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
This project's uniqueness lies in its approach: it starts with questions about Python's specifics, prompting participants to read documentation thoroughly, contemplate deeply, and brainstorm with peers before resorting to code execution.

Resources
9.10. Objects and values
9.11. Aliasing
Immutable vs mutable types
Mutation (Only this chapter)
9.12. Cloning lists
Python tuples: immutable but potentially changing
Learning Objectives
By the end of this project, you will be able to explain to anyone, without relying on Google:

General
Why Python programming is awesome
What is an object
What is the difference between a class and an object or instance
What is the difference between immutable object and mutable object
What is a reference
What is an assignment
What is an alias
How to know if two variables are identical
How to know if two variables are linked to the same object
How to display the variable identifier (which is the memory address in the CPython implementation)
What is mutable and immutable
What are the built-in mutable types
What are the built-in immutable types
How does Python pass variables to functions
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
Your code should use the pycodestyle (version 2.7.*)
All your files must be executable
.txt Answer Files
Only one line
No Shebang
All your files should end with a new line

