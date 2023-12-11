"""
CP1404/CP5632 Practical - Saranraj Saravanan
My Guitar

"""
import csv

from guitar import Guitar

def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            name, year, cost = line
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("Original list of guitars:")
    display_guitars(guitars)

    # Sorting by year
    guitars.sort()

    print("\nSorted list of guitars by year:")
    display_guitars(guitars)


def get_user_input():
    name = input("Enter the guitar name: ")
    year = int(input("Enter the year: "))
    cost = float(input("Enter the cost: "))
    return Guitar(name, year, cost)

def add_guitar(guitars, new_guitar):
    guitars.append(new_guitar)

def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("Original list of guitars:")
    display_guitars(guitars)

    # Sorting by year
    def __lt__(self, other):
        # Compare Guitars based on the 'year' attribute
        return self.year < other.year

    print("\nSorted list of guitars by year:")
    display_guitars(guitars)

    # Adding new guitars
    new_guitar = get_user_input()
    add_guitar(guitars, new_guitar)

    # Saving the updated list to the data file
    save_guitars(filename, guitars)

    # Displaying the updated list
    print("\nUpdated list of guitars:")
    display_guitars(guitars)

if __name__ == "__main__":
    main()
