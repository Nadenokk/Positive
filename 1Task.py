
def my_code(data, n=0):
    for key, value in data.items():
        print(n*'\t',key, ':', sep='')
        if isinstance(value, dict):
            data1={**value}
            my_code(data1, n+1)
        else:
            print((n+1)*'\t', value, sep='')

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
#добавила обещанный пример с ещё одним вложенным словарём
my_code({
 '1': {
 'child': '1/child/value',
     'child1':
         {
             '1/child1':'1/child1/value'
         }
 },
 '2': '2/value'
})
