'''=================================================================================='''
'''
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:
a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If we change the first number to something else, comp may not return true anymore:
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.
Remarks
a or b might be [] (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in Haskell, Elixir, C++, Rust, R, Shell, PureScript).
If a or b are nil (or null or None), the problem doesn't make sense so return false.
Note for C
The two arrays have the same size (> 0) given as parameter in function comp.
'''
from math import sqrt

def comp(array1, array2):
    if array1 == None or array2 == None or array1 == [] and array2 != [] or array1 != [] and array2 == []:
        return False
    if array1 == [] and array2 == []:
        return True
    if False in [False if array1[i]**2 not in array2 else array2.remove(array1[i]**2) for i in range(len(array1))]:
        return False
    else:
        return True

'''=================================================================================='''
'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]
'''

def array_diff(a, b):
    if b == [] or b == None:
        return a
    elif a == [] or a == None:
        return []
    b = list(set(b))
    for i in b:
        count = 0
        if i in a:
            for j in a:
                if i == j:
                    count += 1
        if count != 0:
            for k in range(count):
                a.remove(i)
    return a

'''=================================================================================='''
'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
'''

def create_phone_number(n):
    return "({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}".format(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9])

'''=================================================================================='''
'''
Well met with Fibonacci bigger brother, AKA Tribonacci.
As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(
So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.
Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)
If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata
[Personal thanks to Professor Jim Fowler on Coursera for his awesome classes that I really recommend to any math enthusiast and for showing me this mathematical curiosity too with his usual contagious passion :)]
'''

def tribonacci(signature,n):
    if len(signature) >= n:
        return signature[:n]
    signature.append(sum(signature[-3:]))
    return tribonacci(signature, n)

'''=================================================================================='''
'''
A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
For example, take 153 (3 digits):
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):
    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
The Challenge:
Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.
Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.
'''

def narcissistic( value ):
    degree = len(str(value))
    return True if value == sum([int(str(value)[i])**degree for i in range(degree)]) else False

'''=================================================================================='''
'''
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
'''

def find_it(seq):
    for i in seq:
        count=0
        for j in seq:
            if i==j:
                count+=1
        if count%2!=0:
            return i

'''=================================================================================='''
'''
Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.
Let's assume that a song consists of some number of words (that don't contain WUB). To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.
For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".
Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.
Input
The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters
Output
Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
Examples
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
'''

def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

'''=================================================================================='''
'''
Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2, will be too slow.
Example
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
'''

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        if num % 2 == 0:
            return False
        i = 3
        while i**2 <= num:
            if num % i == 0:
                return False
            i += 2
        return True

'''=================================================================================='''
'''
The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.
In effect: 89 = 8^1 + 9^2
The next number in having this property is 135.
See this property again: 135 = 1^1 + 3^2 + 5^3
We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.
Let's see some cases:
sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a, b] the function should output an empty list.
sum_dig_pow(90, 100) == []
Enjoy it!!
'''

def sum_dig_pow(a, b):
    l = []
    for i in range(a, b+1):
        if sum(int(num)**(deg+1) for deg, num in enumerate(str(i))) == i:
            l.append(i)
    return l

'''=================================================================================='''
'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?
Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
'''

def tickets(people):
    d = {25:0, 50:0, 100:0}
    price = 25
    for cash in people:
        if cash > price:
            delta = cash - price
            for change in (50,25):
                while change <= delta and d[change] > 0:
                    delta -= change
                    d[change] -= 1
            if delta != 0:
                return 'NO'
        d[cash] += 1
    return 'YES'

'''=================================================================================='''
