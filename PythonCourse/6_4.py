def find_most_frequent(text):
    list_words = []
    text = str(text.lower()) + ' '
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_position = None
    tmp = ''
    
    for letter in text:
        letter_position = alphabet.find(letter)
        if letter_position != -1:
            tmp += letter
        else:
            if tmp != '':
                list_words.append(str(tmp))
                tmp = ''
    print list_words    
                    
    index = []
    j = 0
    i = 1
    for j in range(len(list_words) - 1):
        i = j + 2
        while i < len(list_words):
            if list_words[j] == list_words[i]:
                index.append(list_words[i])
                break
            i += 2

    index1 = []
    y = 0
    u = 1
    for y in range(len(index) - 1):
        u = y + 2
        while u < len(index):
            if index[y] == index[u]:
                index1.append(index[u])
                break
            u += 2
            
    print index1
    if len(index) > 1:
        t = 0
        while t < len(index) - 1:
            b = 0
            for b in range(len(index) - 1):
                if index[b] > index[b + 1]:
                    tmp1 = index[b + 1]
                    index[b + 1] = index[b]
                    index[b] = tmp1
            t = t + 1
    print index1
    return index1

find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.') 
