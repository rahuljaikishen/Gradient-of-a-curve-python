import sympy as sym

def config():
    x , y = sym.symbols('x y')

    #we can change the f here to represent any f(x,y) continuos function where x,y belongs to RxR
    f = x**2*y-x*y**2 
    return {
        'function_expr': str(f),
        'derivative_wrt_x': str(f.diff(x)), #On differentiating w.r.t x we get 2xy - y²
        'derivative_wrt_y': str(f.diff(y)) #On differentiating w.r.t y we get x² - 2xy
    }
