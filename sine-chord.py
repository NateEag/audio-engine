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

help_msg = '''Usage: %s <output.wav> <length> <amplitude> <frequency>...

length - length of WAV file in seconds.
amplitude - volume of sine wave as a float - 0 is silent, 1 is max.
frequency - pitch of sine wave in hertz (integer).''' % sys.argv[0]


def sine_sample(frequency, time):
    """Return a sample for a sinewave with given `frequency` at `time`."""

    return math.sin(2 * math.pi * frequency * time)


def main():
    if len(sys.argv) < 5:
        print(help_msg)

        exit(2)

    num_seconds = int(sys.argv[2])

    f = wave.open(sys.argv[1], 'w')

    f.setnchannels(NUM_CHANNELS)
    f.setsampwidth(SAMPLE_WIDTH)
    f.setframerate(FRAMERATE)

    frequencies = [int(freq) for freq in sys.argv[4:]]

    amplitude = float(sys.argv[3])
    amplitude = math.ceil(float(amplitude) * MAX_SAMPLE_VALUE)

    for i in range(0, num_seconds * 44100):
        time_in_secs = i / 44100.0

        value = 0
        for frequency in frequencies:
            value += sine_sample(frequency, time_in_secs)

        # FIXME This does not account for multiple sines adding up to be > 1.
        #
        # In a real system you'd have a mixer module proper - here I'd just
        # split my max sample value across all the pitches, I guess?
        #
        # As long as you keep the number of notes and amplitude value low this
        # works fine, of course... :P
        value = amplitude * value

        packed_value = struct.pack('h', int(value))

        # Outputting the same value once for each audio channel, I think?
        f.writeframes(packed_value)
        f.writeframes(packed_value)

    f.close()

if __name__ == '__main__':
    main()
