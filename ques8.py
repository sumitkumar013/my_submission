def difference(n):
    # Check if n is less than or equal to 17
    if n <= 17:
        # If n is less than or equal to 17, return the absolute difference between 17 and n
        return 17 - n
    else:
        # If n is greater than 17, return the absolute difference between n and 17 multiplied by 2
        return (n - 17) * 2

# Call the "difference" function with the argument 22 and print the result
print(difference(22))

# Call the "difference" function with the argument 14 and print the result
print(difference(14))
