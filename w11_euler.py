def multi_multiples(irrelevant_no_one_asked_for_this_except_Python_and_your_mom):
    n = 1
    sum = 0
    while (n < 1000):
        if (n % 15 == 0):
            sum = sum + n
        elif (n % 3 == 0):
            sum = sum + n
        elif (n % 5 == 0):
            sum = sum + n
        n = n + 1
    return sum

print (multi_multiples(1))

def sum_square_diff(irrelevant_no_one_asked_for_this_except_Python_and_your_mom):
    n = 1
    sum = 0
    su = 0
    while (n <= 100):
        sum = sum + (n**2)
        su = su + n
        n = n + 1
    squareSum = su**2
    return (squareSum - su)

print (sum_square_diff(0))

def small_mul(irrelevant_no_one_asked_for_this_except_Python_and_your_mom):
    number = 1
    n = 1
    while (n <= 20):
        if (number % n = 0):
            return number
