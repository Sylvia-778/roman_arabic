# Created on Wed Oct 16

# @author: jiangliqi

import sys
import re


def arabic1_is_valid(convert_number):
    if arabic2_is_valid(convert_number) and int(convert_number) <= 3999:
        return True
    else:
        return False


def arabic2_is_valid(convert_number):
    if convert_number.isdigit() and convert_number[0] != '0' and int(convert_number) > 0:
        return True
    else:
        return False


def symbol2_is_valid(convert_number):
    if re.compile(r'[a-zA-Z]+$').match(convert_number):
        convert_number_list = list(convert_number)
        for i in convert_number_list:
            if convert_number_list.count(i) > 1:
                return False
        return True
    else:
        return False


def letter3_is_valid(convert_letter):
    if re.compile(r'[a-zA-z]+$').match(convert_letter):
        return True
    else:
        return False


def roman_is_valid(roman_number):
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if re.compile(r'[IVXLCDM]+$').match(roman_number):
        return convert_letter_is_valid(roman_number, roman_dict)
    else:
        return False


def letter2_is_valid(convert_number, generalised_letter):
    letter_dict = generalised_to_classical(generalised_letter)
    if re.compile(r'[a-zA-Z]+$').match(convert_number):
        return convert_letter_is_valid(convert_number, letter_dict)
    else:
        return False


def convert_letter_is_valid(convert_number, letter_dict):
    convert_list = list(convert_number)
    one_start_list = []
    five_start_list = []
    for i in convert_list:
        if i not in letter_dict.keys():
            return False
    for key, value in letter_dict.items():
        if re.compile(r'1[0]*$').match(str(value)):
            one_start_list.append(key)
        else:
            five_start_list.append(key)
    if len(convert_number) > 3:
        for i in range(len(convert_number) - 3):
            if convert_number[i] == convert_number[i + 1] and convert_number[i + 1] == convert_number[i + 2] and convert_number[i + 2] == convert_number[i + 3]:
                return False
    for i in five_start_list:
        if convert_list.count(i) > 1:
            return False
    if len(convert_list) > 1:
        for i in range(len(convert_list) - 1):
            if letter_dict[convert_list[i]] < letter_dict[convert_list[i + 1]]:
                if convert_list[i] not in one_start_list or 10 * letter_dict[convert_list[i]] < letter_dict[convert_list[i + 1]]:
                    return False
    if len(convert_list) > 2:
        for i in range(len(convert_list) - 2):
            if letter_dict[convert_list[i]] < letter_dict[convert_list[i + 2]]:
                return False
            if letter_dict[convert_list[i]] == letter_dict[convert_list[i + 2]] and letter_dict[convert_list[i]] < letter_dict[convert_list[i + 1]]:
                return False
    return True


def generalised_to_classical(letter):
    letter_list = list(letter)
    letter_list.reverse()
    letter_dict = {}
    letter_dict.update({letter_list[0]: 1})
    for i in range(0, len(letter_list), 2):
        if i+1 in range(len(letter_list)):
            letter_dict.update({letter_list[i] + letter_list[i + 1]: letter_dict[letter_list[i]] * 4})
            letter_dict.update({letter_list[i + 1]: letter_dict[letter_list[i]] * 5})
        else:
            break
        if i+2 in range(len(letter_list)):
            letter_dict.update({letter_list[i] + letter_list[i + 2]: letter_dict[letter_list[i]] * 9})
            letter_dict.update({letter_list[i + 2]: letter_dict[letter_list[i]] * 10})
        else:
            break
    return letter_dict


def arabic_to_roman(arabic_num):
    roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    return arabic_convert(arabic_num, roman_dict)


def arabic_to_generalised(convert_number, generalised_letter):
    symbol_dict = generalised_to_classical(generalised_letter)
    if convert_letter_is_valid(arabic_convert(convert_number, symbol_dict), symbol_dict):
        return arabic_convert(convert_number,symbol_dict)
    else:
        return False


def arabic_convert(convert_number, symbol_dict):
    result = ''
    letter = list(symbol_dict.keys())
    letter_value = list(symbol_dict.values())
    letter.reverse()
    letter_value.reverse()
    for i in range(len(letter)):
        while convert_number >= letter_value[i]:
            convert_number -= letter_value[i]
            result += letter[i]
        if convert_number == 0:
            break
    return result


def roman_to_arabic(roman_number):
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    return letter_convert(roman_number, roman_dict)


def generalised_to_arabic(convert_number, generalised_letter):
    generalised_dict = generalised_to_classical(generalised_letter)
    return letter_convert(convert_number, generalised_dict)


def letter_convert(convert_number, symbol_dict):
    arabic_number = 0
    for i in range(len(convert_number) - 1):
        if symbol_dict[convert_number[i]] < symbol_dict[convert_number[i + 1]]:
            arabic_number -= symbol_dict[convert_number[i]]
        else:
            arabic_number += symbol_dict[convert_number[i]]
    arabic_number += symbol_dict[convert_number[-1]]
    return arabic_number


def generalised_symbol(convert_letter):
    convert_list = list(convert_letter)
    no_order_list = []
    compare_list = []
    one_start_list = []
    if len(convert_list) == 1:
        str_using = convert_list[0]
    elif len(convert_list) == 2:
        str_using = convert_list[1] + convert_list[0]
    else:
        for i in range(len(convert_list) - 2):
            for j in range(i + 2, len(convert_list)):
                if convert_list[i] != convert_list[j]:
                    compare_list.append((convert_list[i], convert_list[j]))
        for i in range(len(convert_list) - 2):
            if convert_list[i] == convert_list[i + 2] and convert_list[i] != convert_list[i + 1]:
                compare_list.append((convert_list[i], convert_list[i + 1]))
        for i in compare_list:
            if (i[1], i[0]) in compare_list:
                return False
        for i in convert_list:
            if convert_list.count(i) > 1:
                one_start_list.append(i)
        for i in range(len(convert_list) - 1):
            if (convert_list[i + 1], convert_list[i]) in compare_list:
                one_start_list.append(convert_list[i])
        for i in convert_list:
            if i not in no_order_list:
                no_order_list.append(i)
        for item in compare_list:
            index0 = no_order_list.index(item[0])
            index1 = no_order_list.index(item[1])
            if index0 > index1:
                no_order_list[index0], no_order_list[index1] = no_order_list[index1], no_order_list[index0]
        if len(no_order_list) > 1:
            no_order_list.reverse()
            count = 0
            for i in no_order_list:
                if count == len(no_order_list) - 1:
                    break
                position = no_order_list.index(i)
                if (no_order_list[position + 1], no_order_list[position]) in compare_list:
                    if no_order_list[position + 1] in one_start_list and (position + 1) % 2 != 0:
                        no_order_list.insert(position + 1, '_')
                else:
                    if no_order_list[position] not in one_start_list and position % 2 == 0:
                        no_order_list[position], no_order_list[position + 1] = no_order_list[position + 1], no_order_list[position]
                count += 1
            no_order_list.reverse()
        str_using = ''.join(no_order_list)
    return str_using


if __name__ == "__main__":
    word = input('How can I help you? ')
    form1 = re.compile(r'[\s]*Please[\s]+convert[\s]+([\S]+)[\s]*$')
    form2 = re.compile(r'[\s]*Please[\s]+convert[\s]+([\S]+)[\s]+using[\s]+([\S]+)[\s]*$')
    form3 = re.compile(r'[\s]*Please[\s]+convert[\s]+([\S]+)[\s]+minimally[\s]*$')
    if form1.match(word):
        converted_number = form1.match(word).group(1)
        if arabic1_is_valid(converted_number):
            print('Sure! It is', arabic_to_roman(int(converted_number)), sep=' ')
        elif roman_is_valid(converted_number):
            print('Sure! It is', roman_to_arabic(converted_number), sep=' ')
        else:
            print('Hey, ask me something that\'s not impossible to do!')
    elif form2.match(word):
        converted1 = form2.match(word).group(1)
        converted2 = form2.match(word).group(2)
        if symbol2_is_valid(converted2):
            if arabic2_is_valid(converted1):
                if arabic_to_generalised(int(converted1), converted2):
                    print('Sure! It is', arabic_to_generalised(int(converted1), converted2), sep=' ')
                else:
                    print('Hey, ask me something that\'s not impossible to do!')
            elif letter2_is_valid(converted1, converted2):
                print('Sure! It is', generalised_to_arabic(converted1, converted2), sep=' ')
            else:
                print('Hey, ask me something that\'s not impossible to do!')
        else:
            print('Hey, ask me something that\'s not impossible to do!')
    elif form3.match(word):
        convert3 = form3.match(word).group(1)
        if letter3_is_valid(convert3) and generalised_symbol(convert3):
            print('Sure! It is', generalised_to_arabic(convert3, generalised_symbol(convert3)), 'using', generalised_symbol(convert3), sep=' ')
        else:
            print('Hey, ask me something that\'s not impossible to do!')
    else:
        print('I don\'t get what you want, sorry mate!')
        sys.exit()


