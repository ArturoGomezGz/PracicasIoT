import blynklib

BLYNK_AUTH = 'beuEgtupZMgQPAoyg9xXXvYJVgtONlAU'
blynk = blynklib.Blynk(BLYNK_AUTH)

blynk.run()
blynk.virtual_write(0, 10)

blynk.disconnect()