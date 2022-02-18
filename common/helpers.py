import numpy as np
from common.config import config

class Helpers:
    def __init__(self):
        pass
    def fun(x, y):
        """compute the value of f(x,y) at a given point

        :param x: point x(0,1,...n) in R
        :param y: point y(0,1,...n) in R
        :return: value of function at a given point x,y
        """
        expr = config()['function_expr']
        return eval(expr)

    def gradientVector(x,y):
        """compute the gradient of f(x,y) at a given point

        :param x: point x(0,1,...n) in R
        :param y: point y(0,1,...n) in R
        :return: partial derivatives for gradient vector (direction of steepest ascent) at a given point x,y
        """
        
        d_expr_x = config()['derivative_wrt_x']
        d_expr_y = config()['derivative_wrt_y']
        return eval(d_expr_x), eval(d_expr_y)
    
    def getGridBounds(x0,y0):
        """generate values around x0,y0 to plot on grid

        :param x0: number in R
        :param y0: number in R
        :return: grid x,y bounds
        """
        max_x0y0 = max(x0,y0) #We want to create grids around the max of x0 and y0 to ensure both values can be represented on the graph
        x = y = np.arange(-max_x0y0-1, max_x0y0+1, 0.5)
        return x, y