function coreo15 () {
    linea = 0
    valor = 0
    anterior = 0
    ballant = 1
    velmotor = 30
    if (Gegant == "M") {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
        basic.pause(1000)
        while (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0) {
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 15)
        }
        maqueen.motorStop(maqueen.Motors.M2)
    } else {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 15)
        }
        maqueen.motorStop(maqueen.Motors.M1)
    }
    ballant = 0
}
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        relvelocidad = 0.5
    } else if (receivedNumber == -1) {
        relvelocidad = 0.7
    } else {
        relvelocidad = 0.6
    }
})
function coreo21 () {
    ballant = 1
    velmotor = 25
    linea = 0
    anterior = 1
    relvelocidad = 0.6
    if (Gegant == "\"X\"") {
        distanciabase = maqueen.Ultrasonic(PingUnit.Centimeters)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 15)
        while (linea < 4) {
            valor = maqueen.readPatrol(maqueen.Patrol.PatrolLeft)
            if (anterior != valor) {
                linea = linea + 1
            }
            persegeixX()
            basic.pause(100)
        }
        maqueen.motorStop(maqueen.Motors.M2)
    } else {
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
            basic.pause(100)
        }
        while (linea < 3) {
            valor = maqueen.readPatrol(maqueen.Patrol.PatrolLeft)
            if (anterior != valor) {
                linea = linea + 1
            }
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, velmotor * relvelocidad)
            basic.pause(100)
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0) {
            maqueen.motorStop(maqueen.Motors.M2)
            basic.pause(200)
        }
        maqueen.motorStop(maqueen.Motors.M1)
    }
    ballant = 0
}
function coreo15_res () {
    linea = 0
    valor = 0
    anterior = 0
    ballant = 1
    velmotor = 25
    if (Gegant == "M") {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
        while (linea < 4) {
            valor = maqueen.readPatrol(maqueen.Patrol.PatrolRight)
            if (anterior != valor) {
                anterior = valor
                linea = linea + 1
            }
        }
        maqueen.motorStop(maqueen.Motors.M2)
    } else {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
        while (linea < 4) {
            valor = maqueen.readPatrol(maqueen.Patrol.PatrolLeft)
            if (anterior != valor) {
                anterior = valor
                linea = linea + 1
            }
        }
        maqueen.motorStop(maqueen.Motors.M2)
    }
    ballant = 0
}
function coreo15_ultrasons () {
    linea = 0
    valor = 0
    anterior = 0
    ballant = 1
    velmotor = 30
    if (Gegant == "M") {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
        basic.pause(2000)
        distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
        while (distancia > 12) {
            distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
        }
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 15)
        while (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0) {
        	
        }
        maqueen.motorStop(maqueen.Motors.M2)
    } else {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
        basic.pause(2000)
        distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
        while (distancia > 12) {
            distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
        }
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 15)
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        	
        }
        maqueen.motorStop(maqueen.Motors.M1)
    }
    ballant = 0
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
function persegeixX () {
    distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
    if (distancia > 30) {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 25)
    } else {
        if (distancia > distanciabase * 1.1) {
            // Si esta lluny
            radio.sendNumber(1)
        } else if (distancia < distanciabase * 0.9) {
            // Si esta aprop
            radio.sendNumber(-1)
        } else {
            radio.sendNumber(0)
        }
    }
}
function Coreo13 () {
    ballant = 1
    velmotor = 25
    distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
    while (distancia > 12) {
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, velmotor)
        } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 20)
        } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 20)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
        } else {
            maqueen.motorStop(maqueen.Motors.M1)
            maqueen.motorStop(maqueen.Motors.M2)
        }
        distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
    }
    maqueen.motorStop(maqueen.Motors.All)
    ballant = 0
}
function coreo17 () {
    linea = 0
    valor = 0
    anterior = 0
    ballant = 1
    velmotor = 30
    if (Gegant == "X") {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, velmotor)
        basic.pause(1000)
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 15)
        }
        maqueen.motorStop(maqueen.Motors.M2)
    } else {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, velmotor)
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        	
        }
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 15)
        }
        maqueen.motorStop(maqueen.Motors.M1)
    }
    ballant = 0
}
radio.onReceivedString(function (receivedString) {
    coreografia_part = receivedString
    if (!(ballant)) {
        if (coreografia_part == "C13") {
            Coreo13()
        } else if (coreografia_part == "C15") {
            coreo15()
        } else if (coreografia_part == "C17") {
            coreo17()
        } else {
        	
        }
    }
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
let distancia = 0
let distanciabase = 0
let relvelocidad = 0
let velmotor = 0
let anterior = 0
let valor = 0
let linea = 0
let Gegant = ""
let ballant = 0
ballant = 0
Gegant = "?"
radio.setGroup(100)
basic.showLeds(`
    . # # # .
    # . . . #
    . . . # .
    . . # . .
    . . # . .
    `)
