# Theory exercises 1
These exercises relate to the first lecture where we showed 2 problems, several algorithms for each problem and several programs for each algorithm.

The problems from the lecture were:

1) Calculate all prime numbers smaller or equal to a given bound

2) Calculate the product of two non negative integers

## Exercises

1) What would you do if asked to say whether a positive integer number is prime or not?

2) Using the first algorithm we showed for deciding whether a number is prime or not (implemente in the function ```is_prime```), how many times is the test ```n % i == 0``` executed

	a) for ```n == 100```

	b) for ```n == 101```

	c) for ```n == 102```

	d  for ```n == 10000000```

3) In the lecture we plainly state that a factor of $n$ cannot be larger than $\lfloor \sqrt{n} \rfloor$. Eplain why this is so. Provide examples supporting your argument.

4) For a prime number ```p```, how many times is the test ```n % i == 0``` executed in the functions ```is_prime(p)``` and ```is_prime_better(p)```?

5) Do a by-hand execution of the recursive algorithm for multiplication, programmed in the function ```rec_mul``` for numbers 123 and 321.

6) Explain why we needed the statement ```if len(m) % 2 == 1: mid+=1``` in this function.

7) Provide the mathematical argument for using only three recursive calls in Karatsuba's algorithm.







