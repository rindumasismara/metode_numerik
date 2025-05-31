from sympy import sympify, lambdify, Symbol

def secant_method(f_expr_str, x0, x1, tol=1e-5, max_iter=100):
    x = Symbol('x')
    try:
        f_expr = sympify(f_expr_str)
        f = lambdify(x, f_expr, modules=['numpy'])
    except:
        return None, "Fungsi tidak valid.", []

    iterasi = []
    for i in range(1, max_iter + 1):
        try:
            fx0 = f(x0)
            fx1 = f(x1)
            if fx1 - fx0 == 0:
                return None, "Terjadi pembagian dengan nol.", []
            x_temp = x1 - (fx1 * (x0 - x1)) / (fx0 - fx1)
            error = abs(x_temp - x1)
        except:
            return None, "Kesalahan dalam evaluasi fungsi.", []

        iterasi.append({
            'i': i,
            'x0': round(x0, 6),
            'x1': round(x1, 6),
            'x_temp': round(x_temp, 6),
            'f_x1': round(fx1, 6),
            'error': round(error, 6)
        })

        if error < tol:
            break

        x0, x1 = x1, x_temp

    return x_temp, None, iterasi
