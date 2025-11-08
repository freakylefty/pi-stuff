# pi-stuff
A wee little collection of projects and scripts I've put together for Raspberry Pi shenanigans

## Hardware Used

- **[Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)**: Somewhat self-explanatory I hope, given the context.  4GB RAM version running  
- **[Display HAT Mini](https://shop.pimoroni.com/products/display-hat-mini?variant=39496084717651)**: From Pimoroni, a 2", 320x240 LCD with some buttons for added funsies
- **[Sense HAT](https://www.raspberrypi.com/products/sense-hat/)**: Add-on board that includes a variety of sensors, an 8x8 LED matrix, and the world's smallest joystick

## The Projects

### [Game of Life](./conway/README.md)

> Display HAT

A simple version of Conway's Game of Life, with a couple of twists - colour is based off time (one channel per hour/minute/second), and out of bounds neighbours count as random cells to keep the simulation 'alive'.
