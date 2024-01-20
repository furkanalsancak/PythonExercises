def digital_root(n):
    # Continue the loop until n is a single-digit number
    while n >= 10:
        # Convert the number to a list of its digits
        digits = []
        for digit in str(n):
            digits.append(int(digit))
        
        # Calculate the sum of the digits
        digit_sum = sum(digits)
        
        # Display the process
        print(f"{n}  -->  {' + '.join(map(str, digits))} = {digit_sum}", end="  -->  ")

        # Update n with the sum of digits
        n = digit_sum

    print(n)  # Print the final result
    return n

# Example usage:
nums = [942, 456]

for num in nums:
    result = digital_root(num)
    print(f"The digital root of {num} is: {result}")