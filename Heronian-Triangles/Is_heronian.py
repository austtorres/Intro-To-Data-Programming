import math

def area(a, b, c):
  
  
  a = float(a)
  b = float(b)
  c = float(c)
  
  s = (a + b + c)/2
  
  area= math.sqrt(s*(s-a)*(s-b)*(s-c))
  
  return area



def is_heronian(a, b, c):
  
  if int(a) != a or int(b) != b or int(c) != c:
    return False
    
  if int(area(a, b, c)) != area(a, b, c):
    return False
    
  if int(area(a, b, c)) == area(a, b, c):
    return True
    
    
    
    
    
    
    
    
    
