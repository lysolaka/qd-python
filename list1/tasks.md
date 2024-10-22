# List 1

## Guessing game
Write a function `guess_number()` that takes a user guess and compares it with a randomly generated number between 1 and 9. If the guess is incorrect, it returns `False`, and if correct, it returns `True` with a message `"Well guessed!"`.

## If the number is even or odd
(Really that's all, you don't get it? - it's your problem)

Write a program which will print `True` if the number is even and print `False` otherwise.

## Christmas tree
Write a program that displays a tree of a height specified by the user, made of stars using for and/or while loops. The tree should look similar to this:
```
    *
   ***
  *****
 *******
*********
```

## Reverse string
Write a program that takes input from the user and reverses it (prints backwards). It also should detect and reverse any digits given in the input like so: 0 → 9, 1 → 8, etc.

Examples:

book1 → 8koob

20lamp → pmal97

## Number checker
Write a program that takes a number as an input from the user (you should check of the input is a valid natural number) and in separate functions checks:
1. If the number is even or odd 
2. If the number is prime 
3. Solves a quadratic equation `2 * x^2 - 5 * (input) * x + 100` using discriminant (Δ). It also should consider the imaginary solutions case. The solution might be exact or approximate. (hint: use `cmath` library)

The output should look as follows:
Even: Odd, Prime: No, Quadratic Solutions: (50, 0)
or
Invalid Input: Not a natural number

## Division
Write a program which accepts a sequence of comma separated binary numbers as its input and inside a function prints the numbers that are divisible by 5 in a comma separated sequence. 

Sample Data : 01001, 00111111, 100010101010, 10011101, 1010101010, 1001, 000000, 11111111 

Expected Output : 000000, 11111111 

In case the number is not a binary number, print:

Invalid Input: Not a valid binary number

## Scrabble score calculator
Write a Scrabble ([rules](https://www.scrabblepages.com/scrabble/rules/), [tutorial](https://youtu.be/K1KgvZwwJqo?si=iqaB_ucICbjqUIFt)) game score calculator, a function that calculates score for a given word, taking into account also double and triple word score. Make sure, it accepts both lowercase as well as uppercase letters. 
