pins.digitalWritePin(DigitalPin.P0, 1)
pins.setPull(DigitalPin.P1, PinPullMode.PullUp)
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P1) == 0) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        basic.showIcon(IconNames.Yes)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.showIcon(IconNames.No)
    }
})
