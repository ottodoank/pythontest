print("pilih ruangan yang anda ingin masuki, pintu 1 atau pintu 2")
pintu=input("masukkan pilihan anda: ")
if pintu==1:
    print"selamat datang di pintu 1, silahkan pilih 3 pilihan"
    print"1. fak"
    print"2. dem"
    print"3. sit"
    satu=input("PILIH salah satu pilihan diatas!!!  : ")
    if satu==1:
        print"anda itu fak!"
    elif satu==2:
        print"anda itu dem!"
    elif satu==3:
        print"anda itu sit!"
if pintu==2:
    print"selamat datang di pintu 2, silahkan pilih 2 pilihan"
    print"1. krik"
    print"2. kruk"
    satu=input("PILIH salah satu pilihan diatas!!!  : ")
    if satu==1:
        print"anda itu krik!"
    elif satu==2:
        print"anda itu kruk!"
print("DONE")
