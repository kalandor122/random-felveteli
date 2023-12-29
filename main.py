import subprocess
import os
import random
import time


feladat = 1 
évek = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
path_to_acrobat = os.path.abspath(r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe") 


feladatperoldal = {
    1 : 3,
    2 : 3,
    3 : 4,
    4 : 5,
    5 : 6,
    6 : 7,
    7 : 8,
    8 : 8,
    9 : 9,
    10 : 10
}

egy = []
kettő = []
három = []
négy = []
öt = []
hat = []
hét = []
nyolc = []
kilenc = []
tíz = []

forditó = {
    1: egy,
    2: kettő,
    3: három,
    4: négy,
    5: öt,
    6: hat,
    7: hét,
    8: nyolc,
    9: kilenc,
    10: tíz,
}

evek = [egy, kettő, három, négy, öt, hat, hét, nyolc, kilenc, tíz]
pontok = 0
start = time.perf_counter()

for i in range(10):
    a = random.choice(évek)
    forditó[i+ 1].append(a)
    path_to_pdf = os.path.abspath(rf'\felvételik\{a}.pdf')

    process = subprocess.Popen([path_to_acrobat, '/A', f'page={feladatperoldal[feladat]}', path_to_pdf], shell=False, stdout=subprocess.PIPE)
    
    b = input("Válasz: ")
    forditó[i+ 1].append(b)
    process.terminate()
    feladat += 1

end = time.perf_counter()
times = end - start

print(times / 60)


for i in range(10):
    print(evek[i])
    path_to_pdf = os.path.abspath(rf'\felvételik\megoldókulcs\{evek[i][0]}.pdf')
    process = subprocess.Popen([path_to_acrobat, '/A', "1", path_to_pdf], shell=False, stdout=subprocess.PIPE)
    print(forditó[i+1][1])
    pontok += int(input())
    process.terminate()


szalek = (pontok / 50)
print(szalek * 100)
print(times / 60)

