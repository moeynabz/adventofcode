multi_line_string = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
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
    
    for character in word:
        if character.isdigit():
            list_of_identified_numbers.append(int(character))
            
    return [list_of_identified_numbers[0], list_of_identified_numbers[-1]]
    
def combine_numbers(first_number: int, last_number = 0) -> int:
    result = 0
    
    if last_number == 0:
        result = int(str(first_number) + str(first_number))
    else:
        result = int(str(first_number) + str(last_number))
        
    return result

final_sum = 0

counter = 0

while multi_line_string != "":
    index_of_new_line = new_line_index(multi_line_string)
    word = multi_line_string[0:index_of_new_line]
    fnum_lnum_list = find_numbers_in_word(word)
    final_sum += combine_numbers(fnum_lnum_list[0], fnum_lnum_list[1])
    multi_line_string = multi_line_string[index_of_new_line::]

print(final_sum)