class Rl:

    def __init__(self, name, rank, peak_rank, MMR):
        self.name = name
        self.rank = rank
        self.peak_rank = peak_rank
        self.MMR = MMR

    def print_info(self):
        print(f"Username: {self.name}")
        print(f"Rank: {self.rank}")
        print(f"Peak rank: {self.peak_rank}")
        print(f"MMR: {self.MMR}")

def main():
    rl1 = Rl(name="Iced-post2", rank="Diamond 1", peak_rank="Diamond 3", MMR=1080)
    rl1.print_info()

    rl2 = Rl(name="musty", rank="Supersonic legend", peak_rank="No data", MMR=2050)
    rl2.print_info()

if __name__ == "__main__":
    main()

