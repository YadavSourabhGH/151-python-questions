#Number to Words

def number_to_words(number):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = ""
    for digit in str(number):
        result += words[int(digit)] + " "
    return result.strip()

num = int(input("Enter a number: "))
print(f"{num} in words is: {number_to_words(num)}")


