from typing import Dict


class InstanceManager:
    """ singleton class for managing all instances in lib """
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, dict: Dict[str, object] = {}):
        if not self._initialized:
            self.dict = dict
            self._initialized = True

    def registerObject(self, kay: str, obj: object) -> None:
        self.dict[kay] = obj

    def getObject(self, kay: str) -> object:
        return self.dict[kay]
