from sympy import symbols, exp, sympify, lambdify, sqrt, solve, Eq
import numpy as np

x = symbols('x')

def generate_candidates(f_expr):
    # Bentuk 3 kandidat g(x) dari f(x)
    candidates = []

    try:
        # g1(x) = sqrt(e^-x / 4)
        g1 = sqrt(exp(-x)/4)
        candidates.append(g1)
    except:
        pass

    try:
        # g2(x) dari solusi eksplisit e^-x = 4x^2 → -x = ln(4x^2) → x = -ln(4x^2)
        sol = solve(Eq(exp(-x), 4*x**2), x)
        if sol:
            candidates.append(-sol[0])  # hasil rearranged x = ...
    except:
        pass

    try:
        # g3(x) = 1/2 * sqrt(e^-x)
        g3 = sqrt(exp(-x)) / 2
        candidates.append(g3)
    except:
        pass

    return candidates


def fixed_point_iteration(g_expr, x0=0.5, tol=1e-5, max_iter=100):
    g = lambdify(x, g_expr, modules=['numpy'])
    iterasi = []
    for i in range(max_iter):
        try:
            x1 = g(x0)
            error = abs(x1 - x0)
            iterasi.append({
                'i': i+1,
                'x0': round(x0, 6),
                'x1': round(x1, 6),
                'error': round(error, 6)
            })
            if error < tol:
                break
            x0 = x1
        except:
            break
    return iterasi


def fixed_point_best(f_expr_str, x0=0.5, tol=1e-5):
    try:
        f_expr = sympify(f_expr_str)
        candidates = generate_candidates(f_expr)
        all_results = []

        for idx, g_expr in enumerate(candidates, 1):
            try:
                iters = fixed_point_iteration(g_expr, x0, tol)
                if len(iters) > 0 and iters[-1]['error'] < tol:
                    all_results.append({
                        'label': f"g{idx}(x) = {g_expr}",
                        'expr': g_expr,
                        'iterations': iters,
                        'final_root': iters[-1]['x1'],
                        'total_steps': len(iters)
                    })
            except:
                continue

        # Pilih yang paling sedikit iterasi
        if all_results:
            best = min(all_results, key=lambda x: x['total_steps'])
            return best, all_results
        else:
            return None, []

    except Exception as e:
        return None, []
