# Tempy

> TEMPerHUM

A utility to monitor temperature and humidity for a workspace where that was important enough to do, but unimportant enough for me to enjoy it.

## Instructions

### Installation

This project relies on the [TEMPerHUM](https://github.com/cjmair/temperhum) library from cjmair - of all the sample code and repos I found, this was the one that worked and was an absolute godsend.  Follow the instructions in the linked repository to get set up.

### Running

- If you just want local reporting, run `python3 watch.py`
- For remote logging, set up `upload.py` with your own endpoint and configuration, then run `python3 main.py`

Both take a reading and report every 30 minutes.
