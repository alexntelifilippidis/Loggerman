from src.loggerman.singleton import SingletonMeta

class ExampleSingleton(metaclass=SingletonMeta):
    pass

def test_creates_single_instance() -> None:
    instance1 = ExampleSingleton()
    instance2 = ExampleSingleton()
    assert instance1 is instance2

def test_handles_multiple_classes_independently() -> None:
    class AnotherSingleton(metaclass=SingletonMeta):
        pass

    instance1 = ExampleSingleton()
    instance2 = AnotherSingleton()
    assert instance1 is not instance2

def test_allows_arguments_on_initialization() -> None:
    class SingletonWithArgs(metaclass=SingletonMeta):
        def __init__(self, value):
            self.value = value

    instance1 = SingletonWithArgs(value=42)
    instance2 = SingletonWithArgs(value=99)
    assert instance1 is instance2
    assert instance1.value == 42