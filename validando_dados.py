

print('\033[1;36m')
genero = 0
while genero != "M" and genero != "F":
    genero = str(input("Digite seu sexo [M/F]: ")).upper()

    if genero != "M" and genero != "F":
        print("\033[1;31mGenero invalidado!")

    elif genero == "M":
        print('\033[1;32mGenero Validado, obrigado!')

    else:
        print("\033[1;35mGenero Validado, obrigada!")

        


