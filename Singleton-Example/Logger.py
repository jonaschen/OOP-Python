class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the Logger object")
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.messages = []
        return cls._instance

    def log(self, message):
        self.messages.append(message)
        print(f"[LOG]: {message}")
