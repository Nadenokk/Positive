from itertools import chain

class Component:
    def __init__(self, *algorithm_list):
        self.algorithm_list = algorithm_list

    def __call__(self, source_object):
        result = []
        queue = [source_object]
        while queue:
            result.extend(queue)
            queue = list(chain.from_iterable(
                algorithm(item)
                for item in queue
                for algorithm in self.algorithm_list
            ))
        return result

    def formate(self, name):
        if "Orange" in str(type(name)): return '/Orange'
        if "Lemon" in str(type(name)): return '/Lemon'
        if "Apple" in str(type(name)): return '/Apple'

    def my_method(self, x, n=0):

        fulld={}
        firstalgorithm={}
        emptyalgorithm={}

        if x==Lemon:
            x=Lemon()
            fulld["Potential"]=['/Lemon']
        if x==Orange:
            x=Orange(n)
            fulld["Potential"] = ['/Orange']
        if x==Apple:
            x=Apple()
            fulld["Potential"] = ['/Apple']
        fulld['Algorithm'] = {"FirstAlgorithm": firstalgorithm, "EmptyAlgorithm": emptyalgorithm}
        step1fullFA = FirstAlgorithm().__call__(x)
        if len(step1fullFA) !=0:
            firstalgorithm[fulld["Potential"][0]] = [fulld["Potential"][0]+self.formate(step1fullFA[0]), fulld["Potential"][0]+self.formate(step1fullFA[1])]
            fulld["Potential"].append(fulld["Potential"][0]+self.formate(step1fullFA[0]))
            fulld["Potential"].append(fulld["Potential"][0]+self.formate(step1fullFA[1]))
            if "Orange" in str(type(step1fullFA[0])):
                step2=Orange(3)
                step2fullFA=(FirstAlgorithm().__call__(step2))
                firstalgorithm[fulld["Potential"][0] + self.formate(step1fullFA[0])] = [fulld["Potential"][0]+self.formate(step1fullFA[0])+self.formate(step2fullFA[0])]
                fulld["Potential"].append(fulld["Potential"][0]+self.formate(step1fullFA[0])+self.formate(step2fullFA[0]))
        fullEA = EmptyAlgorithm().__call__(x)
        if len(fullEA)!=0: emptyalgorithm[fulld["Potential"][0]]=[fulld["Potential"][0]+self.formate(fullEA[0])]
        return fulld


class Apple:
    pass
class Orange:
    def __init__(self, number):
        self.number = number

class Lemon:
    pass

class FirstAlgorithm:
    SPECIFICATION = {
        Orange: [Apple],
        Lemon: [Orange, Apple]
    }

    def __call__(self, source_object):
        if isinstance(source_object, Orange):
            return [
            Apple() for _ in range(source_object.number)
            ]
        if isinstance(source_object, Lemon):
            return [Orange(3), Apple()]
        return []


class EmptyAlgorithm:
    SPECIFICATION = {}

    def __call__(self, source_object):
        return []


import json

component = Component(FirstAlgorithm(), EmptyAlgorithm())
print(json.dumps(component.my_method(Lemon), indent=4))
