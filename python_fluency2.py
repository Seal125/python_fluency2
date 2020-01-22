import re

def halved(lst):
    return [num / 2 for num in lst]

def only_positive(lst):
    return [num for num in lst if num > 0]

def total(lst):
    return sum(lst)

def stripped_strings(lst):
    return [re.sub('\W', '', word) for word in lst]

def find_special(lst):
    return [i for i in range(len(lst)) if lst[i] == 'special']

def valid_contacts(lst):
    return [contact for contact in lst if len(contact.phone_number) == 10]

def contact_names(lst):
    return [contact['name'] for contact in lst]

print(contact_names([
        {name: 'Reuben', "phone_number": '9196218777'},
        {name: 'Laisha', "phone_number": '0123334766'},
        {name: 'Cielo', "phone_number": '764'},
        {name: 'Maya', "phone_number": '7653324599'}
      ]))