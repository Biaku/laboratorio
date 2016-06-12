import csv


with open('media/csv/archivo_4n04SCQ.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    mail = 'tavo_x99@hotmail.com'
    for row in reader:
        if row[0] == mail:
            print('el usuario ya existe === >' + row[0])
            print('\t obteniendo el id del usuario')
            print('\t insertando nombre de pdf ===> ' + row[3])

        else:
            print('el usuario no existe ===>' + row[0])
            print('\t creando usuario')
            print('\t nombre de usuario ===>' + row[0])
            print('\t contraseña de usuario ===>' + row[1])
            print('\t insertando nombre de paciente ===> ' + row[2])
            print('\t obteniendo el id del usuario')
            print('\t insertando nombre de pdf ===> ' + row[3])