from flask import Blueprint, render_template, request
from methods.bisection import bisection_method
from methods.regulafalsi import regulafalsi_method
from methods.fixedpoint import fixed_point_best
from methods.newtonraphson import newton_raphson_method
from methods.secant import secant_method

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/aturan')
def aturan():
    return render_template('aturan.html')

@main.route('/credit')
def credit():
    return render_template('credit.html')

@main.route('/bisection', methods=['GET', 'POST'])
def bisection():
    result = None
    error = None
    table = []

    if request.method == 'POST':
        func_str = request.form['function']
        a = float(request.form['a'])
        b = float(request.form['b'])
        tol = float(request.form['tolerance'])

        root, error, table = bisection_method(func_str, a, b, tol)
        if not error:
            result = root

    return render_template('bisection.html', result=result, error=error, table=table)

@main.route('/regulafalsi', methods=['GET', 'POST'])
def regulafalsi():
    result = None
    error = None
    table = []

    if request.method == 'POST':
        func_str = request.form['function']
        a = float(request.form['a'])
        b = float(request.form['b'])
        tol = float(request.form['tolerance'])

        root, error, table = regulafalsi_method(func_str, a, b, tol)
        if not error:
            result = root

    return render_template('regulafalsi.html', result=result, error=error, table=table)

@main.route('/fixedpoint', methods=['GET', 'POST'])
def fixedpoint():
    result = None
    best_label = None
    error = None
    all_tables = []

    if request.method == 'POST':
        func_str = request.form['function']
        tol = float(request.form['tolerance'])
        x0 = float(request.form['x0'])

        best, all_results = fixed_point_best(func_str, x0, tol)

        if not best:
            error = "Tidak ada kandidat g(x) yang berhasil konvergen dengan f(x) tersebut."
        else:
            result = best['final_root']
            best_label = best['label']
            all_tables = all_results

    return render_template('fixedpoint.html', result=result, best_label=best_label, error=error, all_tables=all_tables)

@main.route('/newtonraphson', methods=['GET', 'POST'])
def newtonraphson():
    result = None
    error = None
    table = []

    if request.method == 'POST':
        func_str = request.form['function']
        x0 = float(request.form['x0'])
        tol = float(request.form['tolerance'])

        root, error, table = newton_raphson_method(func_str, x0, tol)
        if not error:
            result = root

    return render_template('newtonraphson.html', result=result, error=error, table=table)

@main.route('/secant', methods=['GET', 'POST'])
def secant():
    result = None
    error = None
    table = []

    if request.method == 'POST':
        func_str = request.form['function']
        x0 = float(request.form['x0'])
        x1 = float(request.form['x1'])
        tol = float(request.form['tolerance'])

        root, error, table = secant_method(func_str, x0, x1, tol)
        if not error:
            result = root

    return render_template('secant.html', result=result, error=error, table=table)
