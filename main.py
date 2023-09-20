a = 0

def on_button_pressed_a():
    global a
    if True:
        a -= 1
        basic.show_number(a)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global a
    if True:
        a += 1
        basic.show_number(a)
input.on_button_pressed(Button.B, on_button_pressed_b)