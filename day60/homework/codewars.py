#https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
def invert(lst):
    numbers = []
    for num in lst:
        numbers.append(-num)
    return numbers

#https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python
def smash(words):
    word = ' '.join(words)
    return word

#https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/python
def between(a,b):
    return list(range(a, b + 1))

#https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python
def get_grade(s1, s2, s3):
    average_score = (s1 + s2 + s3) / 3
    
    if 90 <= average_score <= 100:
        return "A"
    elif 80 <= average_score < 90:
        return "B"
    elif 70 <= average_score < 80:
        return "C"
    elif 60 <= average_score < 70:
        return "D"
    else:
        return "F"
    
#https://www.codewars.com/kata/5556282156230d0e5e000089/train/python
def dna_to_rna(dna):
    rna = dna.replace('T', 'U')
    return rna

