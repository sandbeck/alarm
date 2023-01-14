import machine
import utime

PIN_PIR = 28

pir = machine.Pin(PIN_PIR, machine.Pin.IN, machine.Pin.PULL_DOWN)

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("ALARM! Bevaegelse detekteret")

pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

