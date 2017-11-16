arv1 = int(input("Sisestage arv:  "))
arv2 = int(input("Sisestage arv:  "))
arvud = [arv1, arv2]
print(arvud)
print('Paarisarvud nende arvude vahel on:')
for x in range(arv1, arv2):
    if (x%2 == 0):
        print(x)

fname = "kttekst.txt"

num_lines = 0
num_words = 0
num_chars = 0
num_smaller = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        
        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
    for smaller in words:
        if len(smaller) < 5:
            num_smaller += len(smaller)
print('Tekstis on nii palju sõnu:')
print(num_words)
print('Tekstis on sõnu väiksemaid kui 5 tähte:')
print(num_smaller)

List1 = [11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24]
List2 = [5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 24, 18, 31, 7, 1, 7]
print('Kahe listi ühisosa on:')
for element in List1:
    if element in List2:
        print(element)

print('Suurim number on:')
suurim = List1 + List2
suurimnumber = max(suurim)
print(suurimnumber)

print('Väikseim number on:')
vnumber = min(suurim)
print(vnumber)

print('Esimese listi keskmine on:')
keskmine1 = sum(List1) / len(List1)
print(keskmine1)

print('Teise listi keskmine on:')
keskmine2 = sum(List2) / len(List2)
print(keskmine2)

print('Mõlema listi keskmine kokku on:')
mkeskmine = sum(suurim) / len(suurim)
print(mkeskmine)
