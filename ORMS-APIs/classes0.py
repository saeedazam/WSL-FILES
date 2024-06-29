class Rl:

    def __init__(self, name, rank, peak_rank, MMR):
        self.name = name
        self.rank = rank
        self.peak_rank = peak_rank
        self.MMR = MMR

def main():

    f = Rl(name="Iced-post2", rank="Diamond 1", peak_rank="Diamond 3", MMR=1080)

    f.MMR += 15

    print(f.name)
    print(f.rank)
    print(f.peak_rank)
    print(f.MMR)

if __name__ == "__main__":
    main()
