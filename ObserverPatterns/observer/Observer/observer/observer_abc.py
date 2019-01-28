import abc

class AbcObserver( metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, value):
        pass
