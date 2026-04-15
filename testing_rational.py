import rational as r


#nums1 = int(input())
#ens1 = int(input())
#nums2 = int(input())
#dens2 = int(input())

#k = r.create(nums1, dens1)
#n = r.create(nums2, dens2)

#r.add(k, n)
s = r.create(1, 2)
f = r.create(5, 7)



assert r.create(1, 0) == None
comparison = r.create(17, 14)
summ = r.add(s, f)
print(summ.numer)
assert r.compare(summ, comparison) == 0


