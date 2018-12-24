def dict_print(dictionary, key_width, value_width):
    print('Keys'.ljust(key_width) + ' ' + 'Values'.ljust(value_width))
    for k, v in dictionary.items():
        print(str(k).ljust(key_width) + ' ' + str(v).ljust(value_width))

picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000} 

dict_print(picnic_items, 20, 20)
