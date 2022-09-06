
def my_code(data, n=1):
    for key, value in data.items():
        print(key, ':', sep='')
        if isinstance(value, dict):
            data1={**value}
            print('\t', end='')
            my_code(data1, n+1)
        else:
            print(n*'\t', value, sep='')

my_code({
 'first': 'first_value',
 'second': 'second_value'
})

my_code({
 '1': {
 'child': '1/child/value',
 },
 '2': '2/value'
})

my_code({
 '1': {
 'child': '1/child/value',
 },
 '2': '2/value'
})

#my_code({1: {'Name': 'Ashish', 'Age': 33, 'Designation': 'Web Developer'}, 2: {'Name': 'Shubham', 'Age': 23, 'Designation': 'IOS APP Developer'}, 3: {'Name': 'Vandana', 'Age': 25, 'Designation': 'Data Scientist'}})