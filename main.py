def coreo15():
    global linea, ballant, velmotor
    linea = 0
    ballant = 1
    velmotor = 25
    if Gegant == "\"M\"":
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
        basic.pause(500)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            basic.pause(100)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            basic.pause(100)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            basic.pause(100)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            basic.pause(100)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            basic.pause(100)
        maqueen.motor_stop(maqueen.Motors.M2)
    else:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
        basic.pause(500)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
            basic.pause(100)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
            basic.pause(100)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
            basic.pause(100)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
            basic.pause(100)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
            basic.pause(100)
        maqueen.motor_stop(maqueen.Motors.M2)
    ballant = 0
def coreo21():
    global distancia, Encontrado, perseguir
    while not (Encontrado):
        distancia = 0
        if distancia < 30:
            Encontrado = 1
    while Encontrado:
        distancia = maqueen.ultrasonic(PingUnit.CENTIMETERS)
        if distancia > 30:
            perseguir = 1
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 15)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 15)
        elif perseguir:
            perseguir = 0
            maqueen.motor_stop(maqueen.Motors.ALL)

def on_button_pressed_a():
    global Gegant
    Gegant = "M"
    basic.show_leds("""
        # . . . #
                # # . # #
                # . # . #
                # . . . #
                # . . . #
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def Coreo13():
    global ballant, velmotor, distancia
    ballant = 1
    velmotor = 25
    distancia = maqueen.ultrasonic(PingUnit.CENTIMETERS)
    while distancia > 8:
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, velmotor)
        elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 20)
        elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 20)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
        else:
            maqueen.motor_stop(maqueen.Motors.ALL)
    maqueen.motor_stop(maqueen.Motors.ALL)
    ballant = 0

def on_received_string(receivedString):
    global coreografia_part
    coreografia_part = receivedString
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global Gegant
    Gegant = "X"
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

coreografia_part = ""
perseguir = 0
distancia = 0
Encontrado = 0
velmotor = 0
linea = 0
Gegant = ""
ballant = 0
ballant = 0
Gegant = "?"
radio.set_group(101)
basic.show_leds("""
    . # # # .
        # . . . #
        . . . # .
        . . # . .
        . . # . .
""")

def on_forever():
    if not (ballant):
        if coreografia_part == "C13":
            Coreo13()
basic.forever(on_forever)
