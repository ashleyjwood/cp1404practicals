FILENAME = "wimbledon.csv"


def main():
    """Print a list of champion names, how many wins they have, and which countries have won. """
    data = load_data()
    champions = get_champions(data)
    print_countries_and_champions(data, champions)


def load_data():
    """Read Wimbledon championship data from file."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        return [line.strip().split(',') for line in in_file]


def get_champions(data):
    """Extract champion names and count their wins."""
    champions = {}
    for line in data[1:]:
        champion = line[2]
        champions[champion] = champions.get(champion, 0) + 1
    return champions


def print_countries_and_champions(data, champions):
    """
    Print the champions and their corresponding wins count.
    Print countries which have had champions.
    """
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    champions = {row[2] for row in data[1:]}
    countries = {row[1] for row in data[1:] if row[2] in champions}
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
