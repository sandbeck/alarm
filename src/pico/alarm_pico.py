from machine import Pin
from utime import sleep_ms

PIN_PIR = 28
PIN_LYS = 25
PIN_KNAP = 15
PIN_SIRENE = 16

pir = Pin(PIN_PIR, Pin.IN, Pin.PULL_DOWN)
knap = Pin(PIN_KNAP, Pin.IN, Pin.PULL_DOWN)
lys = Pin(PIN_LYS, Pin.OUT)
sirene = Pin(PIN_SIRENE, Pin.OUT)

alarmAktiv = False

# Interrupt haandtering
def pir_handler(pin: Pin):
    sleep_ms(100)
    if pin.value() and alarmAktiv:
        print("ALARM! Du er opdaget!")
        lys.on()
        sirene.on()

def slaa_alarm_til(pin: Pin):
    global alarmAktiv
    sleep_ms(2000)
    if pin.value():
        print("Slaar alarm til om 10 sekunder")
        # nedtaelling med lys og lyd
        nedtaelling(9)
        # sluk sirene og lys
        lys.off()
        sirene.off()
        # aktiver alarm
        alarmAktiv = True
        
        # knap skal nu deaktivere alarm
        knap.irq(trigger=Pin.IRQ_RISING, handler=slaa_alarm_fra)

def slaa_alarm_fra(pin: Pin):
    global alarmAktiv
    sleep_ms(2000)
    if pin.value():
        print("Alarm deaktiveret")
        alarmAktiv = False
        lys.off()
        sirene.off()
        knap.irq(trigger=Pin.IRQ_RISING, handler=slaa_alarm_til)

# hjaelpemetoder
def nedtaelling(fra: int):
    for i in range(fra):
        sleep_ms(900)
        print( f'{fra - i} {"..."}')
        lys.on()
        sleep_ms(100)
        lys.off()
    lys.on()
    print("Slaaet til")
    sleep_ms(1000)

# Opstart
print("Starter alarm...")
lys.value(0)
sirene.value(0)
knap.irq(trigger=Pin.IRQ_RISING, handler=slaa_alarm_til)
# aktiver pir
pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

print("Klar!")
