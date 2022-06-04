def on_button_pressed_a():
    global number_1, number_2
    if _switch == 0:
        number_1 += 1
        basic.show_number(number_1)
    if _switch == 1:
        number_2 += 1
        basic.show_number(number_2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global operator
    operator += 1
    if operator == 1:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
        basic.pause(100)
        basic.clear_screen()
    else:
        if operator == 2:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                # # # # #
                                . . . . .
                                . . . . .
            """)
            basic.pause(100)
            basic.clear_screen()
        else:
            if operator == 3:
                basic.show_leds("""
                    # . . . #
                                        . # . # .
                                        . . # . .
                                        . # . # .
                                        # . . . #
                """)
                basic.pause(100)
                basic.clear_screen()
            else:
                if operator == 4:
                    basic.show_leds("""
                        . . # . .
                                                . . . . .
                                                # # # # #
                                                . . . . .
                                                . . # . .
                    """)
                    basic.pause(100)
                    basic.clear_screen()
                else:
                    operator = 1
                    basic.show_leds("""
                        . . # . .
                                                . . # . .
                                                # # # # #
                                                . . # . .
                                                . . # . .
                    """)
                    basic.pause(100)
                    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global _switch
    basic.clear_screen()
    _switch += 1
    if _switch == 2:
        if operator == 1:
            basic.show_number(number_1 + number_2)
        else:
            if operator == 2:
                basic.show_number(number_1 - number_2)
            else:
                if operator == 3:
                    basic.show_number(number_1 * number_2)
                else:
                    basic.show_number(number_1 / number_2)
input.on_button_pressed(Button.B, on_button_pressed_b)

_switch = 0
number_2 = 0
number_1 = 0
operator = 0
operator = 0
number_1 = 0
number_2 = 0
_switch = 0