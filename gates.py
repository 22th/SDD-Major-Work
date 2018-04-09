import random

# A nifty overrides decorator: http://stackoverflow.com/a/8313042
def overrides(interface_class):
    def _overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return _overrider

def trueFalseToOnesAndZeroes(x):
    """ Convert True to 1 and False to 0 """
    if x:
        return 1
    return 0

class GateException(Exception):
    def __init__(self, msg):
        super(GateException, self).__init__(msg)

class Pin(object):
    """ 
    A Pin has a binary value (either True or False). Subclasses should override the setValue() method
    to perform other actions when a value is set.
    """
    def __init__(self):
        self._value = False

    @property
    def value(self):
        return self._value

    @value.setter 
    def value(self, val):
        self.setValue(val)

    def setValue(self, value):
        raise NotImplementedError("Don't instantiate this base class (%s)" % self.__class__.__name__)

class InputPin(Pin):
    """ 
    An InputPin is associated with a particular Gate.
    When an InputPin's value is updated, the pin tells the gate to refresh its output.
    """
    def __init__(self, gate):
        super(InputPin, self).__init__()
        self.gate = gate

    @overrides(Pin)
    def setValue(self, value):
        self._value = bool(value)
        self.gate.refreshOutputs()

class OutputPin(Pin):
    """
    An OutputPin may be connected to other Pins.
    When an OutputPin's value is updated, the pin passes the value along
    to all the pins to which it is connected.
    """
    def __init__(self):
        super(OutputPin, self).__init__()
        self.connections = set()

    @overrides(Pin)
    def setValue(self, value):
        self._value = bool(value)
        for pin in self.connections:
            pin.setValue(self._value)

    def addConnection(self, pin):
        self.connections.add(pin)

class Gate(object):
    """ 
    This defines a base class for logic gates.
    A Gate has a number of input pins and a number of output pins, indexed from 0.
    Inputs and outputs are either True or False.
    Subclasses need to override the refreshOutputs() method
    """

    def __init__(self, nInputs = 0, nOutputs = 0):
        self._inputs = [InputPin(self) for i in xrange(nInputs)]
        self._outputs = [OutputPin() for i in xrange(nOutputs)]

    @property
    def nInputs(self):
        return len(self._inputs)

    @property
    def nOutputs(self):
        return len(self._outputs)

    def setIn(self, index, value):
        """ Set the value of an input pin """
        self.getInPin(index).value = value

    def getIn(self, index):
        """ Get the value of an input pin """
        return self.getInPin(index).value

    def getOut(self, index):
        """ Get the current value of an output pin """
        self.getOutPin(index).value

    def getInPin(self, index):
        if 0 <= index < len(self._inputs):
            return self._inputs[index]
        raise GateException("No input pin %s on this gate (%s)." % (index, self.__class__.__name__))

    def getOutPin(self, index):
        if 0 <= index < len(self._outputs):
            return self._outputs[index]
        raise GateException("No output pin %s on this gate (%s)." % (index, self.__class__.__name__))

    def setInPin(self, index, pin):
        if 0 <= index < len(self._inputs):
            self._inputs[index] = pin
        else:
            raise GateException("No input pin %s on this gate (%s)." % (index, self.__class__.__name__))

    def setOutPin(self, index, pin):
        if 0 <= index < len(self._outputs):
            self._outputs[index] = pin
        else:
            raise GateException("No output pin %s on this gate (%s)." % (index, self.__class__.__name__))

    def _setOut(self, index, value):
        if 0 <= index < len(self._outputs):
            self._outputs[index].value = value
        else:
            raise GateException("No output pin %s on this gate (%s)." % (index, self.__class__.__name__))

    def refreshOutputs(self):
        """ Reimplement in subclass """
        raise NotImplementedError("Don't instantiate this base class")

    def __str__(self):
        return "%s<In=%s Out=%s>" % (self.__class__.__name__, 
            map(lambda pin: trueFalseToOnesAndZeroes(pin.value), self._inputs),
            map(lambda pin: trueFalseToOnesAndZeroes(pin.value), self._outputs))

    def __repr__(self):
        return str(self)

class And(Gate):
    def __init__(self):
        super(And, self).__init__(2, 1)

    @overrides(Gate)
    def refreshOutputs(self):
        self._setOut(0, all(map(lambda pin: pin.value, self._inputs)))

class Or(Gate):
    def __init__(self):
        super(Or, self).__init__(2, 1)

    @overrides(Gate)
    def refreshOutputs(self):
        self._setOut(0, any(map(lambda pin: pin.value, self._inputs)))

class Not(Gate):
    def __init__(self):
        super(Not, self).__init__(1, 1)

    @overrides(Gate)
    def refreshOutputs(self):
        self._setOut(0, not self._inputs[0].value)

class Xor(Gate):
    def __init__(self):
        super(Xor, self).__init__(2, 1)

    @overrides(Gate)
    def refreshOutputs(self):
        self._setOut(0, self._inputs[0].value ^ self._inputs[1].value)

class TwoGateChain(Gate):
    """ A chain of two gates. """
    def __init__(self, a, b):
        super(TwoGateChain, self).__init__()
        self.a = a
        self.b = b
        if a.nOutputs != b.nInputs:
            raise GateException("Cannot connect %s output pins to %s input pins" % (a.nInputs, b.nOutputs))
        self._inputs.extend(self.a._inputs)
        self._outputs.extend(self.b._outputs)
        for i in xrange(a.nOutputs):
            self.a.getOutPin(i).addConnection(self.b.getInPin(i))

class Nand(TwoGateChain):
    def __init__(self):
        super(Nand, self).__init__(And(), Not())

class Nor(TwoGateChain):
    def __init__(self):
        super(Nor, self).__init__(Or(), Not())

class Xnor(TwoGateChain):
    def __init__(self):
        super(Xnor, self).__init__(Xor(), Not())

def cross(x, size):
    if size <= 1:
        return [[a] for a in x]
    result = [[a, b] for a in x for b in x]
    for n in xrange(size - 2):
        result = [a + [b] for a in result for b in x]
    return result

def enumeratePins(gate):
    for pins in cross([0, 1], gate.nInputs):
        for pin, val in enumerate(pins):
            gate.setIn(pin, val)
        print gate

class Fan(Gate):
    """ Copies a single input to multiple outputs. """
    def __init__(self, nOutputs):
        super(Fan, self).__init__(1, nOutputs)

    @overrides(Gate)
    def refreshOutputs(self):
        for i in xrange(len(self._outputs)):
            self._outputs[i].value = self._inputs[0].value
