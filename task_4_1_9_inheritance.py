class Layer:
    def __init__(self):
        self.name = 'Layer'
        self.next_layer = None

    def __call__(self, obj: 'Layer'):
        if obj:
            self.next_layer = obj
            return self.next_layer


class Input(Layer):
    def __init__(self, inputs: int):
        super().__init__()
        self.inputs = inputs
        self.name = 'Input'


class Dense(Layer):
    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = 'Dense'


class NetworkIterator:
    def __init__(self, obj: 'Layer'):
        self.first_layer = obj

    def __iter__(self):
        pointer = self.first_layer
        while pointer:
            yield pointer
            pointer = pointer.next_layer


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer1 = layer(Dense(layer.inputs, 10, 'softmax'))
p = NetworkIterator(network)
for i, v in enumerate(p):
    print(i, v.name)
for i, v in enumerate(p):
    print(i, v.name)

nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0
for x in NetworkIterator(nt):
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"