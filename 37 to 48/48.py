# Given a dictionary {key: value}, swap keys and values if all values are unique (produce {value: key}).

my_dict = {
    "Chaitanya": "A",
    "Sourabh": "B",
    "Vinayak": "C",
    "shashank": "D",
    "Yash": "E",
    "Soham": "F",
    "Ronak": "G",
    "Sujal": "H",
    "Rohan": "I",
    "Tanishq": "J"
}

swapped_dict = {value: key for key, value in my_dict.items() if len(my_dict) == len(set(my_dict.values()))}

print("Swapped dictionary:", swapped_dict)