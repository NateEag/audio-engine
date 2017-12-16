"""A test of generating a WAV file with Python."""

import sys
import wave
import math
import random
import struct

def main():

    if len(sys.argv) < 3:
        print('Usage: %s <output.wav> <seconds-length>' % sys.argv[0])

        exit(2)

    num_seconds = int(sys.argv[2])

    f = wave.open(sys.argv[1], 'w')

    # yay stereo sound
    f.setnchannels(2)
    # not sure what this is
    f.setsampwidth(2)
    # Looks like ye olde 44.1 kHz
    f.setframerate(44100)

    for i in range(0, num_seconds * 44100):
        value = random.randint(-32767, 32767)
        packed_value = struct.pack('h', value)

        # Outputting the same value once for each audio channel, I think?
        f.writeframes(packed_value)
        f.writeframes(packed_value)

    f.close()

if __name__ == '__main__':
    main()
