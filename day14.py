inp = """6 WBVJ, 16 CDVNK => 2 PJBZT
135 ORE => 8 MWDXJ
27 NBRHT, 2 NSWK, 2 CMHMQ, 29 NFCB, 11 KNGJ, 12 MGCKC, 56 NHTKL, 7 WNFSV => 1 FUEL
1 SFJFX, 3 MXNK => 4 NLSBZ
2 PFKRW, 1 VXFRX, 22 QDJCL => 6 GBDG
7 TSTF, 4 ZLJN => 7 DMWS
5 KPCF, 1 DLMDJ, 1 FNWGH => 6 TSTF
8 DTWKS, 1 GBDG => 4 CGZQ
26 CNWZM, 4 KPCF => 3 DTWKS
1 JVLHM, 7 DTWKS, 7 PJBZT => 8 MRPHV
2 MWDXJ => 3 VHFPC
1 WXNW, 6 PFKRW => 7 ZVGVP
2 ZVGVP => 1 CMHMQ
8 JVLHM, 11 XRKN, 1 HCGKZ => 8 CHZLX
20 TSTF => 4 XDZMZ
3 CMHMQ, 7 ZVGVP, 10 XRKN => 9 FNWGH
12 HCGKZ, 4 NLSBZ, 15 RWRDP, 4 MRPHV, 31 KRDV, 6 PMXK, 2 NFVZ => 7 KNGJ
1 TXZCM => 9 BMPJ
2 ZFXQ => 3 NBRHT
13 JVLHM, 1 VHFPC => 3 PBJPZ
7 HCGKZ => 7 PMXK
2 RWRDP, 3 VSTQ, 12 PMXK => 7 MXNK
1 PJBZT, 3 QRSK => 1 KRDV
1 MGCKC, 6 CMHMQ => 6 PQTVS
1 TNHCS, 24 ZLJN => 4 RWRDP
5 MWDXJ, 1 WXNW => 9 QBCLF
1 ZFXQ, 1 DLMDJ => 4 DJXRM
1 ZFXQ => 2 CNWZM
1 KPCF => 6 ZXDVF
2 MRPHV => 1 GSTG
5 BMPJ, 2 ZLJN => 8 XQJZ
1 MWDXJ, 1 ZVGVP => 3 CDVNK
3 NFCB, 3 CMHMQ, 1 MWDXJ => 4 XRKN
1 WXNW, 1 TXZCM => 5 ZLJN
4 ZXDVF => 4 WBVJ
2 GBDG => 4 KPCF
4 CHZLX, 7 ZFXQ, 14 PQTVS => 9 VSTQ
3 TXZCM, 7 ZLJN, 7 ZXDVF => 9 JVLHM
1 DMWS, 3 TSTF => 5 HCGKZ
2 CGZQ => 4 NFVZ
2 PQTVS, 9 VMNJ => 9 TXZCM
3 KPCF => 4 DLMDJ
7 VMNJ, 24 XQJZ, 7 GSTG, 8 NLSBZ, 10 MGCKC, 2 SFJFX, 18 BMPJ => 1 NSWK
41 CNWZM, 5 DJXRM, 1 QRSK, 1 KPCF, 15 XDZMZ, 3 MRPHV, 1 NLSBZ, 9 KRDV => 2 WNFSV
10 PBJPZ, 29 BMPJ, 2 PMXK => 7 SFJFX
116 ORE => 4 WXNW
2 CNWZM => 2 TNHCS
10 QBCLF => 7 NFCB
1 QBCLF => 2 ZFXQ
15 ZLJN => 7 QRSK
183 ORE => 3 QDJCL
11 GBDG => 5 VMNJ
4 DMWS, 3 QRSK => 3 NHTKL
124 ORE => 6 VXFRX
1 MWDXJ => 6 MGCKC
108 ORE => 9 PFKRW"""

# inp = """9 ORE => 2 A
# 8 ORE => 3 B
# 7 ORE => 5 C
# 3 A, 4 B => 1 AB
# 5 B, 7 C => 1 BC
# 4 C, 1 A => 1 CA
# 2 AB, 3 BC, 4 CA => 1 FUEL"""

# inp = """157 ORE => 5 NZVS
# 165 ORE => 6 DCFZ
# 44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
# 12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
# 179 ORE => 7 PSHF
# 177 ORE => 5 HKGWZ
# 7 DCFZ, 7 PSHF => 2 XJWVT
# 165 ORE => 2 GPVTF
# 3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

# inp = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
# 17 NVRVD, 3 JNWZP => 8 VPVL
# 53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
# 22 VJHF, 37 MNCFX => 5 FWMGM
# 139 ORE => 4 NVRVD
# 144 ORE => 7 JNWZP
# 5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
# 5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
# 145 ORE => 6 MNCFX
# 1 NVRVD => 8 CXFTF
# 1 VJHF, 6 MNCFX => 4 RFSQX
# 176 ORE => 6 VJHF"""

from fractions import Fraction
from math import ceil

eqs = inp.split('\n')
eqs = [e.split("=>") for e in eqs]
eqs = [ ([e.split() for e in l.strip().split(",")], r.strip().split()) for l, r in eqs]

reveqs = {}

for l, r in eqs:
    base = r[0]
    reveqs[r[1]] = [(int(base), Fraction(c)/Fraction(base), el) for c, el in l]
    # reveqs[r[1]] = [(int(base), int(c), el) for c, el in l]

print(reveqs)

stonks = {}

def count(elem, n):
    if elem == "ORE":
        return n
    comp = reveqs[elem]
    base = comp[0][0]
    acc = 0
    if elem in stonks:
        print("stonks", stonks[elem])
        n -= stonks[elem]
        stonks[elem] = 0

    if n % base != 0:
        oldn = n
        n += base
        n -= (n % base)
        stonks[elem] = n - oldn

    print(elem)
    # for base, c, el in comp:
    acc = sum(((count(el, c*n)) for base, c, el in comp))
    print(elem, n, acc)
    return acc

tril = 1000000000000
old = 0
fuel = 10**12//248794
diff = 248794
while True:
    cost = count("FUEL", fuel)
    if old == fuel:
        break
    old = fuel
    fuel += (tril - cost)//248794
    odiff = diff
    diff = fuel - old

while True:
    cost = count("FUEL", fuel)
    if cost > tril:
        break
    old = fuel
    fuel += 1
    odiff = diff
    diff = fuel - old

print(old)
