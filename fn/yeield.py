def get_numbers():
    return [1, 2, 3]

def get_numbers_by_yeild():
    yield 1
    yield 2
    yield 3
new_num = get_numbers_by_yeild()
for n in new_num:
    print(n)