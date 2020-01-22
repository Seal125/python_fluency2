import re

def halved(lst):
    new_lst = []

    for num in lst:
        new_lst.append(num / 2)

    return new_lst

def only_positive(lst):
    new_lst = []

    for num in lst:
        if num >= 0:
            new_lst.append(num)

    return new_lst

def total(lst):
    return sum(lst)

def stripped_strings(lst):
    new_lst = []

    for word in lst:
        new_lst.append(re.sub('[^A-Za-z]', '', word))

    return new_lst

def find_special(lst):
    return [i for i in range(len(lst)) if lst[i] == 'special']

def valid_contacts(lst):
    return [lst[i] for i in range(len(lst)) if len(lst[i].phone_number) == 10]

print(valid_contacts([
        {"name": 'Reuben', "phone_number": '9196218777'},
        {"name": 'Laisha', "phone_number": '0123334766'},
        {"name": 'Cielo', "phone_number": '764'},
        {"name": 'Maya', "phone_number": '7653324599'}
      ]))