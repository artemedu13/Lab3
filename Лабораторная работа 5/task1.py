from pprint import pprint

def convert_to_dict(a, b):
    dict_list = []
    for number in range(a, b):
        repr_dict = {'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)}
        dict_list.append(repr_dict)
    return dict_list

pprint(convert_to_dict(0, 16))
#Ответ