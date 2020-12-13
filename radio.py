# import raspberry gpio library
import RPi.GPIO as GPIO
import time
import random

radiostreams = ['http://www.ndr.de/resources/metadaten/audio/m3u/ndr2.m3u']
radiostreams.append ('http://www.rockantenne.de/webradio/rockantenne.m3u')
radiostreams.append ('http://www.rockantenne.de/webradio/channels/punkrock.m3u')
radiostreams.append ('http://www.rockantenne.de/webradio/channels/rockandroll.m3u')
radiostreams.append ('http://www.rockantenne.de/webradio/channels/alternative.m3u')
radiostreams.append ('http://www.rockantenne.de/webradio/channels/heavy-metal.m3u')
radiostreams.append ('http://www.rockantenne.de/webradio/channels/classic-perlen.m3u')
radiostreams.append ('http://streams.radiobob.de/bob-90srock/mp3-128/streams.radiobob.de/play.m3u')
radiostreams.append ('http://streams.radiobob.de/bob-alternative/mp3-128/streams.radiobob.de/play.m3u')
radiostreams.append ('http://streams.radiobob.de/bob-bestofrock/mp3-128/streams.radiobob.de/play.m3u')
radiostreams.append ('http://streams.radiobob.de/bob-hartesaite/mp3-128/streams.radiobob.de/play.m3u')
radiostreams.append ('http://streams.radiobob.de/bob-metal/mp3-128/streams.radiobob.de/play.m3u')
radiostreams.append ('http://streams.radiobob.de/bob-punk/mp3-128/streams.radiobob.de/play.m3u')
radiostreams.append ('http://streams.radiobob.de/bob-rockhits/mp3-128/streams.radiobob.de/play.m3u')
radiostreams.append ('http://streams.radiobob.de/metalcore/mp3-128/streams.radiobob.de/play.m3u')
radiostreams.append ('http://streams.radiobob.de/bob-shlive/mp3-128/streams.radiobob.de/play.m3u')
radiostreams.append ('http://stream.radiohamburg.de/rhh-live/mp3-128/linkradiohamburgde/play.m3u')
radiostreams.append ('http://streams.deltaradio.de/delta-alternative/mp3-128/listenlive/play.m3u')
radiostreams.append ('http://stream.hamburg-zwei.de/hh2-live/mp3-128/listenlive/stream.m3u')

GPIO.setmode(GPIO.BCM)

# setup the GPIO pins
GPIO.setup(22, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
        buttonRadio = GPIO.input(22)
        buttonVolUp = GPIO.input(23)
        buttonVolDown = GPIO.input(24)
        buttonStop = GPIO.input(25)

        if (buttonRadio == False):
                # stop current station
                from subprocess import call
                call(["killall", "mpg123"])

                # run new station
                print("Starting random Radio Station")
                station = random.choice(radiostreams)
                print(station)
                runcommand = 'mpg123 -@{0}'.format(station)
                from subprocess import Popen
                Popen(runcommand.split(), shell=False)
        
        if (buttonStop == False):
                # stop current station
                from subprocess import call
                call(["killall", "mpg123"])
                print("Stopping")

        if (buttonVolUp == False):
                print("Vol+")

                # example with amixer
                from subprocess import call
                call(["vol.sh", "+"])

        if (buttonVolDown == False):
                print("Vol-")

                # example with amixer
                from subprocess import call
                call(["vol.sh", "-"])

        time.sleep(0.1)