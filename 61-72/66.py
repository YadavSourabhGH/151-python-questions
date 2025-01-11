# Decimal to binary

def decimal_to_binary(decimal_number):
    binary = ""
    '''
        The binary variable is initially set to an empty string ("") because this is    
        where the binary digits (either 0 or 1) will be accumulated. 
        Each new digit will be added to the front of this string as the conversion process proceeds.
    '''
    while decimal_number > 0:
        binary = str(decimal_number % 2) + binary
        decimal_number //= 2
    return binary

decimal = int(input("Enter a decimal number: "))
print(f"The binary equivalent of {decimal} is: {decimal_to_binary(decimal)}")


