#Root finding with the use of Bisection Method


import numpy as np
from scipy.optimize import fsolve

def roots_with_bisection_method(start_point,end_point,func, tolerance,max_num_of_iteration=50):
    iterations=0
    print ("Iterations \t Start Point \t End Point\tMidpoint\t Function(midpoint)")
    while iterations <= max_num_of_iteration:
        midpoint= (start_point + end_point)/2  #bisection method formula for midpoint of two provided points
        mid_function =func(midpoint)
        
        result = print (iterations, "\t\t",'{:.5f}'.format(start_point),"\t",'{:.5f}'.format(end_point),'\t{:.5f}'.format(midpoint),"\t ",'{:.4f}'.format(mid_function) )
        if abs(end_point-start_point)< tolerance:
            break 
        iterations= iterations +1
        if func(start_point) *mid_function>0:
            start_point=midpoint
        else:
            end_point=midpoint
        
    return result, midpoint  #returning to continue the loop untill the root is found with specified tolerance.
    
#defining the function whose roots are to be found 
given_function= lambda x:  (np.exp(x)-(5*(x**2))) #np.exp(-x) + np.cos(2*np.pi*x)
#another way to define the function 
# def given_func(x):
#     return (np.exp(x)-(5*(x**2)))

#Asking user for the interval where they want to find the root/s of the function 
print("Enter values for Start Point(a): ")
start_point = float(input())

print("Enter values for Endpoint(b): ")
end_point = float(input())
print("\n")

#Call the pre definded function 
outcome =roots_with_bisection_method(start_point,end_point,given_function, 0.00001)
print (f"\nThe root in interval [{start_point}, {end_point}] =", outcome[1])

#This method finds the multiple roots in specific interval 
fsolve_method = fsolve (given_function,(start_point,end_point))
print("\nRoots with the help of fsolve method ", fsolve_method )
