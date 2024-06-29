class RL:

    counter = 1

    def __init__(self, name, rank, peak_rank, MMR):

        self.id = RL.counter
        RL.counter += 1

        self.XP = []

        self.name = name
        self.rank = rank
        self.peak_rank = peak_rank
        self.MMR = MMR

    def print_info(self):
        print(f"Username: {self.name}")
        print(f"Rank: {self.rank}")
        print(f"Peak rank: {self.peak_rank}")
        print(f"MMR: {self.MMR}")

        print()
        print("XP level: ")
        for XP in self.XP:
            print(f"{XP.level}")

    def MMR_change(self, points):
        self.MMR += points

    def add_XP(self, p):
        self.XP.append(p)
        p.rl_id = self.id

class XP:
    def __init__(self, level):
        self.level = level

def main():

    rl1 = RL(name="Iced-post2", rank="Diamond 1", peak_rank="Diamond 3", MMR=1080)

    Bob = XP(level=2365)
    Sam = XP(level=1000)
    Henry = XP(level=1687)

    rl1.add_XP(Bob)
    rl1.add_XP(Sam)
    rl1.add_XP(Henry)

    rl1.print_info()

if __name__ == "__main__":
    main()

