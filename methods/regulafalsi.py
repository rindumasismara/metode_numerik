from sympy import sympify, lambdify, Symbol

def regulafalsi_method(f_expr_str, a, b, tol, max_iter=100):
    x = Symbol('x')
    f_expr = sympify(f_expr_str)
    f = lambdify(x, f_expr, modules=['numpy'])

    if f(a) * f(b) > 0:
        return None, "Fungsi tidak memenuhi syarat: f(a) * f(b) < 0", []

    iterasi = []
    for i in range(1, max_iter + 1):
        fa = f(a)
        fb = f(b)
        c_new = (a * fb - b * fa) / (fb - fa)
        fc = f(c_new)

        iterasi.append({
            'i': i,
            'a': round(a, 6),
            'b': round(b, 6),
            'c': round(c_new, 6),
            'fa': round(fa, 6),
            'fb': round(fb, 6),
            'fc': round(fc, 6),
        })

        if abs(fc) < tol:
            break

        if fa * fc < 0:
            b = c_new
        else:
            a = c_new

    return round(c_new, 6), None, iterasi
