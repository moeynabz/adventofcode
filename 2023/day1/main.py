multi_line_string = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def new_line_index(multi_line_string: str) -> int:
    index_of_new_line = 0

    for index, word in enumerate(multi_line_string):
        if word == "\n":
            index_of_new_line = index + 1
            break
    return index_of_new_line

def find_numbers_in_word(word: str) -> list:
    list_of_identified_numbers = []
    result = []
    
    list_of_numbers_as_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    
    for word_number in (list_of_numbers_as_dict.keys()):
        if word_number in word:
            word = word.replace(word_number, str(list_of_numbers_as_dict[word_number]))
            result.append(list_of_numbers_as_dict[word_number])

    for character in word:
        if character.isdigit():
            list_of_identified_numbers.append(int(character))
            
    result = [list_of_identified_numbers[0], list_of_identified_numbers[-1]]
    print(word)
    return result

def combine_numbers(first_number: int, last_number=0) -> int:
    result = 0

    if last_number == 0:
        result = int(str(first_number) + str(first_number))
    else:
        result = int(str(first_number) + str(last_number))

    return result


final_sum = 0

while multi_line_string != "":
    index_of_new_line = new_line_index(multi_line_string)
    word = multi_line_string[0:index_of_new_line]
    print(word)
    fnum_lnum_list = find_numbers_in_word(word)
    print(fnum_lnum_list)
    final_sum += combine_numbers(fnum_lnum_list[0], fnum_lnum_list[1])
    multi_line_string = multi_line_string[index_of_new_line::]


print(find_numbers_in_word("eightwothree"))