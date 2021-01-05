# A Python3 Program to generate test cases 
# for random number 
import random 
  
# the number of runs 
# for the test data generated 
requiredNumbers = 5; 
  
# minium range of random numbers 
lowerBound = 0; 
  
# maximum range of random numbers 
upperBound = 1000; 
  
# Driver Code 
if __name__ == '__main__': 
  
    for i in range(requiredNumbers): 
        a = random.randrange(0, upperBound - 
                    lowerBound) + lowerBound; 
        print(a); 
