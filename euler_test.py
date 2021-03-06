import big_o
from big_o import complexities as cmpl
import gnuplotlib as gp
import math
import numpy as np
import unittest
import warnings

import euler


class PruebasEuler(unittest.TestCase):

    def test_e_cuadratica(self):
        e = euler.e_cuadratica(1000)
        self.assertAlmostEqual(math.e, e)

    def test_compl_e_cuadratica(self):
        print()
        best, fitted = big_o.big_o(euler.e_cuadratica, big_o.datagen.n_, min_n=10, max_n=1000,
                                   n_measures=100, n_repeats=3, verbose=False, classes=[cmpl.Linear, cmpl.Quadratic, cmpl.Constant], return_raw_data=True)

        xs = fitted['measures']
        ys = fitted['times']
        gp.plot(xs, ys, _with='lines', terminal='dumb 60,30',
                unset='grid', title='e_cuadratica', xlabel='n', ylabel='T(n)')

        for k, v in fitted.items():
            if isinstance(k, big_o.complexities.ComplexityClass):
                residual = v
                r2 = 1 - residual / (ys.size * ys.var())
                print(k, f' (r={residual}, r^2={r2})')


        if not isinstance(best, big_o.complexities.Quadratic):
            warnings.warn(
                f'Complejidad esperada Cuadratica, complejidad estimada {best}')

    def test_e_lineal(self):
        e = euler.e_lineal(1000)
        self.assertAlmostEqual(math.e, e)

    def test_compl_e_lineal(self):
        print()
        best, fitted = big_o.big_o(euler.e_lineal, big_o.datagen.n_, min_n=10, max_n=1000,
                                   n_measures=100, n_repeats=3, verbose=False, classes=[cmpl.Linear, cmpl.Quadratic, cmpl.Constant], return_raw_data=True)

        xs = fitted['measures']
        ys = fitted['times']
        gp.plot(xs, ys, _with='lines', terminal='dumb 60,30',
                unset='grid', title='e_lineal', xlabel='n', ylabel='T(n)')

        for k, v in fitted.items():
            if isinstance(k, big_o.complexities.ComplexityClass):
                residual = v
                r2 = 1 - residual / (ys.size * ys.var())
                print(k, f' (r={residual}, r^2={r2})')

        if not isinstance(best, big_o.complexities.Linear):
            warnings.warn(
                f'Complejidad esperada Lineal, complejidad estimada {best}')
