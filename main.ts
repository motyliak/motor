function motor_off() {
    pins.digitalWritePin(DigitalPin.P0, 0)
    basic.showIcon(IconNames.No)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    remote_control = false
    motor_on()
    strip.rotate(1)
    strip.show()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    motor_off()
    remote_control = true
})
function motor_on() {
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.showIcon(IconNames.Yes)
}

let remote_control = false
pins.digitalWritePin(DigitalPin.P0, 1)
pins.setPull(DigitalPin.P1, PinPullMode.PullUp)
basic.showIcon(IconNames.Happy)
remote_control = true
let strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)
strip.showRainbow(1, 360)
strip.show()
basic.forever(function on_forever() {
    strip.show()
    if (remote_control) {
        if (pins.digitalReadPin(DigitalPin.P1) == 0) {
            motor_on()
        } else {
            motor_off()
        }
        
    }
    
})
