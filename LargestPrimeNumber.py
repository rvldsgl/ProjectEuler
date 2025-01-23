
def is_prime_number(number):
    if number <= 1:
        return False  
    if number <= 3:
        return True  
    if number % 2 == 0 or number % 3 == 0:
        return False  
    i = 5
    while i * i <= number:  
        if number % i == 0 or number % (i + 2) == 0:
            return False  
        i += 6  
    return True  


list_of_prime = []
is_true = True

def prime_factor(number):
  global is_true
  i = 2    
  while is_true:
    if is_prime_number(i) and number % i == 0:
        number = number // i
        list_of_prime.append(i)
        
    elif is_prime_number(number) :
        list_of_prime.append(number)
        print(list_of_prime)
        is_true = False
    else:
      i +=1

prime_factor(600851475143)


        



