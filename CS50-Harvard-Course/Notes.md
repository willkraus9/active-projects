# Harvard CS50 - Full Computer Science University Course (up to Python)
## Link: https://www.youtube.com/watch?v=8mAITcNt710&list=LL&index=58
## Coding sandbox: https://sandbox.cs50.io/a8e20238-ad4c-4250-9e24-ce50a1f4d0cd? (easier than downloading library)
### Lecture 0: Intro / Scratch
 * action verbs = **Functions**
 * answer some question / fork = **Conditionals**
     * part which is being answered (true / false)= **Boolean Expresssions**
 * directive to do something over and over again = **Loops**
 * doing an action and putting out a result = **Algorithm**
    * Algorithms should be named what they do! 
    * For implementation across programs, abstract parameters for adaptability
    * stuff to put into algorithm = **Argument / Parameter / Input**
    * stuff take out of algorithm = **Return Values / Outputs**
* **NB:** *Evaluation (does it do the thing) + critique of code (how well is thing done) is good for reviewing!*

### Lecture 1: C 
* By the end of lec: write "correct" code (does thing + good design)
* **IDE** = Integrated Developer Environment (used to write code)
* **Compiler** = convert one language to another (human-facing code --> machine code)
* **Terminal** = see what computer interaction sees; runs commands on computer in command line interface 
* To run code: run in command line
    * "make _name of program in c_"
        * (now there is a file that is called that on computer)
        * (go into current folder) (run) _name of program_ --> ./_name of program_
* **GUI** = 'gooey' = Graphical User Interface
* Command Line Interface: Linux
    * rm = remove files
    * ls = list all files in folder
* **NB:** *have to compile each time when make changes!*
* in C: have functions, arguments
    * functions: _word_
    * arguments: add double quotes (for **string** of words)
        * also have to end with semicolon
    * Return values - get value use and reuse
        * in C: ans = get_string() (receives string in response to be assigned to "ans" function)
            * also have to tell what kind of variable the function will be stored as
    * All together: string answer = get_string("What is your name?");
* **Float** = regular number
    string answer = get_string("What's Your Name?");
    printf("Hi there, %s!",answer);
* so to make the files, you have to open bash in the terminal (have the $ instead of PC) for stuff to work?
* All three syntax structures are the same: 
    * int counter = counter + 1;
    * int counter += 1;
    * int counter++;
* **const** = add before int to make unchangeable; capitalize variable name!
* **NB:** *if you find youself copying and pasting, you are probably doing something inefficient!*
* || = or, && = and
* single quotes = single char; double quotes = string
* **while loops**: while(true)
    * **do while**: do a task, then see if actually possible.
* **for loops**: for (int i = 0; condition; if so, do something else)
    * for (int i=0; i<=3; i++)
* create function: void name (input) 
* **NB**: *read top to bottom (get functions different orders by void at top, then explain later at bottom)*
* **Break** = completely shut down code (can use to end loops) 
### Lecture 2: Arrays 
* clang = compile, -o = output, rm = remove
* how to debug: use printf (print the values of variables)
    * printf("variable is __") in a loop 
    * could also use debug50 (commad from the get go)
        * mention already compiled code, walk through code step by step
            * pause execution at human pace
* one recommended debugging technique: talk out loud about code
    * "rubber duck debugging - talking through code - I said something stupid
* **NB**: *As long as one variable in an arithmetic expression is a float (or something with more storage), all other variables will be too!* 
* **Array** = matrix used to store multiple variables of the same storage type (char, string, etc.) together as one variable (eliminate extra variable names)
    * int scores[3]; (array of size three, 3 = index)
    * scores[0] = x, scores[1] = y (have to start at 0!)
* strings are just arrays of characters - s[1] s[2] s[3]
    * separate different strings = null character (8 0s, \0)
* manual pages = helpful functions (might be complex)
### Lecture 3: Algorithms 
### Lecture 4: Memory 
### Lecture 5: Data Structures


