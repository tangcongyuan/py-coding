class Base:
    def __init__(self):
        print('Base init.')

class Derived(Base):
    def __init__(self):
        print('Derived init.')
        super().__init__()

class Final(Derived):
    def __init__(self):
        print('Final init.')
        super().__init__()

if __name__ == '__main__':
    # d = Derived()
    f = Final()