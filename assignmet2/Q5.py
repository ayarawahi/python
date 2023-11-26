a=[23, 54, 76, 12, 90]

out=""
for i in a:
    out+=str(i)+'|'
out=out.rstrip('|')
print(out)