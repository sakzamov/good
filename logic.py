class Rasptsania:
    raspiska = {"понедельник": "2024-12-13_20-58-03.png", "вторник": "2024-12-13_20-58-0.png", "среда": "2024-12-13_20-58-01.png", "четверг": "2024-12-13_20-58-02.png", "пятница": "2024-12-13_20-58-00.png"}
    def __init__(self, raspiska):
        self.raspiska = raspiska
    def open_raspisanea(self, day):
        raspiska = self.raspiska[day]
        return raspiska

    