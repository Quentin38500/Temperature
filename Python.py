import serial
import time
import datetime
import gspread


x = 1
while x < 2 :
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json',scope)
    client = gspread.authorize(creds)
    sheet = client.open('Température').sheet1
    
    serial_port = serial.Serial(port = "COM3" , baudrate =115200)
    # réinitialisation
    serial_port.setDTR( False )
    time.sleep (0.1)
    serial_port.setDTR(True )
    # on vide le buffer
    serial_port.flushInput ( )
    # lecture des données
    liste = []
    for i in range (10) :
        liste.append(serial_port.readline ( ) )
    serial_port.close ( )
    a = liste[5]
    b = a.decode("utf-8")
    c = b[:-3]
    d = float(c)
    #sheet.delete_row(1)
    date = datetime.datetime.now()
    sheet.insert_row([d,str(date.hour)+":"+str(date.minute)+":"+str(date.second)+"   "+str(date.day)+"/"+str(date.month)+"/"+str(date.year),time.time()])
    time.sleep(60)