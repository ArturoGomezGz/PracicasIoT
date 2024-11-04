import RPi.GPIO as GPIO
import time
import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="password",
 database="IoT"
)
mycursor = mydb.cursor()

# ConfiguraciÃƒÂ³n de los pines
GPIO_TRIGGER = 4  # Pin conectado a Trig
GPIO_ECHO = 17    # Pin conectado a Echo

# ConfiguraciÃƒÂ³n de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def medir_distancia():
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.5)
    
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    inicio_pulso = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        inicio_pulso = time.time()
    
    fin_pulso = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        fin_pulso = time.time()
    
    duracion = fin_pulso - inicio_pulso
    distancia = duracion * 17150
    return round(distancia, 2)

    print(f"Distancia: {dist} cm")
    time.sleep(1)


    GPIO.cleanup()


medir_distancia()

mycursor.execute("SELECT * FROM distancia")
myresult = mycursor.fetchall()
print(myresult)

