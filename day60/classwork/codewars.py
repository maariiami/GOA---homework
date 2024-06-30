#https://www.codewars.com/kata/555a67db74814aa4ee0001b5/train/python

def is_even(n): 
   if n % 2 == 0:
    return True
   else:
        return False
   

#https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python

def find_average(numbers):
    
    if len(numbers) == 0:
        return 0
    
    sum_of_numbers = sum(numbers)
    length_of_numbers = len(numbers)
    
    return sum_of_numbers / length_of_numbers
   
#https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/python

def reverse_number(n):
    n = str(n)
    n = n[::-1]
    
    if n[-1] == '-':
        n = n[0:-1]
        n = "-" + n
        
    return int(n)


#https://www.codewars.com/kata/5966eeb31b229e44eb00007a/train/python

def vaporcode(s):
    s =  s.replace(" " , "")
    s = s.upper()
    chars = []
    
    for char in s:
        chars.append(char)
        
    return "  " .join(chars)

#https://www.codewars.com/kata/5566b0dd450172dfc4000005/train/python

def length_of_sequence(arr,n):
    if arr.count(n) != 2:
        return 0
    
    first = arr.index(n)
    second = 0
    
    for index in range (len(arr) -1 , -1, -1):
        if arr[index] ==n:
            second = index
            break
        
    return len(arr[first:second +1])
    
#https://www.codewars.com/kata/5868812b15f0057e05000001/train/python

def tail_swap(strings):
    first_arr = strings[0].split(":")
    second_arr = strings[1].split(":")
    
    temp = first_arr[1]
    first_arr[1] = second_arr[1]
    second_arr[1] = temp
    
    return[":".join(first_arr), ":".join(second_arr)]
    
#https://www.codewars.com/kata/58d76854024c72c3e20000de/train/python


        
