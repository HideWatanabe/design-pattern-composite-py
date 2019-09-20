from abc import ABC, abstractmethod

class SoccerPlayer(ABC):
    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    def shoot(self):
        pass

class Forward(SoccerPlayer):
    def shoot(self):
        print(f"{self.name} has shooted and... Goooallll!!!")

class Defender(SoccerPlayer):
    def shoot(self):
        print(f"{self.name} has shooted and... What a mess!!!")

if __name__ == "__main__":
    ronaldo = Forward("Ronaldo")
    pepe = Defender("Pepe")

    ronaldo.shoot()
    pepe.shoot()