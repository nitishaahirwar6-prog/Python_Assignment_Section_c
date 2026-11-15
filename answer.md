Analysis – Python Assignment

Q1. Compare the for loop and while loop approach used in the programs. Which do you prefer and why?

Answer: A for loop is used when the number of iterations is known. A while loop is used when repetition depends on a condition. I prefer the for loop because it is simple, easy to understand, and requires less code for a fixed number of iterations.

Q2. For the Fibonacci program, compare the loop-based and recursive versions. Which one repeats more work as n grows, and why?

Answer: The recursive Fibonacci method repeats more work because it calculates the same Fibonacci values multiple times. The loop-based method calculates each term only once, so it is more efficient for larger values of n.

Q3. For the prime number check, what is the largest divisor you actually need to test up to, instead of checking all the way up to n minus 1? Explain briefly why this works.

Answer: We only need to check divisors up to the square root of n. If a number has a divisor greater than its square root, it must also have a matching divisor smaller than its square root. Therefore, checking beyond the square root is unnecessary.

Q4. In the Number Guessing Game, what strategy could a user follow to minimize the number of guesses, regardless of the range? Name the strategy.

Answer: The user should use the Binary Search Strategy. In this strategy, the user guesses the middle number of the remaining range and eliminates half of the possible numbers after every guess. This reduces the number of guesses required.