import sqlite3

def main():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()

    while True:
        print("\nOperations Menu:")
        print("1. Display a list of cities sorted by population (ascending).")
        print("2. Display a list of cities sorted by population (descending).")
        print("3. Display a list of cities sorted by name.")
        print("4. Display the total population of all the cities.")
        print("5. Display the average population of all the cities.")
        print("6. Display the city with the highest population.")
        print("7. Display the city with the lowest population.")
        print("8. Exit.")

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            display_sorted_cities(cur, "Population ASC")
        elif choice == "2":
            display_sorted_cities(cur, "Population DESC")
        elif choice == "3":
            display_sorted_cities(cur, "CityName ASC")
        elif choice == "4":
            display_total_population(cur)
        elif choice == "5":
            display_average_population(cur)
        elif choice == "6":
            display_city_by_population(cur, "DESC")
        elif choice == "7":
            display_city_by_population(cur, "ASC")
        elif choice == "8":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 8.")

    conn.close()

def display_sorted_cities(cur, order_by):
    query = f"SELECT CityName, Population FROM Cities ORDER BY {order_by}"
    cur.execute(query)
    results = cur.fetchall()
    print("\nCities sorted by", order_by.split()[0], ":")
    for row in results:
        print(f"{row[0]:20} {row[1]:,.0f}")

def display_total_population(cur):
    cur.execute("SELECT SUM(Population) FROM Cities")
    result = cur.fetchone()[0]
    print(f"\nTotal population of all cities: {result:,.0f}")

def display_average_population(cur):
    cur.execute("SELECT AVG(Population) FROM Cities")
    result = cur.fetchone()[0]
    print(f"\nAverage population of all cities: {result:,.0f}")

def display_city_by_population(cur, order):
    query = f"SELECT CityName, Population FROM Cities ORDER BY Population {order} LIMIT 1"
    cur.execute(query)
    result = cur.fetchone()
    if order == "DESC":
        print(f"\nCity with the highest population: {result[0]} ({result[1]:,.0f})")
    else:
        print(f"\nCity with the lowest population: {result[0]} ({result[1]:,.0f})")

if __name__ == '__main__':
    main()