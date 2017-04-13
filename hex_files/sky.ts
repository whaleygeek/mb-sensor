basic.forever(() => {
    if (input.acceleration(Dimension.Y) > 1000) {
        radio.sendString("sky")
        basic.showIcon(IconNames.Heart)
        while (input.acceleration(Dimension.Y) > 1000) {
            basic.pause(100)
        }
        basic.clearScreen()
    }
    basic.pause(100)
})
radio.setGroup(0)
