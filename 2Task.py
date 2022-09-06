def my_code(obj, key, list1=None):
    if list1 is None:
        list1 = []
    list1.append(key)  # добавляю в лист вершину с которой работаю
    if key in obj.keys():
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (list)):
                    for v1 in v:
                        if (v1 in obj[key] and k==key): #условия смежной вершины: 1) значение есть в словаре под номером родительской
                                                            # 2) номер совпадает с номером родительской
                            if v1 not in obj.keys() or len(obj[v1])==1: #убеждение, что это вершина крайняя или что связана лишь с одной дочерней вершиной
                                obj[key].remove(v1)
                            return my_code(obj, v1, list1)
    else: # пошел заново с первой вершины другие пути искать
        return my_code(obj, list1[0], list1)
    return print_answer(list1)

def print_answer(l): #привожу к формату вывода, так как в лист складываются все маршруты к конечным вершинам
    answer = []
    [answer.append(x) for x in l if x not in answer]
    print(*answer, sep='\n')

data = {
 1: [2, 3],
 2: [4]
}
data1 = {
 1: [2, 3],
 2: [3, 4],
 4: [1]
}
my_code(data, 1)
my_code(data1, 1)



