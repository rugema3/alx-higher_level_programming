<h1>0x00. Python - Hello, World</h1>

<h1>Resources</h1>
<b>Read or watch:</b>
<ul>
<li><a href='https://intranet.alxswe.com/rltoken/JsFCs_NBzMAR7-XPAZ9BoA'>The Python tutorial (only the first three chapters below)</a></li>
<li><a href='https://intranet.alxswe.com/rltoken/kifRlLG2iMX5AZiW8lrCMg'>Whetting Your Appetite</a>
<li><a href='https://intranet.alxswe.com/rltoken/RVpfAuagCo9SdfYeoHd6jg'>Using the Python Interpreter</a></li>
<li><a href='https://intranet.alxswe.com/rltoken/kifRlLG2iMX5AZiW8lrCMg'>An Informal Introduction to Python (Read up until “3.1.2. Strings” included)</a></li>
<li><a href='https://intranet.alxswe.com/rltoken/Ju0J8BxkuPX5yKZctyKfsQ'> How To Use String Formatters in Python 3</a></li>
<li><a href='https://intranet.alxswe.com/rltoken/szBsJ-Qyig_RrImN7RGlOg'>Learn to Program</a></li>
<li><a href='https://intranet.alxswe.com/rltoken/tgYt-0zVy1T4sDlE9ohxnA'>Pycodestyle – Style Guide for Python Code</a></li>
</ul>

<h1>Requirements</h1>
<h2>Python Scripts</h2>
<ul>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly #!/usr/bin/python3</li>
<li>A README.md file at the root of the repo, containing a description of the repository</li>
<li>A README.md file, at the root of the folder of this project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.8.*) </li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using wc</li>

</ul>

<h2>Shell Scripts</h2>

<ul>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
<li>All your scripts should be exactly two lines long (wc -l file should print 2)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly #!/bin/bash</li>
<li>All your files must be executable</li>
</ul>


<h1>Tasks</h1>
<pre>
0. Run Python file
mandatory
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 0-run

1. Run inline
mandatory
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 1-run_inline

2. Hello, print
mandatory
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 2-print.py

3. Print integer
mandatory
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code here
The output of the script should be:
the number, followed by Battery street,
followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long
You have to use f-strings tips

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 3-print_number.py

4. Print float
mandatory
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code here
The output of the program should be:
Float:, followed by the float with only 2 digits
followed by a new line
You are not allowed to cast number to string
You have to use f-strings

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 4-print_float.py

5. Print string
mandatory
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

You can find the source code here
The output of the program should be:
3 times the value of str
followed by a new line
followed by the 9 first characters of str
followed by a new line
You are not allowed to use any loops or conditional statement
Your program should be maximum 5 lines long

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 5-print_string.py

6. Play with strings
mandatory
Complete this source code to print Welcome to Holberton School!

You can find the source code here
You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code
Your program should be exactly 5 lines long


Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 6-concat.py

7. Copy - Cut - Paste
mandatory
Complete this source code

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 7-edges.py

8. Create a new sentence
mandatory
Complete this source code to print object-oriented programming with Python, followed by a new line.

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 8-concat_edges.py

9. Easter Egg
mandatory
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)


Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 9-easter_egg.py

10. Linked list cycle
mandatory
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

Prototype: int check_cycle(listint_t *list);
Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:

Only these functions are allowed: write, printf, putchar, puts, malloc, free

Solving a problem is already a big win! but finding the best and optimal way to solve it, it’s way better! Think about the most optimal / fastest way to do it.

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 10-check_cycle.c, lists.h

11. Hello, write
#advanced
Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

Use the function write from the sys module
You are not allowed to use print
Your script should print to stderr
Your script should exit with the status code 1

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 100-write.py

12. Compile
#advanced
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)



Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 101-compile

13. ByteCode -> Python #1
#advanced
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

Tip: Python bytecode
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 102-magic_calculation.py

</pre>
