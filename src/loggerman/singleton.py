from typing import Any, Dict, Type


class SingletonMeta(type):
    """
    Metaclass for implementing the Singleton pattern.

    Ensures that only one instance of a class using this metaclass
    is created. Subsequent instantiations return the same instance.

    :cvar _instances: Stores instances of singleton classes keyed by class.
    :type _instances: Dict[Type, Any]
    """

    _instances: Dict[Type[Any], Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """
        Call method to control instance creation.

        :param args: Positional arguments for the class constructor.
        :type args: tuple
        :param kwargs: Keyword arguments for the class constructor.
        :type kwargs: dict
        :return: The singleton instance of the class.
        :rtype: Any
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]