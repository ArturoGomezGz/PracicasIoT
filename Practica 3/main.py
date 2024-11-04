import RPi.GPIO as GPIO
import time
import mysql.connector

# Conexión a la base de datos MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="IoT"
)
mycursor = mydb.cursor()

# Configuración de los pines
GPIO_TRIGGER = 4  # Pin conectado a Trig
GPIO_ECHO = 17    # Pin conectado a Echo

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def medir_distancia():
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.5)
    
    # Generar el pulso en el pin Trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    # Calcular el tiempo de inicio y fin del pulso
    inicio_pulso = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        inicio_pulso = time.time()
    
    fin_pulso = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        fin_pulso = time.time()
    
    # Calcular la distancia en cm
    duracion = fin_pulso - inicio_pulso
    distancia = duracion * 17150
    distancia = round(distancia, 2)
    
    # Imprimir y retornar la distancia
    print(f"Distancia: {distancia} cm")
    return distancia

try:
    while True:
        dist = medir_distancia()
        
        # Insertar la distancia en la base de datos
        sql = "INSERT INTO distancia (distancia) VALUES (%s)"
        val = (dist,)
        mycursor.execute(sql, val)
        mydb.commit()
        
        # Espera de 1 segundo antes de la siguiente medición
        time.sleep(1)

except KeyboardInterrupt:
    print("Medición detenida por el usuario.")
finally:
    GPIO.cleanup()
    mydb.close()
