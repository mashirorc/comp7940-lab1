def main():    
    print("Hello, World!")
    l = [52633, 8137, 1024, 999]
    find_factors_list(l)
    
def find_factors(x):
    factors = []
    # Find the all factors of x using a loop and the operator %
    # % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
    for i in range(1, x+1):
        if x % i == 0:
            factors.append(i)
    return factors

# Write a function that prints all factors of the given parameter x
def print_factor(x):
    factors = find_factors(x)
    print("Factors of", x, "are:")
    for factor in factors:
        print(factor)

# Write a program that be able to find all factors of the numbers in the list l
def find_factors_list(l):
    for x in l:
        print_factor(x)

if __name__ == '__main__':
    main()




