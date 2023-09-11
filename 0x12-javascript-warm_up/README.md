<h1>0x12-javascript-warm_up</h1>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg" alt="javascript Image">

<h1>Resources</h1>
<b>Read or watch:</b>

<li><a href="https://intranet.alxswe.com/rltoken/3HLjEesLsmyWfRUWnxgUGg">Writing JavaScript Code</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/zgOWmcpVLZFEmFlmuwayyg">Variables</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/VPd6JWaLrwOBzjAeXNAEqg">Data Types</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/3HLjEesLsmyWfRUWnxgUGg">Operators</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/PHtcJJk30gBNmlFQ9R4RVg">Operator Precedence</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/tsreKcNh_KmTmLPHsfvJRw">Controlling Program Flow</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/e3EfHIxICdIncGBwwIDbXQ">Functions</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g">Objects and Arrays</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g">Intrinsic Objects</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/g-MgvO09Ur02RhM63gVyXw">Module patterns</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/gJi61GeJTRX0g-M0Rx-0Iw">var, let and const</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/Y8hkOcy5jO22lQGyF6_NiA">JavaScript Tutorial</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/NZawtiBjWUpiojnrtVywNw">Modern JS</a></li>

<h1>Objectives:</h1>
<p>
You need to know the following concepts:
</p>
<li>Why JavaScript programming is amazing</li>
<li>How to run a JavaScript script</li>
<li>How to create variables and constants</li>
<li>What are differences between var, const and let</li>
<li>What are all the data types available in JavaScript</li>
<li>How to use the if, if ... else statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use while and for loops</li>
<li>How to use break and continue statements</li>
<li>What is a function and how do you use functions</li>
<li>What does a function that does not use any return statement return</li>
<li>Scope of variables</li>
<li>What are the arithmetic operators and how to use them</li>
<li>How to manipulate dictionary</li>
<li>How to import a file</li>

<h1>Tasks</h1>

<h2>0. First constant, first print</h2>
mandatory
<p>Write a script that prints “JavaScript is amazing”:</p>

<li>You must create a constant variable called myVar with the value “JavaScript is amazing”</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<pre>
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 0-javascript_is_amazing.js</li>
  
<h2>1. 3 languages</h2>
mandatory
<p>Write a script that prints 3 lines:</p>

<li>The first line: “C is fun”</li>
<li>The second line: “Python is cool”</li>
<li>The third line: “JavaScript is amazing”</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<pre>
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 1-multi_languages.js</li>
  
<h2>2. Arguments</h2>
mandatory
<p>
Write a script that prints a message depending of the number of arguments passed:
</p>
<li>If no arguments are passed to the script, print “No argument”</li>
<li>If only one argument is passed to the script, print “Argument found”</li>
<li>Otherwise, print “Arguments found”</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>Reference: process.argv</li>
<pre>
guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 2-arguments.js</li>
  
<h2>3. Value of my argument</h2>
mandatory
<p>Write a script that prints the first argument passed to it:
</p>
<li>If no arguments are passed to the script, print “No argument”</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>You are not allowed to use length</li>
<pre>
guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 3-value_argument.js</li>
  
<h2>4. Create a sentence</h2>
mandatory
<p>Write a script that prints two arguments passed to it, in the following format: “ is ”
</p>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<pre>
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 4-concat.js</li>
  
<H2>5. An Integer</H2>
mandatory
<P>
Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
</P>
<li>If the argument can’t be converted to an integer, print “Not a number”</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>You are not allowed to use try/catch</li>
<pre>
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 5-to_integer.js</li>
  
<h2>6. Loop to languages</h2>
mandatory
<p>Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
</p>
<li>The first line: “C is fun”</li>
<li>The second line: “Python is cool”</li>
<li>The third line: “JavaScript is amazing”</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>You are not allowed to use any if/else statement</li>
<li>You can use only one console.log</li>
<li>You must use a loop (while, for, etc.)</li>
<pre>
guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 6-multi_languages_loop.js</li>
  
<h2>7. I love C</h2>
mandatory
<p>Write a script that prints x times “C is fun”
</p>
<li>Where x is the first argument of the script</li>
<li>If the first argument can’t be converted to an integer, print “Missing number of occurrences”</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>You can use only two console.log</li>
<li>You must use a loop (while, for, etc.)</li>
<pre>
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 7-multi_c.js</li>
  
<h2>8. Square</h2>
mandatory
<p>Write a script that prints a square
</p>
<li>The first argument is the size of the square</li>
<li>If the first argument can’t be converted to an integer, print “Missing size”</li>
<li>You must use the character X to print the square</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>You must use a loop (while, for, etc.)</li>
<pre>
guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js School
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 8-square.js</li>
  
<h2>9. Add</h2>
mandatory
<p>Write a script that prints the addition of 2 integers
</p>
<li>The first argument is the first integer</li>
<li>The second argument is the second integer</li>
<li>You have to define a function with this prototype: function add(a, b)</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<pre>
guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 9-add.js</li>
  
<h3>10. Factorial</h3>
mandatory
<p>Write a script that computes and prints a factorial
</p>
<li>The first argument is integer (argument can be cast as integer) used for computing the factorial
<li>Factorial of NaN is 1</li>
<li>You must do it recursively</li>
<li>You must use a function</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<pre>
guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 10-factorial.js</li>
  
<h2>11. Second biggest!</h2>
mandatory
<p>Write a script that searches the second biggest integer in the list of arguments.
</p>
<li>You can assume all arguments can be converted to integer</li>
<li>If no argument passed, print 0</li>
<li>If the number of arguments is 1, print 0</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<pre>
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 11-second_biggest.js</li>
  
<h2>12. Object</h2>
mandatory
<p>Update this script to replace the value 12 with 89:
You are not allowed to use var
</p>
<pre>
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 12-object.js</li>
  
<h2>13. Add file</h2>
mandatory
<p>Write a function that returns the addition of 2 integers.
</p>
<li>The function must be visible from outside
<li>The name of the function must be add
<li>You are not allowed to use var
<em>Tip</em>
<pre>

guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 13-add.js</li>

<h2>14. Const or not const</h2>
<em>#advanced</em>
<p>Write a file that modifies the value of myVar to 333</p>
<pre>
guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myvar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$ 
</pre>
<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4ae30fb44f708dbb3abc211b784db614e615ca21.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230911%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230911T082745Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e903afbd29f8019670e451514fa892ed96092655722753661efe3a51a90c98b3">

Hint: Scope

This exercise doesn’t pass semistandard so don’t worry about it.

<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 100-let_me_const.js</li>
  
<h2>15. Call me Moby</h2>
<em>#advanced</em>
<p>Write a function that executes x times a function.
</p>
<li>The function must be visible from outside</li>
<li>Prototype: function (x, theFunction)</li>
<li>You are not allowed to use var</li>
<pre>
guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 101-call_me_moby.js</li>
  
<h2>16. Add me maybe</h2>
<em>#advanced</em>
<p>Write a function that increments and calls a function.
</p>
<li>The function must be visible from outside</li>
<li>Prototype: function (number, theFunction)</li>
<li>You are not allowed to use var</li>
<pre>
guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 102-add_me_maybe.js</li>
  
<h2>17. Increment object</h2>
<em>#advanced</em>
<p>Update this script by adding a new function incr that increments the integer value.

You are not allowed to use var
</p>
<pre>
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$ 
</pre>
<h3>Repo:</h3>

<li>GitHub repository: alx-higher_level_programming</li>
<li>Directory: 0x12-javascript-warm_up</li>
<li>File: 103-object_fct.js</li>
  
