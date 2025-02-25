import math

def is_prime(n):
    """Check if a number is prime in O(sqrt(n)) time."""
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def find_k_for_prime(prime):
    """Find the smallest k such that prime * k ends in 1 or 9."""
    for i in range(1, 4):  # Ensure we search through a valid range
        product = prime * i
        last_digit = product % 10
        if last_digit == 1:
            return (product - 1) // 10  # k is positive
        elif last_digit == 9:
            return -((product + 1) // 10)  # k is negative
    return None  # Should never happen for primes

def check_divisibility_by_prime(number, prime):
    """Check divisibility using place value reduction."""
    k = find_k_for_prime(prime)
    if k is None:
        return False, []

    steps = [number]
    seen = set()  # Prevent infinite loops

    while number >= 10:
        if number in seen:  # Cycle detection
            break
        seen.add(number)

        last_digit = number % 10
        remaining_digits = number // 10
        number = remaining_digits - (last_digit * k)  # Apply correct transformation
        steps.append(number)

    return number % prime == 0, steps

def main():
    print("Prime Divisibility Checker\n")

    number = int(input("Enter the number to check: "))

    while True:
        prime = int(input("Enter a prime number: "))
        if is_prime(prime):
            break
        print("Not a prime number. Try again.")

    is_divisible, steps = check_divisibility_by_prime(number, prime)
    k = find_k_for_prime(prime)

    print(f"\nk value for {prime}: {k}")
    print("\nSteps:")
    for step in steps:
        print(step)
    
    print(f"\nFinal result: {steps[-1]}")
    print(f"{number} is {'divisible' if is_divisible else 'not divisible'} by {prime}.")

    # Verify with actual division
    print(f"\nVerification: {number} ÷ {prime} = {number / prime:.2f} with remainder {number % prime}")

if __name__ == "__main__":
    main()

