'''=================================================================================='''
'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
'''

def move_zeros(array):
    count, arr = 0, []
    for i in range(len(array)):
        if type(array[i]) != bool and array[i] == 0:
            count += 1
        else:
            arr.append(array[i])
    for i in range(count):
        arr.append(0)
    return arr

'''=================================================================================='''
'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

def pig_it(text):
    string = []
    bad_chars = [";", ":", "!", "*", ",", " ", "?"] 
    for i in text.split():
        if i not in bad_chars:
            string.append(i[1:] + i[0] + 'ay')
        else:
            string.append(i)
    string_2 = ' '.join(string)
    return string_2

'''=================================================================================='''
