# MPRIS web remote

A dead simple, web-based remote to control playback on your computer from any device connected to the same network.

<p align="center">
  <img src="screenshot.png">
</p>

Too lazy to get up from your coach to pause the movie streamed on your computer when the lady goes to the toilet? I got
you covered. One button, one function: simplicity as a product. Plus zero installation or configuration fuss.

## Prerequisites

  - Python >= 3.10 (developed using Python 3.12)
  - A modern web browser
  - A Linux-based OS (this project leverages [D-Bus](https://en.wikipedia.org/wiki/D-Bus) and [MPRIS2](https://specifications.freedesktop.org/mpris/latest/))

## Installation

  1. Clone this repo somewhere
  2. `pip install -r requirements.txt`

## Usage

  1. `quart run`
  2. Run any program which is MPRIS-compatible (Firefox, VLC, whatever). The first one found will be used
  3. On another device connected to the same network, navigate to `http://<name>.local:8080`, where `<name>` is the name
     of the computer running this project (this leverages [mDNS](https://en.wikipedia.org/wiki/Multicast_DNS))

## Deployment

> [!CAUTION]
> This project is NOT suitable for production use. Do NOT attempt to deploy for use through internet.