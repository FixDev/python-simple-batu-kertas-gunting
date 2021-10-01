from random import randint

choises = ['Batu', 'Kertas', 'Gunting']

computer = choises[randint(0, 2)]

player = False

while player == False:

    player = input("Batu, Kertas, Gunting? ")
    if player == computer:
        print('Yah Serii:(')
    elif player == "Batu" and computer == 'Kertas':
        print('Kamu Kalah', computer, 'Menggulung', player)
    elif player == "Batu" and computer == 'Gunting':
        print('Kamu Menang', player, 'Menghancurkan', computer)
    elif player == "Kertas" and computer == 'Gunting':
        print('Kamu Kalah', computer, 'Memotong', player)
    elif player == "Kertas" and computer == 'Batu':
        print('Kamu Menang', computer, 'Menggulung', player)
    elif player == "Gunting" and computer == 'Batu':
        print('Kamu Kalah', computer, 'Menghancurkan', player)
    elif player == "Gunting" and computer == 'Kertas':
        print('Kamu Menang', computer, 'Dipotong', player)
    else:
        print('Sepertinya kamu salah input:(')

    player = True
    computer = choises[randint(0, 2)]
