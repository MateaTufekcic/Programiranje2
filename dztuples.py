#Zadatak1
imena = ['Mario', 'Josip', 'Ivana', 'Mija', 'Ivan', 'Ante', 'Marino', 'Ana-Marija', 'Frano', 'Mladen', 'Marko', 'Jozo Matej', 'Karlo', 'Mate', 'Katarina', 'Tomislava', 'Alija', 'Sara', 'Petar', 'Safet', 'Matej', 'Stjepan', 'Ivan', 'Antonio', 'David', 'Ivan Entoni', 'Marija', 'Mate', 'Kristijan', 'Antonio', 'Ružica', 'Petar', 'Ana', 'Zvonimir', 'Matea', 'Petar', 'Miroslav', 'Matea', 'Marija', 'Marko', 'Antonio', 'Matej', 'Iva', 'Leonardo', 'Karlo', 'Josip', 'Ivan', 'Vice', 'Azer']
prezimena = ['Jonjić', 'Ćavar', 'Bunoza', 'Sabljić', 'Luetić', 'Šimić', 'Rupar', 'Bakula', 'Vranjković', 'Tomić', 'Benković', 'Lasić', 'Rezo', 'Penava', 'Galić', 'Đopa', 'Kičin', 'Budimir', 'Lončar', 'Srna', 'Knežević', 'Marić', 'Udovičić', 'Jakovljević', 'Grubišić', 'Bunoza', 'Krištić', 'Zeljko', 'Slišković', 'Bebek', 'Grgić', 'Ilišević', 'Šimić', 'Milardović', 'Tufekčić', 'Markić', 'Pinjuh', 'Bošnjak', 'Krištić', 'Ćubela', 'Mlikota', 'Kraljević', 'Šimović', 'Karačić', 'Bagarić', 'Jurković', 'Živković', 'Božić', 'Džemić']
bodovi = [100, 100, 100, 90, 80, 75, 60, 60, 55, 55, 55, 50, 50, 50, 50, 50, 50, 40, 35, 35, 30, 30, 25, 25, 20, 20, 20, 15, 15, 15, 15, 15, 10, 10, 10, 10, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0]

studenti=list(zip(imena,prezimena,bodovi))
for student in studenti:
    (ime, prezime, bodovi)= student
    if bodovi >= 50:
        print(ime, prezime, bodovi)
#DZ
sortirani_studenti=sorted(studenti, key=lambda x: x[1])

rjecnik = {
    'Nedovoljan': 0,
    'Dovoljan': 0,
    'Dobar': 0,
    'Vrlodobar': 0,
    'Izvrstan': 0
}

for student in studenti:
    bodovi = student[2]
    
    if bodovi >= 90:
        rjecnik['Izvrstan'] += 1
    elif bodovi >= 80:
        rjecnik['Vrlodobar'] += 1
    elif bodovi >= 65:
        rjecnik['Dobar'] += 1
    elif bodovi >= 50:
        rjecnik['Dovoljan'] += 1
    else:
        rjecnik['Nedovoljan'] += 1

print(rjecnik)

