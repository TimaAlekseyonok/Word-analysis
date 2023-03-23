glas = ['а', 'у', 'е', 'ы', 'о', 'э', 'я', 'и', 'ю', 'ё']
sogl = ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ',
        'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'x', 'ч', 'с',
        'м', 'т', 'ь', 'б']

a = input('Введите слово: ')
a = a.lower()
print('Это слово включает в себя ', len(a), 'символов')

glasn_v_slove = []
sogl_v_slove = []
neopozn = []

for g in a:
    if g in glas:
        glasn_v_slove.append(g)

print('Гласные в этом слове: ', glasn_v_slove, ', ', 'их количество: ', len(glasn_v_slove))

for s in a:
    if s in sogl:
        sogl_v_slove.append(s)

print('Согласные в этом слове: ', sogl_v_slove, ', ', 'их количество: ', len(sogl_v_slove))

for x in a:
    if x not in glas and x not in sogl:
        neopozn.append(x)

print('Неопознанные символы в этом слове: ', neopozn, ', ', 'их количество: ', len(neopozn))