'''
Assalamualaikum wr wb, dalam rangka menyambut kedatangan bulan suci Ramadhan 1444 H
saya akan mencoba membuat snake game dengan python tkinter, versi saya
selamat menyaksikan dan semoga bermanfaat
ASMR
seperti ini tampilannya
'''

import random
from tkinter import *

# konstanta
heigh=400
width=400
size=20
part=3
x=0
y=0
objek=[] #menampung koordinat ular
koor_makanan=[(width/2,heigh/2)] # awal game, posisi makanan ada di tengah



win=Tk()
win.title('Snake Game by Jefri')

canva=Canvas(win,heigh=heigh,width=width,bg='yellow')
canva.pack()

# membuat makanannya
makanan=canva.create_rectangle(koor_makanan[0][0]+size,koor_makanan[0][1]+size,koor_makanan[0][0],koor_makanan[0][1],fill='green',tag='makanan')

# membuat ular awal
for i in range(part):
		objek.append([x,y+i*size])
		for a,b in objek:
			ular=canva.create_rectangle(a+size,b+size,a,b,fill='red',tag='ular')


# membuat fungsi jika makanan sudah dimakan, maka makanan akan muncul lagi di posisi random
def buat_makanan():
	x=random.randrange(0,width,size)
	y=random.randrange(0,heigh,size)
	# menghapus list koordinat makanan, dan memasukkan koordinat baru
	del koor_makanan[0]
	koor_makanan.append([x,y])
	makanan=canva.create_rectangle(koor_makanan[0][0]+size,koor_makanan[0][1]+size,koor_makanan[0][0],koor_makanan[0][1],fill='green',tag='makanan')



# membuat fungsi ketika ular bertemu makanan, maka panjang ular bertambah 1 dan makanan hilang
def dapat_makan():
	a=koor_makanan[0][0]
	b=koor_makanan[0][1]
	for c,d in objek:
		if c==a and d==b: #ketika koordinat ular dan makanan sama
			#mengambil koordinat dua badan ular terakhir
			x,y=objek[-1]
			g,h=objek[-2]
			if x==g:
				objek.append([x,y+size]) # kalau arah badan ular terakhir vertikal maka penambahan juga vertikal
			if y==h:
				objek.append([x+size,y]) # kalau arah badan ular horizontal, maka penambahan juga horizontal
			canva.delete('makanan') # makanan dihapus


# fungsi untuk mengatur jalan si ular
def arah(sb_x,sb_y):
	# memasukkan membuat makanan baru
	# cek jika makanan sudah hilang, maka buat baru
	if len(canva.find_withtag('makanan'))==0:
		buat_makanan()
	del objek[0]
	x,y=objek[-1]
	objek.append([x+sb_x,y+sb_y])
	canva.delete('ular')
	for a,b in objek:
		ular=canva.create_rectangle(a+size,b+size,a,b,fill='red',tag='ular')
	# memasukkan fungsi dapat makaanan disini
	dapat_makan()



# mengatur arah menggunakan keyboard
win.bind('<Down>',lambda event:arah(0,size))
win.bind('<Up>',lambda event:arah(0,-size))
win.bind('<Right>',lambda event:arah(size,0))
win.bind('<Left>',lambda event:arah(-size,0))

win.mainloop()

# Alhamdulillah, semoga bermanfaat dan selamat menunaikan ibadah puasa
# source code ada di deskripsi, insyaAllah
