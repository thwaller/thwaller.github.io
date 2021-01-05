// A Java Program to generate test cases  
// for random number 
import java.io.*; 
import java.util.Random; 
  
class GeneratingRandomNumbers  
{ 
  
    // the number of runs  
    // for the test data generated 
    static int requiredNumbers = 5; 
  
    // minium range of random numbers 
    static int lowerBound = 0; 
  
    // maximum range of random numbers 
    static int upperBound = 1000; 
  
    // Driver Code 
    public static void main (String[] args) throws IOException  
    { 
        Random random = new Random(); 
          
        for(int i = 0; i < requiredNumbers; i++) 
        { 
            int a = random.nextInt(upperBound - lowerBound) +  
                                                lowerBound; 
            System.out.println(a); 
        } 
    } 
} 
