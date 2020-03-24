import sys

str = sys.argv[1].lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

new_string = ''
letter_position = None


for i in str:
    letter_position = alphabet.find(i)
    if letter_position != -1:
        new_string = new_string + i


reverse_list = list(new_string)

reverse_list.reverse()
if reverse_list==list(new_string):
    print 'YES'
else:
    print 'NO'



