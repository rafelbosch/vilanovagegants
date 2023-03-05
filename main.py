def Coreografia():
    global coreografia_part
    coreografia_part = 1
    part1()
    coreografia_part = 2
    Part2()
    coreografia_part = 3
    part1()
    coreografia_part = 4
    Part3()
    coreografia_part = 5
    par4()
    coreografia_part = 6
    part5()
    coreografia_part = 7
    par4()
    coreografia_part = 8
    part6()
def part5():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.DOUBLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))

def on_button_pressed_a():
    Coreografia()
input.on_button_pressed(Button.A, on_button_pressed_a)

def part6():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.DOUBLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
def par4():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
def Part2():
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))

def on_button_pressed_b():
    part6()
input.on_button_pressed(Button.B, on_button_pressed_b)

def Part3():
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.DOUBLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
def part1():
    music.set_volume(255)
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.DOUBLE))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
perseguir = 0
distancia = 0
Encontrado = 0
coreografia_part = 0
coreografia_part += 0
basic.pause(2000)
while not (Encontrado):
    distancia = maqueen.ultrasonic(PingUnit.CENTIMETERS)
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