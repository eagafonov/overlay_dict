class overlay_dict:
    def __init__(self):
        self._layers = [dict()]

    @property
    def top(self):
        return self._layers[-1]

    def push_layer(self):
        self._layers.append(dict())

    def pop_layer(self):
        self._layers.pop()

    def __setitem__(self, key, item):
        self.top[key] = item

    def __getitem__(self, key):
        for l in reversed(self._layers):
            if key in l:
                return l[key]

        raise KeyError(key)
