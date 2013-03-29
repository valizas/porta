def dv(ci):
        ci = list(str(ci))

        dvs = [4, 3, 6, 7, 8, 9, 2][:len(ci)] # precisamos tantos digitos verif. como digitos tiene la ci
        dvs.reverse()
    
        sum = reduce(lambda x, y: x+y, map(lambda x, y: int(x)*y, ci, dvs))

        sum %= 10

        return str( (10-sum) % 10 )

print "3856766", dv(3856766)
print "2635590", dv(2635590)
print "811455", dv(811455)
print dv(3034273)
