def count_character_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def print_frequency(frequency):
    print("Character frequency:")
    for char, freq in frequency.items():
        print(f"{char}: {freq}")

# Main program
input_string = input("Enter a string: ")
frequency = count_character_frequency(input_string)
print_frequency(frequency)