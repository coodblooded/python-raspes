from observer import AbcObserver
import abc

class AbcSubject(metaclass= abc.ABCMeta):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbcObserver):
            raise TabError('Observer not derived from AbsObservation')

        self._observers |= { observer }

    def detach(self, observer):
        self._observers -= { observer }

    def notify(self, value = None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)