# -*- coding: utf-8 -*-
"""
Author: Haixu Leng
Date: 02/23/2020

different algorithms for multiplication.
"""
import time # for performance benchmark

class gradeMultiplication:
    '''
    Since we are dealing with very large numbers, we will use a string for input
    and output.
    '''
    def __init__(self, numberA, numberB):
        self.numberA = numberA
        self.numberB = numberB
        self.result = self.multiplication(self.numberA, self.numberB)
        
    def multiplication(self, numberA, numberB):
        sumList = []
        self.numberA = int(self.numberA)
        i = 0
        for digit in self.numberB[::-1]:
            a = int(digit)
            partialMultiplication = str(a * self.numberA) + "0" * i
            i = i + 1
            sumList.append(int(partialMultiplication))
        return sum(sumList)
    
    def get(self):
        return self.result
    
class recursiveMultiplication(gradeMultiplication):
    '''
    In this algorithm, the two numbers x and y will be decomposed into
    x = 10^(n/2) * a + b
    y = 10^(n/2) * c + d
    assuming n is even
    '''
    def __init__(self, numberA, numberB):
        self.numberA = numberA
        self.numberB = numberB
        self.nHalf = 4
        self.result = self.multiplication(self.numberA, self.numberB, self.nHalf)
        
    def multiplication(self, numberA, numberB, nHalf = 4): # override, n = 2, nHalf = 1
        n = 2 * nHalf
        if len(numberA) < n and len(numberB) < n:
            #print(numberA + "  " + numberB)
            return str(int(numberA) * int(numberB))
        else:
            if len(numberA) < n:
                a = 0
            else:
                a = int(numberA[: -nHalf])
            b = int(numberA[-nHalf:])
            if len(numberB) < n:
                c = 0
            else:
                c = int(numberB[: -nHalf])
            d = int(numberB[-nHalf:])
            
            ac = self.multiplication(str(a),str(c))
            bd = self.multiplication(str(b),str(d))
            adbc = str(int(self.multiplication(str(a + b),str(c + d))) - int(ac) - int(bd))
            return str(int(ac + "0" * n) + int(adbc + "0" * nHalf) + int(bd))
        
    
    
    
if __name__ == "__main__":
    a = "3141592653589793238462643383279502884197169399375105820974944592"
    b = "2718281828459045235360287471352662497757247093699959574966967627"
    t0 = time.perf_counter()
    test = gradeMultiplication(a,b)
    t1 = time.perf_counter()
    print(test.get(), "lasted: ", (t1-t0))
    
    
    a = "3141592653589793238462643383279502884197169399375105820974944592"
    b = "2718281828459045235360287471352662497757247093699959574966967627"
    t0 = time.perf_counter()
    test = recursiveMultiplication(a,b)
    t1 = time.perf_counter()
    print(test.get())
    print(test.get(), "lasted: ", (t1-t0)) # recursive is slower than grade? The performance depends on n
            

