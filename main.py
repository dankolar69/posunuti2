a = [0, 0]
b = [0, 1]
c = [0, 2]
d = [0, 3]
e = [0, 4]

led.plot(a[0], a[1])
led.plot(b[0], b[1])
led.plot(c[0], c[1])
led.plot(d[0], d[1])
led.plot(e[0], e[1])


def on_button_pressed_b():
    y = 0
    while y < 5:
        a[0] += 1
        b[0] += 1
        c[0] += 1
        d[0] += 1
        e[0] += 1
        y += 1
        
        if y >= 5:
            y = 0
            a[0] = 0
            b[0] = 0
            c[0] = 0
            d[0] = 0
            e[0] = 0
        basic.clear_screen()
        led.plot(a[0], a[1])
        led.plot(b[0], b[1])
        led.plot(c[0], c[1])
        led.plot(d[0], d[1])
        led.plot(e[0], e[1])
        basic.pause(3000)

input.on_button_pressed(Button.B, on_button_pressed_b)
