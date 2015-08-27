kata= raw_input ("masukkan sebuah kata : ")
banyak= input ("loop kata sebanyak: ")
a=1
while (a<=banyak):
    print kata, "ke", a
    #print "{0} ke {1}". format(kata,loop)
    a=a+1
print ''
print "variable loop terakhir={0}". format(loop)
