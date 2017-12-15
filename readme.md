# Audio Engine

I know pretty well what I want from a live performance audio engine (largely due
to years spent with the magnificent [Nord G2X](http://www.nordkeyboards.com/products/nord-modular-g2)).

I don't know exactly how to get it.

In this repository, I hope to articulate exactly what I want and figure out how
I might be able to get it.


## Requirements

- Digital (with deep magic analog can be simulated pretty well but analog can
  never be made as reliable and reproduceable as digital)
- Hard real-time (guarantee that loaded patches will run without glitching)
- Scale number/complexity of simultaneous patches based on current hardware
- CPU architecture agnostic (DSP chips are cool but tie you to hardware that
  stops getting produced)
- Open source (so the instruments I design could in theory be played in distant
  future)
- MIDI support
- OSC support
- Support for defining new controller interfaces (if MIDI/OSC aren't enough)
- Support for arbitrary # of audio inputs/outputs
- First-class support for defining new DSP audio processing primitives

...I know there are more but that's a start, which is all I'm looking for right
now.


## How Not To Build It

It's very possible something out there already meets my perceived needs and I
just don't know about it.

I've done a fair amount of searching, but the smart thing would be to refine my
requirements into a semi-clear articulation, then ask for it in the relevant
communities online - electro-music.com, any StackExchange audio site, and maybe
a subreddit or three.

If what I want is out there, someone there can tell me about it.


## How To Build It

I have not found anything that meets all these requirements. If it doesn't
exist and I can't get more talented folks to build it for me, how could I build
it?


### Write Raw DSP Patches By Hand

I have an okay-ish grasp of how DSP works.

Writing a few basic components from scratch and getting them to generate audio
in concert would be a great way to find out just how much I don't understand.

With the knowledge gained from that experiment, I'd be much better suited to
start working on the building blocks I need.

Note that these need not be interactive - just render an audio file using
nothing but my own code to generate samples.

Something like:

- sine wave generator
- saw wave generator
- low-pass filter (tested on the saw wave, presumably)
- LFO (test by modulating oscillator pitches and/or filter cutoff)
- program combining them into something vaguely resembling 'music'

Looks like Python has a built-in module for working with .wav files ('wave',
predictably enough), so that could be a place to start.


### Write Interactive DSP Patch By Hand

Easy to explain, if not for me to do - repurpose my test hunks of code into
things that work interactively on a desktop computer with MIDI reasonably well.

Again, this means teaching it about MIDI entirely myself. That's painful wheel
reinvention, to force me to really understand the building blocks myself.

I'm sure it would be a horribly painful experience, and that I'd learn a ton
from it.

Bonus Points: find a cheap OSC controller and teach it to speak OSC, too.


### Find Real-Time OS That Meets My Requirements

Somewhere out there, a real-time OS that has decent primitives for abstracting
the hardware and handling audio *has* to exist.

...right?

If not, roll up my sleeves and learn enough fundamentals to add whatever's
missing to the best candidate.


### Port Interactive DSP Patch To Chosen OS

Again, this should teach me all sorts of horrible lessons I don't yet know I
don't know.


### Port Three Of My G2 Patches To Chosen OS

This, again, would be horribly painful.

But, once I've done it, even if they sound nothing like the original and barely
work at all, I will have a bunch of shoddy code that taught me painful lessons
I can then apply for the next step:


### Hack Out POC For Building Interactive Patches On Chosen OS

This is the "miracle occurs" step.

at the moment I think the essence of this is:

- DSP primitive units know nothing about hardware
- Defining new DSP primitives is semi-feasible
- MIDI (and OSC?) are handled for you
- Layering, splitting, and inter-patch communication all work
- Engine can tell you how much load this machine can handle


### ???

There are ten billion things I'd want to layer on top of this if I got that
much working.

For the moment, that's way more planning than I need for a project I have no
time to work on.

If I actually managed to get it this far, I might actually consider trying to
apply my business plan.


## How To Finance It

I can't build this for free, really. No way I'll ever have enough time, even if
I retire at 55 and live into my 90s.

A business model could be to build a killer performance instrument *around* the
core audio engine, not unlike the G2 (so freaking playable).

The mistake that killed the G2, IMO, was not having patches stock on the
shipping instrument that blew peoples' minds. The stuff that came in later
years many regular keyboard players would have died to have, if only they'd
known it could be done.

By the same token, regular keyboard players will pay through the nose for an
instrument with killer patches. The fact that the software is OSS doesn't
matter - they want to buy a working instrument that plays beautifully, not
spend hours sourcing and assembling their own hardware.

So, unlike many OSS projects, I think this one could actually be a viable
business, supported by hardware sales - *if* you could build a really amazing
instrument(s?), which is a *gigantic* if.
