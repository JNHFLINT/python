
# Recursion: Breaking down big problems into smaller, sub problems

# Fibonacci sequence: Previous two numbers add up to next number
# The sequence is defined as follows: F_n = F(n - 1) + F(n - 2)

# First two numbers will always be 0 and 1 so we will need to cover them as base cases

# Let's say n = 3:
# F_3 = F(3 - 1) + F(3 - 2) = F_2 + F_1 = 2


def fibonnaci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)
    
example = fibonnaci(6)
print(f'Fibonacci result of entering 6 is: {example}')