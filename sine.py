"""A test of generating a WAV file with Python."""

import sys
import wave
import math
import random
import struct

# yay stereo sound
NUM_CHANNELS = 2

# number of bytes in a single audio sample
SAMPLE_WIDTH = 2

# Looks like ye olde 44.1 kHz sampling rate?
FRAMERATE = 44100

# What's the highest possible sample value?
BITS_IN_SAMPLE = SAMPLE_WIDTH * 8 - 1
MAX_SAMPLE_VALUE = 2 ** BITS_IN_SAMPLE - 1

help_msg = '''Usage: %s <output.wav> <length> <frequency> <amplitude>

length - length of WAV file in seconds.
frequency - pitch of sine wave in hertz (integer).
amplitude - volume of sine wave as a float - 0 is silent, 1 is max.''' % sys.argv[0]


def main():

    if len(sys.argv) < 5:
        print()

        exit(2)

    num_seconds = int(sys.argv[2])

    f = wave.open(sys.argv[1], 'w')

    f.setnchannels(NUM_CHANNELS)
    f.setsampwidth(SAMPLE_WIDTH)
    f.setframerate(FRAMERATE)

    frequency = int(sys.argv[3])

    amplitude = math.ceil(float(sys.argv[4]) * MAX_SAMPLE_VALUE)
    amplitude = int(amplitude)

    for i in range(0, num_seconds * 44100):
        time_in_secs = i / 44100.0

        value = amplitude * math.sin(2 * math.pi * frequency * time_in_secs)
        packed_value = struct.pack('h', int(value))

        # Outputting the same value once for each audio channel, I think?
        f.writeframes(packed_value)
        f.writeframes(packed_value)

    f.close()

if __name__ == '__main__':
    main()
