import matplotlib.pyplot as plt
import pandas as pd
import CsvHandler as ch


def udskriv_graf(name):
    #print(df.head())
    df = pd.read_csv("Eksamen/temperaturer.csv", sep=";", encoding='utf8')
    ax = plt.gca()
    df = df[-5:]
    df.plot(kind='line', x='Nr', y=name, color='red', ax=ax)
    plt.show()
    menu()

def add_temp():
    nr = input("Indtast nummer: ")
    patient_1 = input("Niels Jensen: ")
    patient_2 = input("Jens Olsen: ")
    patient_3 = input("Bente Hansen: ")
    patient_4 = input("Mona Jensen: ")
    patient_5 = input("Lise Clausen: ")
    patient_6 = input("Kurt Andersen: ")

    before1 = str(ch.getRow("Eksamen/temperaturer",-1)).split(';')[1]

    after1 = patient_1

    before2 = str(ch.getRow("Eksamen/temperaturer",-1)).split(';')[2]

    after2 = patient_2

    before3 = str(ch.getRow("Eksamen/temperaturer",-1)).split(';')[3]

    after3 = patient_3

    before4 = str(ch.getRow("Eksamen/temperaturer",-1)).split(';')[4]

    after4 = patient_4

    before5 = str(ch.getRow("Eksamen/temperaturer",-1)).split(';')[5]

    after5 = patient_5

    before6 = str(ch.getRow("Eksamen/temperaturer",-1)).split(';')[6]

    after6 = patient_6

    if float(after1)-float(before1)  <= -1:
        print("Alarm - Patient 1")
    if float(after2)-float(before2)  <= -1:
        print("Alarm - Patient 2")
    if float(after3)-float(before3)  <= -1:
        print("Alarm - Patient 3")
    if float(after4)-float(before4)  <= -1:
        print("Alarm - Patient 4")
    if float(after5)-float(before5)  <= -1:
        print("Alarm - Patient 5")
    if float(after6)-float(before6.replace('\']', ""))  <= -1:
        print("Alarm - Patient 6")
        
    


    
    ch.insertRow("Eksamen/temperaturer", [nr, patient_1, patient_2, patient_3, patient_4, patient_5, patient_6], ";")
    
    menu()

def afslut():
    print("Tak for nu!")

def menu():
    print("Indtast dit valg (g = udskriv graf q = afslut a = tilføj temperatur)")
    valg = input("Indtast dit valg:")
    if (valg == 'g'):
        name = input("Indtast navn: ")
        udskriv_graf(name)
    if (valg == 'a'):
        add_temp()
    if (valg == 'q'):
        afslut()

menu()