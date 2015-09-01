my_list=[]
my_hobby=['eat','dahar','makan','mangan','kumpul']
print "my first hobby is {0} and the second is {1}". format (my_hobby[0], my_hobby[4])
print "my first hobby is {} and the second is {}". format (my_hobby[0], my_hobby[4])
print "my first hobby is {satu} and the second is {dua}". format (satu=my_hobby[0], dua=my_hobby[4])
print "i have {} hobby". format (len(my_hobby))

for nama_var in my_hobby:
    print nama_var
# nama variabel bisa diisi bebas

my_hobby.append('sleeping')
print my_hobby
# menambahkan list

tambah=raw_input("input a hobby :")
my_hobby.append(tambah)
print my_hobby
# input a hobby to append to the list

masuk=raw_input("input a hobby :")
my_hobby.insert(2, masuk)
print my_hobby
# index python selalu dimulai dari 0

print my_hobby.index('sleeping')
# mencari nomor index dengan string

my_hobby.remove('makan')
print my_hobby
# menghapus list makan dengan string

my_hobby.pop(1)
print my_hobby
# menghapus list dengan index

my_hobby.sort()
print my_hobby
# mengurutkan sesuai abjad

my_hobby.reverse()
print my_hobby
# membalikkan urutan
