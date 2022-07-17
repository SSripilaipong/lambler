from abc import abstractmethod, ABC


class TemplateBase(ABC):

    @classmethod
    @abstractmethod
    def load(cls, *args, **kwargs):
        pass
