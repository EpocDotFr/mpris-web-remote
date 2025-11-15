# MPRIS web remote

A dead simple, web-based remote to control playback on your computer from any device connected to the same network.

<p align="center">
  <img src="screenshot.png">
</p>

Too lazy to get up from your coach to pause the movie streamed on your computer when the lady goes to the toilet? I got
you covered. One button, one function: simplicity as a product. Plus zero installation fuss.

## Prerequisites

  - Python >= 3.10 (developed using Python 3.12)
  - A Linux-based OS (this project leverages [D-Bus](https://en.wikipedia.org/wiki/D-Bus) and [MPRIS2](https://specifications.freedesktop.org/mpris/latest/))

## Installation

  1. Clone this repo somewhere
  2. `pip install -r requirements.txt`

## Usage

  1. Run any program which is MPRIS-compatible (Firefox, VLC, whatever)
  2. `quart run`
  3. On another device connected to the same local network, navigate to `http://<ip>:8080`, where `<ip>` is the IP of the
     computer running this project

> [!CAUTION]
> This project is not suitable for production use. You have been warned.