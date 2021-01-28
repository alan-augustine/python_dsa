"""
polynomial(1,2,3,4) = x^3 + 2x^2 + 3x + 4
derivative = dx/dy = 3x^2 + 4x + 3
display/printing is not perfect (eg: for polynomial(100) ):
 can be tweaked further
"""
def polynomial(*p):
    l = len(p)
    i = 1
    # dx/dy of a const. is zero, so ignore last element
    for i in range(len(p)-1):
        coeff = p[i]*(l-i-1)

        # for last element, no need to print 'x^0'
        if i == l - 2:
            e = ''
            x_pow = ''
            pow = ''
        else:
            e = ' + '
            x_pow = 'X^'
            pow = str(l -i - 2)
            
        print(str(coeff)+x_pow+ pow,end=e)
    print()
polynomial(1, 2, 3, 4)
polynomial(5, 4, 3, 2, 1)
polynomial(100)
polynomial(100,1)