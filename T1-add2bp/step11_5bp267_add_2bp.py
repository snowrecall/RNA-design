#/usr/bin/python

seq = 'GGGGAAGGGCAACUUUCUA'

add_bp = ['AU','UA','GC','CG','GU','UG']

for m in add_bp:
    for s in range(1,7):
        print seq[:s+1]+m[0]+seq[s+1:19-s]+m[1]+seq[19-s:19]


