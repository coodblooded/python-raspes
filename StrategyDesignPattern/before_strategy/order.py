class Order(object):
    def __init__(self, shipping):
        self._shipping = shipping

    @property
    def shipper(self):
        return self._shipping