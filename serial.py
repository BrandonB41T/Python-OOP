"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Create new generator"""
        self.start = start
        self.nextNum = start

    def __repr__(self):
        return f"SerialGenerator: start={self.start}"

    def generate(self):
        """Return serial number"""

        self.nextNum += 1
        return self.nextNum - 1

    def reset(self):
        """Reset number"""

        self.nextNum = self.start
    


