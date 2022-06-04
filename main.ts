input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (_switch == 0) {
        number_1 += 1
        basic.showNumber(number_1)
    }
    
    if (_switch == 1) {
        number_2 += 1
        basic.showNumber(number_2)
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    operator += 1
    if (operator == 1) {
        basic.showLeds(`
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        `)
        basic.pause(100)
        basic.clearScreen()
    } else if (operator == 2) {
        basic.showLeds(`
                . . . . .
                                . . . . .
                                # # # # #
                                . . . . .
                                . . . . .
            `)
        basic.pause(100)
        basic.clearScreen()
    } else if (operator == 3) {
        basic.showLeds(`
                    # . . . #
                                        . # . # .
                                        . . # . .
                                        . # . # .
                                        # . . . #
                `)
        basic.pause(100)
        basic.clearScreen()
    } else if (operator == 4) {
        basic.showLeds(`
                        . . # . .
                                                . . . . .
                                                # # # # #
                                                . . . . .
                                                . . # . .
                    `)
        basic.pause(100)
        basic.clearScreen()
    } else {
        operator = 1
        basic.showLeds(`
                        . . # . .
                                                . . # . .
                                                # # # # #
                                                . . # . .
                                                . . # . .
                    `)
        basic.pause(100)
        basic.clearScreen()
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    basic.clearScreen()
    _switch += 1
    if (_switch == 2) {
        if (operator == 1) {
            basic.showNumber(number_1 + number_2)
        } else if (operator == 2) {
            basic.showNumber(number_1 - number_2)
        } else if (operator == 3) {
            basic.showNumber(number_1 * number_2)
        } else {
            basic.showNumber(number_1 / number_2)
        }
        
    }
    
})
let _switch = 0
let number_2 = 0
let number_1 = 0
let operator = 0
operator = 0
number_1 = 0
number_2 = 0
_switch = 0
