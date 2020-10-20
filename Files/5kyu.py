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
'''
Consider the following expansion:
solve("3(ab)") = "ababab"     -- because "ab" repeats 3 times
solve("2(a3(b))" = "abbbabbb" -- because "a3(b)" == "abbb", which repeats twice.
Given a string, return the expansion of that string.
Input will consist of only lowercase letters and numbers (1 to 9) in valid parenthesis. There will be no letters or numbers after the last closing parenthesis.
More examples in test cases.
Good luck!
'''

def solve(st):
    res=''
    clear_st = st.replace('(','').replace(')','')
    for i in range(len(clear_st)-1, -1, -1):
        try:
            if type(int(clear_st[i])) == int:
                res *= int(clear_st[i])
        except:
            res = clear_st[i] + res
    return res

#but better way - use str.isalpha() and str.isdigit()
'''=================================================================================='''
