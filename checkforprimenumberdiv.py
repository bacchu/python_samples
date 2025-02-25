def split_by_place_values(number):
    """
    Split a number into its place value components.
    
    Args:
        number: An integer to be decomposed
        
    Returns:
        A string showing the number as a sum of its place value components
    """
    # Convert number to string to easily access digits
    num_str = str(number)
    
    # Get the length of the number
    length = len(num_str)
    
    # Initialize an empty list to store components
    components = []
    
    # Process each digit
    for i, digit in enumerate(num_str):
        # Skip zeros as they don't contribute to the sum
        if digit == '0':
            continue
            
        # Calculate the place value (10^(length-i-1))
        place_value = 10 ** (length - i - 1)
        
        # Add the component to our list
        components.append(f"{digit}*{place_value}")
    
    # Join the components with " + " to create the final string
    result = " + ".join(components)
    
    return result


def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n: The number to check
        
    Returns:
        Boolean: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


def find_prime_factors(n):
    """
    Find all prime factors of a number.
    
    Args:
        n: The number to factorize
        
    Returns:
        List of prime factors with their counts
    """
    factors = []
    
    # Check for factor 2
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        factors.append((2, count))
    
    # Check for odd factors
    factor = 3
    while factor * factor <= n:
        count = 0
        while n % factor == 0:
            count += 1
            n //= factor
        if count > 0:
            factors.append((factor, count))
        factor += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append((n, 1))
    
    return factors


def find_k_for_prime(prime):
    """
    Find the value of k for a prime number according to the rule:
    Multiply the prime by consecutive numbers until you get a number ending in 1 or 9.
    If it ends in 1, k is negative; if it ends in 9, k is positive.
    """
    for i in range(1, prime + 1):
        product = prime * i
        if product % 10 == 1:
            # Calculate k using the formula: 10k - 1 = product
            k = (product + 1) // 10
            return -k
        elif product % 10 == 9:
            # Calculate k using the formula: 10k - 1 = product
            k = (product + 1) // 10
            return k
    
    # This should not happen for primes, but just in case
    return None


def check_divisibility_by_prime(number, prime):
    """
    Check if a number is divisible by a prime using the described rule.
    
    Args:
        number: The number to check
        prime: The prime number to check divisibility against
        
    Returns:
        Boolean: True if number is divisible by prime, False otherwise
        steps: List of intermediate steps in the calculation
    """
    # Find the k value for the prime
    k = find_k_for_prime(prime)
    
    # Convert number to string to work with digits
    num_str = str(number)
    
    # Keep track of steps
    steps = [number]
    current_number = number
    
    # Continue until we reach a two-digit or smaller number
    while current_number >= 100:
        # Get the last digit of the current number
        units_digit = current_number % 10
        
        # Get the remaining digits (all except the last one)
        remaining_digits = current_number // 10
        
        # Apply the formula: remaining_digits + (units_digit * k)
        current_number = remaining_digits + (units_digit * k)
        
        # Add this step to our list
        steps.append(current_number)
    
    # Check if the final number is divisible by the prime
    is_divisible = (current_number % prime == 0)
    
    return is_divisible, steps


def get_valid_integer_input(prompt):
    """
    Get a valid integer input from the user.
    
    Args:
        prompt: The prompt to display to the user
        
    Returns:
        An integer value
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def main():
    # Display welcome message
    print("Welcome to the Prime Divisibility Checker!")
    print("This program can:")
    print("1. Check if a number is divisible by a prime using a special rule")
    print("2. Find all prime factors of a number")
    print("3. Show the number split by place values\n")
    
    # Get input from the user
    number = get_valid_integer_input("Enter a number: ")
    
    # Show place value decomposition
    print(f"\nPlace Value Decomposition:")
    print(f"{number} = {split_by_place_values(number)}\n")
    
    # Find and display prime factors
    print("Finding prime factors...")
    factors = find_prime_factors(number)
    
    if not factors:
        print(f"{number} has no prime factors (it is 1).")
    else:
        print(f"Prime factors of {number}:")
        factor_strings = []
        for prime, count in factors:
            if count == 1:
                factor_strings.append(f"{prime}")
            else:
                factor_strings.append(f"{prime}^{count}")
        
        factor_expression = " × ".join(factor_strings)
        print(f"{number} = {factor_expression}")
        
        # Show the expanded form with all repeated factors
        expanded_factors = []
        for prime, count in factors:
            expanded_factors.extend([prime] * count)
        
        expanded_expression = " × ".join(map(str, expanded_factors))
        print(f"{number} = {expanded_expression}")
    
    # Ask if the user wants to check divisibility by a specific prime
    check_specific = input("\nDo you want to check divisibility by a specific prime? (y/n): ").lower()
    
    if check_specific == 'y':
        # Get the prime number to check divisibility
        while True:
            check_prime = get_valid_integer_input("Enter a prime number to check divisibility: ")
            
            # Verify that the input is a prime number
            if is_prime(check_prime):
                break
            else:
                print(f"{check_prime} is not a prime number. Please enter a prime number.")
        
        # Perform the divisibility check
        is_divisible, steps = check_divisibility_by_prime(number, check_prime)
        
        # Calculate k for the prime
        k = find_k_for_prime(check_prime)
        
        print(f"\nDivisibility Check for {number} by {check_prime}:")
        print(f"k value for {check_prime} is {k}")
        
        # Print the steps
        print("\nSteps:")
        for i, step in enumerate(steps):
            if i < len(steps) - 1:
                units_digit = steps[i] % 10
                remaining_digits = steps[i] // 10
                next_step = steps[i+1]
                print(f"Step {i+1}: {remaining_digits} + ({units_digit} * {k}) = {next_step}")
        
        print(f"\nFinal result: {steps[-1]}")
        
        if is_divisible:
            print(f"{number} is divisible by {check_prime}.")
        else:
            print(f"{number} is not divisible by {check_prime}.")
        
        # As an additional check, show the actual division result
        actual_result = number / check_prime
        remainder = number % check_prime
        print(f"\nVerification: {number} ÷ {check_prime} = {actual_result:.2f} with remainder {remainder}")


if __name__ == "__main__":
    main()
