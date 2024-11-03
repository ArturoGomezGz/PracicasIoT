import RPi.GPIO as GPIO
import time
import BlynkLib

# ConfiguraciÃ³n de Blynk
BLYNK_AUTH = 'TU_AUTH_TOKEN'  # Reemplaza con tu Auth Token de Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH, server="blynk.cloud", port=443, ssl=True)

# ConfiguraciÃ³n de los pines
GPIO_TRIGGER = 4  # Pin conectado a Trig
GPIO_ECHO = 17    # Pin conectado a Echo

# ConfiguraciÃ³n de GPIO
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

try:
    while True:
        dist = medir_distancia()
        print(f"Distancia: {dist} cm")

        # Enviar a Blynk con manejo de reconexiÃ³n
        try:
            blynk.virtual_write(1, dist)
        except BrokenPipeError:
            print("Error: reconectando a Blynk...")
            blynk = BlynkLib.Blynk(BLYNK_AUTH, server="blynk.cloud", port=443, ssl=True)

        blynk.run()
        time.sleep(1)

except KeyboardInterrupt:
    print("MediciÃ³n detenida por el usuario.")
finally:
    GPIO.cleanup()
