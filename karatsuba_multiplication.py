def karatsuba(x,y):
	# check is the number x,y are of length 1
    # base case for the recursive calls
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        # get max number of digits in x or y and get its half
        n = max(len(str(x)),len(str(y)))
        nby2 = n // 2

        # split x,y into 2 parts (a,b) and (c,d) respectivly
        a = x // 10**(nby2)
        b = x % 10**(nby2)
        c = y // 10**(nby2)
        d = y % 10**(nby2)

        # compute a*c , b*d , (a*d + c*d) recursivly 
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_plus_bc = karatsuba(a+b,c+d) - ac - bd

        # writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
        return prod

karatsuba(1234,5678)        