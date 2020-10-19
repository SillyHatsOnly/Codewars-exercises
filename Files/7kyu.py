'''=================================================================================='''
'''
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
If you want to know more http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
More similar exercise are found here http://rosalind.info/problems/list-view/ (source)
DNA_strand ("ATTGC") # return "TAACG"
DNA_strand ("GTAT") # return "CATA"
'''

def DNA(dna):
    pair = {'A':'T','T':'A','G':'C','C':'G'}
    result = ''
    for i in dna:
        result+= pair[i]
    return result

'''=================================================================================='''
'''
In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?
At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants
At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is an integer)
At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213
It will need 3 entire years.
More generally given parameters:
p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)
the function nb_year should return n number of entire years needed to get a population greater or equal to p.
aug is an integer, percent a positive or null number, p0 and p are positive integers (> 0)
Examples:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
Note: Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.
'''

def nb_year(p0, percent, aug, p):
    y = 0
    while p0 < p:
        p0 = p0 + p0*(percent/100) + aug
        y += 1
    return y

'''=================================================================================='''
'''
You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is positive.
Examples:
findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
'''
from math import sqrt

def find_next_square(sq):
    if (sqrt(sq)).is_integer() == True:
        return (sqrt(sq)+1)**2
    else:
      return -1

'''=================================================================================='''
