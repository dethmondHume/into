class SuperStr(str):
    s = None

    def __init__(self, s):
        self.s = s
    
    def is_repeatance(self, s):
        pass

    def is_palindrom(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        new_string = ''
        letter_position = None
        for i in self.s:
            letter_position = alphabet.find(i)
            if letter_position != -1:
                new_string = new_string + i
        reverse_list = list(new_string)
        reverse_list.reverse()
        print reverse_list
        print new_string
        if reverse_list==list(new_string):
            return True
        else:
            return False

test1 = SuperStr('12321')
print test1.is_palindrom()
test2 = SuperStr('12345')
print test2.is_palindrom()
test3 = SuperStr('asdsa')
print test3.is_palindrom()
test4 = SuperStr('asdfg')
print test4.is_palindrom()
test5 = SuperStr('asa')
print test5.is_palindrom()




