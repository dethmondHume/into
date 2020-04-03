morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--.."
}

def encode_morze(text):
    
    text = text.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    new_string = ''
    letter_position = None
    for u in text:
        letter_position = alphabet.find(u)
        if letter_position != -1:
            new_string = new_string + u
    result = ''
    z = len(new_string)
    for i in new_string:
        string = str(morse_code.get(i, 11))
        k = len(string)
        for j in string:            
            if j == "-":
                result = result + "^^^"
            if j == ".":
                result = result + "^"
            if k > 1:
                result = result + "_"
                k = k - 1
        if z > 1:
            result = result + "___"
            z = z - 1
    return result

encode_morze('Morze code')
