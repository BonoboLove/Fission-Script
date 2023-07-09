# Fission-Script
⚛️ Just a esoteric 🔮 transpiled ⚙️ coding language 💬, its a mixture of Python 🐍 and Javascript 📜. ⚛️
Python is the backbone of coding language meaning that anycode that is representing any other language, will not be executed as correctly. The mixture of Javascript means that there are some commands of Javascript in this coding language. But this does not mean Javascript can be compiled from this coding language.

Files:
  1. code.fss - The coding language's coding environment, this is where you write your Fission Script code
  2. transpile.py - The transpiler that converts the code.fss into Python, the new python code is written to pycode.py
  3. pycode.py - The new transpiled code, its completely made up of Python
  4. error_log.txt - The error log, it logs any errors doing the compilation
All of these files' name can be changed within the starting lines of transpile.py

Commands:
  1. send - "send" is the Python and Javascript equivalent of return
  2. ().len - "(x).len" will return the length of x
     If you add an underscore after the opening parentheses, the compiler will force the length of x to be returned
  3. <> - "x<>'123'" will return the first index of 123 from x
  4. .add - "x.add(1)" is the Python equivalent of append / Javascript equivalent of push
  5.  =  => - "x = a, b => a * b" is the Python equivalent of lambda / Javascript equivalent of arrow function
