from sympy import sympify, lambdify, Symbol
import numpy as np

def bisection_method(f_expr_str, a, b, tol, max_iter=100):
    x = Symbol('x')
    f_expr = sympify(f_expr_str)
    f = lambdify(x, f_expr, modules=['numpy'])

    if f(a) * f(b) > 0:
        return None, "Fungsi tidak memenuhi syarat: f(a) * f(b) < 0", []

    iterasi = []
    i = 0
    c_mid = None
    while abs(b - a) > tol and i < max_iter:
        c_mid = (a + b) / 2.0
        fa = f(a)
        fb = f(b)
        fc = f(c_mid)
        iterasi.append({
            'i': i + 1,
            'a': round(a, 6),
            'b': round(b, 6),
            'c': round(c_mid, 6),
            'fa': round(fa, 6),
            'fb': round(fb, 6),
            'fc': round(fc, 6),
        })
        if abs(fc) < tol:
            break
        elif fa * fc < 0:
            b = c_mid
        else:
            a = c_mid
        i += 1

    return round(c_mid, 6), None, iterasi
