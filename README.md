# pi-stuff
A wee little collection of projects and scripts I've put together for Raspberry Pi shenanigans

## Hardware Used

- **[Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)**: Somewhat self-explanatory I hope, given the context.  4GB RAM version running
- **[Display HAT Mini](https://shop.pimoroni.com/products/display-hat-mini?variant=39496084717651)**: From Pimoroni, a 2", 320x240 LCD with some buttons for added funsies
- **[Sense HAT](https://www.raspberrypi.com/products/sense-hat/)**: Add-on board that includes a variety of sensors, an 8x8 LED matrix, and the world's smallest joystick
- **[TEMPerHUM](https://thepihut.com/products/temperhum-usb-temperature-and-humidity-sensor)**: A USB temperature and humidity sensor
- The cheapest set of USB speakers I could find, coupled with a 3-act hero's journey to get Linux to actually use them

## The Projects

### [Game of Life](./conway/README.md)

> Display HAT

A simple version of Conway's Game of Life, with a couple of twists - colour is based off time (one channel per hour/minute/second), and out of bounds neighbours count as random cells to keep the simulation 'alive'.

### [Creepy](./creepy/README.md)

> Sense HAT

A simple cycling display of Minecraft-based sprites in a shameless effort to impress my children.

### [Tempy](./tempy/README.md)

> TEMPerHUM

A sample project to use the TEMPerHUM.  Most of the heavy lifting is done by [cjmair's](https://github.com/cjmair/temperhum) work, much kudos there.

### [TTS](./tts/README.md)

> Speakers

Not really Raspberry PI related, but a component of the TelePI project below that I'm adding separately simply because of the effort involved in getting it working.  As the name suggests, it's a simple text-to-speech script.

### TelePi

> Sense HAT
> Speakers

Included here without code for now.  This was a long project to make what my children called 'the cursed computer'.  I set up Telegram integration so I could control an app via text.  It included:

- [TTS](./tts/README.md): so I could send messages to be read aloud
- [Creepy](./creepy/README.md) integration: so it could idle with Minecraft sprites
- Audio: a selection of mp3 files could be played, mostly to yell at children and tell them to come for dinner or get ready for school

I'll add it here once I a) extract out all the PII and credential stuff, b) remember how I set the Telegram integration up in the first place and c) make sure there aren't any horrifying security holes (there will be)
