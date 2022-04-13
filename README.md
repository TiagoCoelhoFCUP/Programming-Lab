# Programming-Lab
Projects developed under the Programming Lab college chair during the 2017/2018 school year

## Arithmetic Expression Interpreter with Variable Definition

Python implementation of an interpreter of an arithmetic expression language with variable definitions.
Arithmetic expressions must be in prefix notation (e.g. (* 2 6) or (+ 5 x), and variables must be defined by assignments of the form (define x 5). The interpreter argument is a string of expressions. 

To handle variables we used a table that associates variables with their value. This table is updated by define statements and is used to evaluate variables. It is maintained as a global variable and implemented as a list of (variable, value) pairs.

The interpreter's inner workings are mainly divided in three distinct functions:
<ul>
  <li> Tokenize, which splits the initial string into a list of words </li>
  <li> Parse, which takes as argument a list of words (tokens) and return a list of tuples that represent each expression </li>
  <li> Avalia, which takes as argument the list of tuples returned by the parser and returns the result of the evaluation of the expressions </li>
</ul>

For the expr = “(define x 5) ( + (* 2 x) 7)” 

```
tokenize(expr) = [´(´, ´define´, ´x´, ´5´, ´)´ , ´(´, ´+´ , ´(´, ´*´ , ´2´, ´x´, ´)´ , ´7´, ´)´ ]
parse(tokenize(expr) = [ ( ´define´, ´x´, 5 ) , ( ´+´ , ( ´*´, 2 , ´x´) , 7 ) ]
avalia(parse(tokenize(expr) = 17
```

