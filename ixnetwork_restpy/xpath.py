

class Xpath(object):

    def __init__(self):
        self._config = []
        self._children = []
        self._mode = 'normal'

    @property
    def config(self):
        return self._config
