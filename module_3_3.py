def print_params(a=1, b='строка', c=True):
    print(a,b,c)
print_params()
print_params(b=25)
print_params(c=[1,2,3])
values_list = [33, 'human', False]
values_dict = {'a':444, 'b': 99.9, 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [76.32,'world']
print_params(*values_list_2,67)