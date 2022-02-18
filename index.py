import numpy as np
import matplotlib.pyplot as plt
import random
from common.helpers import Helpers

def userInput():
    """Prompt user to enter coordinates of a point in R²
        :return: x0,y0
    """
    print('Bonjour! This program is written to calculate the gradient of f(x,y) = x²y - xy² at a given point.')
    print('Please enter numeric values as prompted')
    valid_inputs = 0
    while(valid_inputs < 2): 
        if valid_inputs == 0 : #Loop to take user inputs until two numeric inputs received
            x=input('Please enter the x co-ordinate value: ')
            try:
                x0 = float(x)
                valid_inputs = valid_inputs+1
            except ValueError:
                print("Please enter a value for x from the domain R")
                continue
        elif valid_inputs == 1 :
            y=input('Please enter the y co-ordinate value: ')
            try:
                y0 = float(y)
                valid_inputs = valid_inputs+1
            except ValueError:
                print("Please enter a value for y from the domain R")
                continue
    return x0,y0

def calculateGradient(x0,y0):
    """compute the gradient of f(x,y) at a given point x0,y0
        :param x0: user input x co-ordinate
        :param y0: user input y co-ordinate
        :return: gradient at x0, y0
    """
    gradient=[]
    g0=Helpers.gradientVector(x0,y0) #Getting the gradient at point x0,y0
    return g0

def plotFigure(x0,y0,g0):
    """Plot the function, 
       Plot the gradient vectors of that function
       Plot the gradient vector at user defined co-ordinate of that function
    """
    x,y = Helpers.getGridBounds(x0,y0)
    X, Y = np.meshgrid(x, y) #creating plotting points for the grid
    zs = np.array([Helpers.fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))]) #computing values for z
    Z = zs.reshape(X.shape)

    #creating figure and subplots
    fig = plt.figure(figsize=(20,15))


    #subplot to map function
    ax = fig.add_subplot(2,2,1, projection='3d')  
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(x,y) = x²y - xy²')
    ax.set_title('f(x,y) = x²y - xy²',fontdict={'fontsize': 20, 'fontweight': 'medium'})
    ax.plot_surface(X, Y, Z)
    
    #subplot to map gradient vector field
    bx = fig.add_subplot(2,2,2)
    bx.set_xlabel('X')
    bx.set_ylabel('Y')
    bx.set_title('Gradient at ('+str(x0)+','+str(y0)+')',fontdict={'fontsize': 20, 'fontweight': 'medium'})


    #Calculating gradients on the curve
    gradient_x = []
    gradient_y = []
    for x1,y1 in zip(np.ravel(X), np.ravel(Y)):
        gx1, gy1= Helpers.gradientVector(x1,y1)
        gradient_x.append(gx1)
        gradient_y.append(gy1)
    
    bx.quiver(X, Y, gradient_x, gradient_y,units='width',pivot='tip', color='blue') #Adding gradient vectors at different points on the curve
    bx.quiver(x0, y0, g0[0], g0[1],units='width',pivot='tip', color='green') #Adding gradient vector for the co-ordinate provided by the user
    bx.set_aspect('equal')
    plt.show()



x0,y0 = userInput()
g0 = calculateGradient(x0,y0)
print('Gradient for f(x,y) = x²y - xy² at ',x0,',',y0,' is ',g0)
plotFigure(x0,y0,g0)
