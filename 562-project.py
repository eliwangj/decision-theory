from scipy.misc import derivative

## The Newton's method
def newton(f, x0, tol):
    x = x0
    counter = 0

    while abs(f(x)) > tol:
        fx = f(x)
        dfx = derivative(f, x)
        x = x - (fx/dfx)
        counter += 1
        print("Iteration: {}; f(x): {}; x: {};".format(counter, f(x), x))

    print("The zero of the function g(x) using Newton's Method is x = {};\nThe initial start point is {}.".format(x, x0))

## Define the target function
def func(K):
    f = 0.001764*K**7 + 0.040173*K**6 + 0.34114*K**5 + 1.4647*K**4 + 3.508*K**3 + 4.75*K**2 + 2.4*K
    return f

## Display the results
tol = 1e-7
x0 = -1
newton(func, x0, tol)