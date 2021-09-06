
# 1.Newton Raphson method 
import numpy as np
from math import exp, log
import matplotlib.pyplot as plt
#Newton-Raphson Method of Root finding 

#defining the function 
def newton_raphson_method(initial_function, deriv_of_function, x0, tolerance, max_num_of_iterations=100):
    x1= 0
    if abs(x0-x1)<=tolerance and abs(x0-x1)/x0 <=tolerance:   
        return x0
    print ("No. of Iterations\t\t x0\t\t\t  function(x0)")
    iterations=1
    
    while iterations <= max_num_of_iterations:   #using while loop 
        x1=x0-(initial_function(x0)/deriv_of_function(x0)) #defining Newton's root finiding formula
        print(f"\tx{iterations}\t\t {x1}\t\t{initial_function(x1)}")
        
        if abs(x0-x1)<= tolerance and abs((x0-x1)/x0)<= tolerance:   
            plt.plot(x0, initial_function(x0), 'or')
            return x1
        x0=x1
        iterations += 1
        plt.plot(x0, initial_function(x0), 'or')
        
        
        #stops iterating because of reaching maximum number of iterations
        if iterations >= (max_num_of_iterations+1):
            print ("NO more Iterations possible, you reached the maximum number of Iterations")
    return x1
    #Defining the function whose root/s are to be found 
#log(x) - 1 + exp(-x) #exp(0.5*x) - exp(0.6*x) + 4
initial_function1= lambda x: np.exp(-x) + np.cos(2*np.pi*x) 


#derivative of the function
#((1/x) - exp(-x)) #0.5*exp(0.5*x) - 0.6*exp(0.6*x)
deriv_of_function= lambda x: -np.exp(-x)-2*np.pi*np.cos(2*np.pi) 

#calling the pre-defined function
output_for_solution = newton_raphson_method(initial_function1,deriv_of_function,1.7,0.0000001)
print ("\nThe value of x is: ",output_for_solution)

#Plotting the function with help of matplotlib library

x=np.linspace(-1,5,200)
x_axis=0*x


fig=plt.figure()
ax=plt.subplot()
ax.plot(x,x_axis,'g_', label='x-axis') #defining x axis 
ax.grid()
plt.xlabel('x-variables')
plt.ylabel('f(x)')
ax.plot(x, initial_function1(x), label ='$ exp(-x) + cos(2*pi*x)  $ ')
plt.title ('Plotting the function')
ax.legend()
plt.show()
    
