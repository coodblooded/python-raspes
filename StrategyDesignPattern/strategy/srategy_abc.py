from abc import ABCMeta, abstractmethod

class AbsStrategy(metaclass=ABCMeta):
    @abstractmethod
    def claculate(self, order):
        """claculate shippting cost"""
        pass
