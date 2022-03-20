ujian_teori=float(input("Nilai Ujian Teori: "))
ujian_praktik=float(input("Nilai Ujian Praktik: "))

if ujian_teori>=70.0 and ujian_praktik>=70.0:
	print("Selamat, anda lulus!")
elif ujian_teori>=70.0 and ujian_praktik<=70.0:
	print("Anda harus mengulang ujian praktik")
elif ujian_teori<=70.0 and ujian_praktik>=70.0:
	print("Anda harus mengulang ujian teori")
else:
	print("Anda harus mengulang kedua ujian tersebut")