from sympy import sympify, diff, lambdify, Symbol

def newton_raphson_method(f_expr_str, x0, tol=1e-5, max_iter=100):
    x = Symbol('x')
    try:
        f_expr = sympify(f_expr_str)
        f = lambdify(x, f_expr, modules=['numpy'])
        df_expr = diff(f_expr, x)
        df = lambdify(x, df_expr, modules=['numpy'])
    except:
        return None, "Fungsi tidak valid.", []

    iterasi = []
    for i in range(1, max_iter + 1):
        try:
            fx = f(x0)
            dfx = df(x0)
            if dfx == 0:
                return None, "Turunan sama dengan nol. Tidak bisa lanjut.", []
            x1 = x0 - fx / dfx
            error = abs(x1 - x0)
        except:
            return None, "Terjadi kesalahan dalam evaluasi fungsi.", []

        iterasi.append({
            'i': i,
            'x0': round(x0, 6),
            'f_x0': round(fx, 6),
            'df_x0': round(dfx, 6),
            'x1': round(x1, 6),
            'error': round(error, 6)
        })

        if error < tol:
            break

        x0 = x1

    return x1, None, iterasi
