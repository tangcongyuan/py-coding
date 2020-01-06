from collections import UserDict

class TopicDict(UserDict):
    def __getitem__(self, key):
        value = super().__getitem__(key)
        print(value)
        return f'[{value}]'

if __name__ == '__main__':
    td = TopicDict({'key': 'value'})
    print(td.values())