def coreo15():
    global linea, valor, anterior, ballant, velmotor
    linea = 0
    valor = 0
    anterior = 0
    ballant = 1
    velmotor = 25
    if Gegant == "\"M\"":
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
        while linea < 4:
            valor = maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)
            if anterior != valor:
                anterior = valor
                linea = linea + 1
            basic.pause(100)
        maqueen.motor_stop(maqueen.Motors.M2)
    else:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
        while linea < 4:
            valor = maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)
            if anterior != valor:
                anterior = valor
                linea = linea + 1
                basic.pause(100)
        maqueen.motor_stop(maqueen.Motors.M2)
    ballant = 0

def on_received_number(receivedNumber):
    global relvelocidad
    if receivedNumber == 1:
        relvelocidad = 0.5
    elif receivedNumber == -1:
        relvelocidad = 0.7
    else:
        relvelocidad = 0.6
radio.on_received_number(on_received_number)

def coreo21():
    global ballant, velmotor, linea, anterior, relvelocidad, distanciabase, valor
    ballant = 1
    velmotor = 25
    linea = 0
    anterior = 1
    relvelocidad = 0.6
    if Gegant == "\"X\"":
        distanciabase = maqueen.ultrasonic(PingUnit.CENTIMETERS)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 15)
        while linea < 4:
            valor = maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)
            if anterior != valor:
                linea = linea + 1
            persegeixX()
            basic.pause(100)
        maqueen.motor_stop(maqueen.Motors.M2)
    else:
        while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
            basic.pause(100)
        while linea < 3:
            valor = maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)
            if anterior != valor:
                linea = linea + 1
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, velmotor * relvelocidad)
            basic.pause(100)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
            maqueen.motor_stop(maqueen.Motors.M2)
            basic.pause(200)
        maqueen.motor_stop(maqueen.Motors.M1)
    ballant = 0

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

def persegeixX():
    global distancia
    distancia = maqueen.ultrasonic(PingUnit.CENTIMETERS)
    if distancia > 30:
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 25)
    else:
        if distancia > distanciabase * 1.1:
            # Si esta lluny
            radio.send_number(1)
        elif distancia < distanciabase * 0.9:
            # Si esta aprop
            radio.send_number(-1)
        else:
            radio.send_number(0)
def Coreo13():
    global ballant, velmotor, distancia
    ballant = 1
    velmotor = 25
    distancia = maqueen.ultrasonic(PingUnit.CENTIMETERS)
    while distancia > 10:
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
        distancia = maqueen.ultrasonic(PingUnit.CENTIMETERS)
    maqueen.motor_stop(maqueen.Motors.ALL)
    ballant = 0
def coreo17():
    global linea, valor, anterior, ballant, velmotor
    linea = 0
    valor = 0
    anterior = 0
    ballant = 1
    velmotor = 25
    if Gegant == "\"X\"":
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
        while linea < 4:
            valor = maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)
            if anterior != valor:
                linea = linea + 1
            basic.pause(100)
        maqueen.motor_stop(maqueen.Motors.M2)
    else:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
        while linea < 4:
            valor = maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)
            if anterior != valor:
                linea = linea + 1
                basic.pause(100)
        maqueen.motor_stop(maqueen.Motors.M2)
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
distancia = 0
distanciabase = 0
relvelocidad = 0
velmotor = 0
anterior = 0
valor = 0
linea = 0
Gegant = ""
ballant = 0
ballant = 0
Gegant = "?"
radio.set_group(100)
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
            coreo15()
        elif coreografia_part == "C15":
            pass
        else:
            pass
basic.forever(on_forever)
