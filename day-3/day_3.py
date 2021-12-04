with open('binary_numbers.txt') as f:
    lines = f.readlines()
    length = len(lines)


# Part One

def most_common(strings):  # Creates a list of amount of 1's at each index for all lines in the string. E.g. a = [1, 3, 2] will have 3 binary numbers with 1 at index 1.  
    indices = []
    bit_length = len(strings[0].strip())  
    for _ in range(bit_length):
        indices.append(0)
    
    for line in strings:
        line = line.strip()
        for index, char in enumerate(line):
            if char == "1":
                indices[index] += 1
    return indices            

def binary_converter(list, list_length):
    output_str = ""
    for index in list:
        if index / list_length >= 0.5:
            output_str += "1"
        else:
            output_str += "0"
    return output_str

# function to flip bits
def flip_bits(binary_str):
    output_str = ""
    for char in binary_str:
        if char == "1":
            output_str += "0"
        else:
            output_str += "1"
    return output_str

# function to convert binary to decimal
def binary_to_decimal(binary_str):
    decimal = 0
    for index, char in enumerate(binary_str):
        if char == "1":
            decimal += 2**(len(binary_str) - index - 1)
    return decimal    


gamma_binary = binary_converter(most_common(lines), length)
epsilon_binary = flip_bits(binary_converter(most_common(lines), length))
gamma_decimal = binary_to_decimal(gamma_binary)
epsilon_decimal = binary_to_decimal(epsilon_binary)
print("Gamma binary: {} \nEpsilon binary: {}".format(gamma_binary, epsilon_binary))
print("Gamma decimal: {} \nEpsilon decimal: {}".format(gamma_decimal, epsilon_decimal))
print("Power consumption: {}".format(gamma_decimal * epsilon_decimal))

# Part Two

def most_common_with_zeros(list, list_length):
    indices = []
    for index in list:
        if index / list_length >= 0.5:
            indices.append(1)
        else:
            indices.append(0)
    return indices

def least_common_with_zeros(list, list_length):
    indices = []
    for index in list:
        if index / list_length <= 0.5:
            indices.append(1)
        else:
            indices.append(0)
    return indices


def oxygen_generator_rating(most_common_list, list):
    line_length = len(list[0].strip())
    trimmed = list
    for i in range(line_length):
        mc_index = most_common_at_index(trimmed, i)
        temp = trim_elements(mc_index, i, trimmed)
        trimmed = temp
        if len(trimmed) == 1:
            return trimmed[0]

def co2_scrubber_rating(least_common_list, list):
    line_length = len(list[0].strip())
    trimmed = list
    for i in range(line_length):
        lc_index = least_common_at_index(trimmed, i)
        temp = trim_elements(lc_index, i, trimmed)
        trimmed = temp
        if len(trimmed) == 1:
            return trimmed[0]


def most_common_at_index(list, index_number):
    length = len(list)
    ind = 0
    for element in list:
        if element[index_number] == "1":
            ind += 1
    if ind / length >= 0.5:
        return 1
    else:
        return 0

def least_common_at_index(list, index_number):
    length = len(list)
    ind = 0
    for element in list:
        if element[index_number] == "1":
            ind += 1
    if ind / length < 0.5:
        return 1
    else:
        return 0


def trim_elements(binary_number, index, list):
    return_list = []
    for element in list:
        if int(element[index]) == binary_number:
            return_list.append(element)
    return return_list


def magic_binary(binary_str): # How did i never know about this? Turns binary to decimal
    return int(binary_str, 2)

def flip_list(list):
    output_list = []
    for item in list:
        if item == 1:
            output_list.append(0)
        else:
            output_list.append(1)
    return output_list


mci = most_common_with_zeros(most_common(lines), length)
ogr = oxygen_generator_rating(mci, lines)
dec_ogr = magic_binary(ogr)
lci = least_common_with_zeros(most_common(lines), length)
# lci = flip_list(mci)
cosr = co2_scrubber_rating(lci, lines)
dec_cosr = magic_binary(cosr)
print("Most common: {}".format(most_common(lines)))
print("Most common with zeros: {}".format(mci))
print("Least common with zeros: {}".format(lci))
print("Oxygen Generator Rating: | binary: {} | decimal: {}".format(ogr, dec_ogr))
print("CO2 Scrubber Rate: | binary {} | decimal: {}".format(cosr, dec_cosr))
print("Life Support Rating: {}.".format(dec_ogr * dec_cosr))
#print(oxygen_generator_rating(most_common_with_zeros(lines), lines))