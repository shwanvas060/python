import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def cal(x,y):
    mean_x = sum(x)/n
    mean_y = sum(y)/n

    i=0
    nu=0.0
    de=0.0

    while(i<n):
        nu += (x[i]-mean_x)*(y[i]-mean_y)
        de += (x[i]-mean_x)*(x[i]-mean_x)
        i+=1
    
    w1=nu/de
    w0=(mean_y) - (w1*mean_x)

    print("W1 = ",w1)
    print("W0 = ",w0)

    print("y =%.2f + %.2f x" %(w0, w1))

    line_x=[]
    line_y=[]
    for i in range(int(max(x))+1):
        line_x.append(i)
        line_y.append(w0+w1*i)
    
    
    plt.plot(line_x, line_y)
    plt.show()
    predicate(w1,w0)
   
def predicate(w1,w0):
    inp=int(input("Enter the Input to predict:"))
    if (min(x)-1)<=inp and (max(x)+5)>=inp:
        print(w0+w1*inp)
    else:
        print('out')
#x=no.of.years,y=salary
if __name__ == '__main__':
    print("1.custom input \n 2.Manual Input")
    
    k = int(input("Enter the input('1'or'2')"))
    if k==1:
        Wages = {'x':[29,9,10,38,16,26,50,10,30,33,43,2,39,15,44,29,41,15,24,50],
        'y': [65000, 7000, 8000, 76000, 23000, 56000, 100000, 3000, 74000, 48000, 73000, 5000, 62000, 37000, 74000, 40000, 90000, 42000, 50000, 100000]}
        Wage= pd.DataFrame(data=Wages)
        n=len(Wage)
        x= Wage.x
        y= Wage.y
        plt.xlabel('Year of Work')
        plt.ylabel('Salary')
        plt.title('Linear Regression')
        plt.plot(x,y,'g^')
        cal(x,y)
    elif k==2:
        n = int(input("Enter the number of tuples:"))
        Wages = {'x':np.array(list(map(int,input("X:").split()))[:n]) ,'y':np.array(list(map(int,input("X:").split()))[:n])}
        Wage= pd.DataFrame(data=Wages)
        x= Wage.x
        y= Wage.y
        plt.xlabel('Year of Work')
        plt.ylabel('Salary')
        plt.title('Linear Regression')
        plt.plot(x,y,'g^')
        cal(x,y)
    else:
        print("Entered Wrongone")
        
      



 
