# A Python3 Program to generate test cases 
# for array filled with random numbers 
import random 
  
# the number of runs 
# for the test data generated 
RUN = 5; 
  
# minimum range of random numbers 
lowerBound = 0; 
  
# maximum range of random numbers 
upperBound = 1000; 
  
# minium size of reqd array 
minSize = 10; 
  
# maximum size of reqd array 
maxSize = 20; 
  
# Driver Code 
if __name__ == '__main__': 
  
    for i in range(RUN): 
        size = random.randrange(0, maxSize - minSize) + minSize; 
        array = [0]*size; 
  
        print(size); 
  
        for j in range(size): 
            a = random.randrange(0, upperBound - lowerBound) + lowerBound; 
            print(a, end=" "); 
  
        print(); 
