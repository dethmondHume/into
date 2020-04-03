import sys

line = str(sys.argv[1])
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_line = ''

for i in line:
    letter_position = alphabet.find(i.lower())
    if letter_position != -1:
        new_line += i        

new_line1 = ''

for i in range(len(new_line) - len(new_line) % 5):
    new_line1 += new_line[i]

new_line2 = ''

for i in new_line1:
    if alphabet.find(i) != -1:
        new_line2 += 'a'
    else:
        new_line2 += 'b'

new_line3 = ''
start = 0
end = 5

for i in range(len(new_line2)/5):
    new_line3 += alphabet[key.find(new_line2[start:end])]
    start += 5
    end += 5

print new_line3
