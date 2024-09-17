from prettytable import PrettyTable


def zhakobi(x,y,z):

    x1 = (-3/4)*y+6
    y1 = (-3/4)*x+(1/4)*z+(15/2)
    z1 = (1/4)*y-6

    x2 = (-3 / 4) * y1 + 6
    y2 = (-3 / 4) * x1 + (1 / 4) * z1 + (15 / 2)
    z2 = (1 / 4) * y1 - 6

    x3 = (-3 / 4) * y2 + 6
    y3 = (-3 / 4) * x2 + (1 / 4) * z2 + (15 / 2)
    z3 = (1 / 4) * y2 - 6

    x4 = (-3 / 4) * y3 + 6
    y4 = (-3 / 4) * x3 + (1 / 4) * z3 + (15 / 2)
    z4 = (1 / 4) * y3 - 6

    x5 = (-3 / 4) * y4 + 6
    y5 = (-3 / 4) * x4 + (1 / 4) * z4 + (15 / 2)
    z5 = (1 / 4) * y4 - 6

    x6 = (-3 / 4) * y5 + 6
    y6 = (-3 / 4) * x5 + (1 / 4) * z5 + (15 / 2)
    z6 = (1 / 4) * y5 - 6

    x7 = (-3 / 4) * y6 + 6
    y7 = (-3 / 4) * x6 + (1 / 4) * z6 + (15 / 2)
    z7 = (1 / 4) * y6 - 6

    x8 = (-3 / 4) * y7 + 6
    y8 = (-3 / 4) * x7 + (1 / 4) * z7 + (15 / 2)
    z8 = (1 / 4) * y7 - 6

    x9 = (-3 / 4) * y8 + 6
    y9 = (-3 / 4) * x8 + (1 / 4) * z8 + (15 / 2)
    z9 = (1 / 4) * y8 - 6

    x10 = (-3 / 4) * y9 + 6
    y10 = (-3 / 4) * x9 + (1 / 4) * z9 + (15 / 2)
    z10 = (1 / 4) * y9 - 6



    table = PrettyTable(['k','x', 'y', 'z'])

    table.add_row([0,x, y, z])

    table.add_row([1, x1, y1, z1])

    table.add_row([2, x2, y2, z2])

    table.add_row([3, x3, y3, z3])

    table.add_row([4, x4, y4, z4])

    table.add_row([5, x5, y5, z5])

    table.add_row([6, x6, y6, z6])

    table.add_row([7, x7, y7, z7])

    table.add_row([8, x8, y8, z8])

    table.add_row([9, x9, y9, z9])

    table.add_row([10, x10, y10, z10])

    print(table)


zhakobi(0,0,0)








