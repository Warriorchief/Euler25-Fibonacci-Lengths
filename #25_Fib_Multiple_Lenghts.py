"""
Euler Project 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def assemble_fib(x):
    fib=[0,1,1];
    i=3;
    while i<x:
        if len(str(fib[i-1]+fib[i-2]))>999:
          print("Found it! Term # ",i,"has length 1000 and is the number ",fib[i-1]+fib[i-2]);
          return
        else:
            fib.append(fib[i-1]+fib[i-2]);
            i+=1;

assemble_fib(10000); #--> Found it! Term #  4782 has length 1000 and is the number ... CORRECT