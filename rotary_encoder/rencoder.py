# -*- coding: utf-8 -*-
"""MicroPython rotary encoder library.
From: https://forum.micropython.org/viewtopic.php?t=1704

Original Code thanks to Christopher Arndt.

"""

from machine import Pin


ENC_STATES = (0, -1, 1, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 1, -1, 0)


class Encoder(object):
    """
    Rotary encoder class
    """
    def __init__(self, pin_x = 'GP4',pin_y = 'GP5', pin_mode=Pin.PULL_UP,
                 scale=1, min=0, max=100, reverse=False):
        """Initializes the rotary encoder.

        @pin_x:
        @pin_y:
        @pin_mode:
        @scale:
        @min:
        @max:
        @reverse:
        """
        self.pin_x = (pin_x if isinstance(pin_x, Pin) else
                      Pin(pin_x, mode=Pin.IN, pull=pin_mode))
        self.pin_y = (pin_y if isinstance(pin_y, Pin) else
                      Pin(pin_y, mode=Pin.IN, pull=pin_mode))

        self.pin_mode = pin_mode
        self.scale = scale
        self.min = min
        self.max = max
        self.reverse = 1 if reverse else -1

        # The following variables are assigned to in the interrupt callback,
        # so we have to allocate them here.
        self._pos = -1
        self._readings = 0
        self._state = 0

        self.set_callbacks(self._callback)

    def _callback(self, line):
        self._readings = (self._readings << 2 | self.pin_x.value() << 1 |
                          self.pin_y.value()) & 0x0f

        self._state = ENC_STATES[self._readings] * self.reverse
        if self._state:
            self._pos = min(max(self.min, self._pos + self._state), self.max)

    def set_callbacks(self, callback=None):
        """Set IRQ callbacks."""
        self.irq_x = self.pin_x.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
                                    handler=callback)
        self.irq_y = self.pin_y.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
                                    handler=callback)

    @property
    def position(self):
        """Get current position."""
        return self._pos * self.scale

    def reset(self):
        """Reset position of the encoder."""
        self._pos = 0
