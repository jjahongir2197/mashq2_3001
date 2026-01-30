class Patient:
    def __init__(self, name, problem):
        self.name = name
        self.problem = problem


class Clinic:
    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        self.queue.append(patient)

    def next_patient(self):
        if self.queue:
            p = self.queue.pop(0)
            print(f"Qabul qilindi: {p.name} | Muammo: {p.problem}")
        else:
            print("Navbat bo‘sh")

    def show_queue(self):
        for i, p in enumerate(self.queue):
            print(i, p.name, "-", p.problem)


clinic = Clinic()

while True:
    print("\n1.Bemor 2.Qabul 3.Navbat 0.Exit")
    c = input(">>> ")

    if c == "1":
        clinic.add_patient(Patient(input("Ism: "), input("Muammo: ")))
    elif c == "2":
        clinic.next_patient()
    elif c == "3":
        clinic.show_queue()
    elif c == "0":
        break
