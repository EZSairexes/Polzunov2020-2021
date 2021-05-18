
class Storage():
    
    def __init__(self, name, adress, list_rack):
        self.__name = name
        self.__adress = adress
        self.__list_rack = list_rack
        

    def get_param(self, what):
        
        if what == 'name':
            return self.__name
        elif what == 'adress':
            return self.__adress
        else:
            return self.__list_rack


s = Storage('NAme', 'Times Squere', ['1', '2', '3'])

print(s.get_param('name'))

class Rack():

    def __init__(self, num, list_pack):
        self.__num = num
        self.__list__pack = list_pack

    def get_param(self, what):
        if what == 'num':
            return self.__num
        else:
            return self.__list__pack

r = Rack(5, ['y', 'd', 'g', 'al'])

print(r.get_param('list_pack'))


class Material():

    def __init__(self, name):
        self.__name = name

    def get_param(self, what):
        if what == 'name':
            return self.__name

m = Material('wood')
print(m.get_param('name'))


class Pack():

    def __init__(self, id, material, how_much):
        self.__id = id
        self.__material = material
        self.__how_much = how_much

    def get_param(self, what):
        if what == 'id':
            return self.__id
        elif what == 'material':
            return self.__material
        else:
            return self.__how_much


p = Pack(44232, 'metal', 55)
print(p.get_param('how_much'))


