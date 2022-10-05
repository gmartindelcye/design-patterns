class User:
    # methods
    def __init__(self, name: str = '') -> None:
        self.name = name


    def sayHello(self) -> None:
        print(f"Hi, my name is {self.name}")