import RPi.GPIO as GPIO
import time

# ConfiguraciÃ³n de los pines
GPIO_TRIGGER = 4  # Pin conectado a Trig
GPIO_ECHO = 17    # Pin conectado a Echo

# ConfiguraciÃ³n de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def medir_distancia():
    # Configura el Trigger en bajo y espera un momento para estabilizar
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.5)
    
    # Enviar un pulso de 10Âµs
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    # Escuchar el pulso de respuesta en el Echo
    inicio_pulso = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        inicio_pulso = time.time()
    
    fin_pulso = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        fin_pulso = time.time()
    
    # Calcular la duraciÃ³n del pulso
    duracion = fin_pulso - inicio_pulso
    
    # Convertir la duraciÃ³n en distancia (en cm)
    distancia = duracion * 17150  # velocidad del sonido (34300 cm/s) dividida entre 2
    
    return round(distancia, 2)

try:
    while True:
        dist = medir_distancia()
        print(f"Distancia: {dist} cm")
        time.sleep(1)
except KeyboardInterrupt:
    print("MediciÃ³n detenida por el usuario.")
finally:
    GPIO.cleanup()

