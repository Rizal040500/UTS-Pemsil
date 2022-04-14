import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def sigma1(inp, n):
    arr = []
    out = 0
    for x in range(n):
        arr.append(inp[x])
        out += arr[x]
    return out, arr

def sigma2(inpX, inpY, n):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inpX[x] * inpY[x]))
        out += arr[x]
    return out, arr

def sigpow1(inp, n):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inp[x] ** 2))
        out += arr[x]
    return out, arr

def cariA(inpX, inpY, inpN):
    Yi = sigma1(inpY, inpN)[0]
    Xi2 = sigpow1(inpX, inpN)[0]
    Xi = sigma1(inpX, inpN)[0]
    XiYi = sigma2(inpX, inpY, inpN)[0]
    out = round(((Yi * Xi2) - (Xi * XiYi))
                / ((inpN * Xi2) - (Xi ** 2)), 3)
    return out

def cariB(inpX, inpY, inpN):
    Yi = sigma1(inpY, inpN)[0]
    Xi = sigma1(inpX, inpN)[0]
    Xi2 = sigpow1(inpX, inpN)[0]
    XiYi = sigma2(inpX, inpY, inpN)[0]
    out = round(((inpN * XiYi) - (Xi * Yi))
                / ((inpN * Xi2) - (Xi ** 2)), 3)
    return out

def inputManual():
    # Input data manual
    x = []
    y = []
    n = int(input("Jumlah Data: "))
    print("Masukan X")
    for i in range(0, n):
        elementX = int(input("Data X: "))
        x.append(elementX)  # Memasukan data ke dalam array x

    print("\nMasukan Y")
    for i in range(0, n):
        elementY = int(input("Data Y: "))
        y.append(elementY)  # Memasukan data ke dalam array y
    return x, y, n

def inputCSV():
    # Input data dari CSV
    data = pd.read_csv("datasepatu.csv")
    X = data.columns[1]
    Y = data.columns[2]

    n = len(data)
    x = data[X]
    y = data[Y]
    return x, y, n

def hitungRegresi(x, y, n):
    # Menghitung Konstanta dan Koefisien
    a = cariA(x, y, n)
    b = cariB(x, y, n)
    print('Nilai Konstanta = ', a)
    print('Nilai Koefisien = ', b)
    print(f'Persamaan Y = {a} {b:+} X')

    # Percobaan user untuk memprediksi nilai Gradient
    inp = input("\nMasukan Nilai X (Berat badan): ")
    print(f'Y = {a} {b:+} * {inp} = {a + (b * int(inp)):.0f}')


    # Cetak scatter plot
    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def scatterFunc(x):
        return slope * x + intercept

    mymodel = list(map(scatterFunc, x))
    plt.title("Regresi Linear")
    plt.xlabel("Ukuran Sepatu")
    plt.ylabel("Berat Badan")
    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()


if __name__ == '__main__':
    menu = ""
    while menu != 0:
        # Pilihan menu perintah
        print("\nSilahkan Pilih Nomor Operasi yang Akan Dijalankan")
        print("1 = Input Data dari CSV"
              "\n2 = Input Data Manual"
              "\n0 = Keluar")
        menu = int(input("\nNomor Operasi yang Dipilih : "))
        if menu == 1:
            x, y , n = inputCSV()
            hitungRegresi(x, y , n)
        elif menu == 2:
            x, y , n = inputManual()
            hitungRegresi(x, y, n)
        elif menu == 0:
            print("Terimakasih & Sampai Jumpa")
        else:
            print("Nomor Tidak Terdaftar, Mohon Masukan Nomor Lain"
                  "\n1 = Input Data dari CSV"
                  "\n2 = Input Data Manual"
                  "\n0 = Keluar")



