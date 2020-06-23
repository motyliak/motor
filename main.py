def motor_off():
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.show_icon(IconNames.NO)

def on_button_pressed_a():
    global remote_control
    remote_control = False
    motor_on()
    strip.rotate(1)
    strip.show()
    
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global remote_control
    motor_off()
    remote_control = True
input.on_button_pressed(Button.B, on_button_pressed_b)

def motor_on():
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.show_icon(IconNames.YES)
remote_control = False
pins.digital_write_pin(DigitalPin.P0, 1)
pins.set_pull(DigitalPin.P1, PinPullMode.PULL_UP)
basic.show_icon(IconNames.HAPPY)
remote_control = True
strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)
strip.show_rainbow(1, 360)
strip.show()

def on_forever():
    strip.show()
    if remote_control:
        if pins.digital_read_pin(DigitalPin.P1) == 0:
            motor_on()
        else:
            motor_off()
basic.forever(on_forever)
