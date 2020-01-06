class Meta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print(f'clsname: {clsname}.')
        print(f'superclasses: {superclasses}.')
        print(f'attributedict: {attributedict}.')
        tmp = super()
        print(tmp)
        return super().__new__(cls, clsname, superclasses, attributedict)

class Derived(metaclass=Meta):
    pass

d = Derived()