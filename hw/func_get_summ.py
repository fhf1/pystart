def get_summ(one, two, delimiter='&'):
    return str(f'{one}{delimiter}{two}')

concat_string = get_summ('Learn', 'python')
print(concat_string.upper())
