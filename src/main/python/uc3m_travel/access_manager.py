class AccessManager:
    """
    Singleton class for AccessManager that manages unique access instances.
    """
    _instances = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(AccessManager, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]
