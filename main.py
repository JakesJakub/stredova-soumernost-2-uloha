A = 0

def on_button_pressed_a():
    global A
    A += 1
    if A == 1:
        basic.clear_screen()
        led.plot_brightness(2, 2, 100)
        led.plot(0, 0)
        led.plot(0, 2)
        led.plot(1, 2)
        led.plot(1, 0)
        led.plot(4, 4)
        led.plot(3, 4)
        led.plot(4, 2)
        led.plot(3, 2)

    if A == 2:
        basic.clear_screen()
        led.plot_brightness(2, 2, 100)
        led.plot(4, 0)
        led.plot(4, 2)
        led.plot(3, 2)
        led.plot(3, 0)
        led.plot(0, 4)
        led.plot(1, 4)
        led.plot(0, 2)
        led.plot(1, 2)
        A -= 2
input.on_button_pressed(Button.A, on_button_pressed_a)