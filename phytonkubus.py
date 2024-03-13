# -*- coding: utf-8 -*-
"""phytonkubus

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15jls5nHuFxt4F-1U1yBzgiI1wXSrVxtA

Kalkulator Kubus
"""

from google.colab import drive
drive.mount('/content/drive')

# Definisi fungsi untuk menghitung luas permukaan, volume, dan keliling kubus

def luas_permukaan_kubus(sisi):
    return 6 * sisi**2

def volume_kubus(sisi):
    return sisi**3

def keliling_kubus(sisi):
    return 12 * sisi

# Contoh penggunaan fungsi dengan sisi kubus = 5
sisi_kubus = 5

luas = luas_permukaan_kubus(sisi_kubus)
volume = volume_kubus(sisi_kubus)
keliling = keliling_kubus(sisi_kubus)

print(f"Luas Permukaan Kubus: {luas} satuan persegi")
print(f"Volume Kubus: {volume} satuan kubik")
print(f"Keliling Kubus: {keliling} satuan panjang")