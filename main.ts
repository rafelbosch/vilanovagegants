function coreo21 () {
    while (!(Encontrado)) {
        distancia = 0
        if (distancia < 30) {
            Encontrado = 1
        }
    }
    while (Encontrado) {
        distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
        if (distancia > 30) {
            perseguir = 1
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 15)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 15)
        } else if (perseguir) {
            perseguir = 0
            maqueen.motorStop(maqueen.Motors.All)
        }
    }
}
input.onButtonPressed(Button.A, function () {
    Gegant = "M"
    basic.showLeds(`
        # . . . #
        # # . # #
        # . # . #
        # . . . #
        # . . . #
        `)
})
function Coreo13 () {
    velmotor = 25
    distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
    if (distancia > 8) {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, velmotor)
    } else {
        maqueen.motorStop(maqueen.Motors.All)
    }
}
function Coreo13n () {
    velmotor = 60
    distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, velmotor)
    if (distancia > 8) {
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, velmotor)
        } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 20)
        } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 20)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
        } else {
            maqueen.motorStop(maqueen.Motors.All)
        }
    }
}
radio.onReceivedString(function (receivedString) {
    coreografia_part = receivedString
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    Gegant = "X"
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
})
let coreografia_part = ""
let velmotor = 0
let Gegant = ""
let perseguir = 0
let distancia = 0
let Encontrado = 0
radio.setGroup(101)
basic.showLeds(`
    . # # # .
    # . . . #
    . # . . #
    . . # . .
    . . # . .
    `)
