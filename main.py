pins.digital_write_pin(DigitalPin.P0, 1)
pins.set_pull(DigitalPin.P1, PinPullMode.PULL_UP)
basic.show_icon(IconNames.HEART)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P1) == 0:
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.show_icon(IconNames.YES)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)
