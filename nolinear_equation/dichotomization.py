# dichotomization
import math

epsilon = 1e-5


def f(x):
    return 1 - x - math.sin(x)


def dichotomization(intv_beg_pnt, intv_end_pnt):
    x = (intv_beg_pnt + intv_end_pnt) / 2
    if intv_end_pnt - intv_beg_pnt > epsilon:  # not met accuracy
        if f(intv_beg_pnt) * f(x) <= 0:
            intv_end_pnt = x
        else:
            intv_beg_pnt = x
        dichotomization(intv_beg_pnt, intv_end_pnt)
    print(x)  # print x in adverse


intv_beg_pnt = 0
intv_end_pnt = 1
dichotomization(intv_beg_pnt, intv_end_pnt)
