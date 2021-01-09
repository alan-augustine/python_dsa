def check_if_satisfies_formulas(a, b, c):
    if a+b == c:
        print("a={0}, b={1}, c={2} satisfies a+b = c".format(a, b, c))
    if a == b-c:
        print("a={0}, b={1}, c={2} satisfies a = b-c".format(a, b, c))
    if a*b == c:
        print("a={0}, b={1}, c={2} satisfies a*b = c".format(a, b, c))

check_if_satisfies_formulas(1, 2, 3)
check_if_satisfies_formulas(1, 3, 2)
check_if_satisfies_formulas(1, 2, 2)
check_if_satisfies_formulas(1, 10, 100)
