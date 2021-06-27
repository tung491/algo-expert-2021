def valid_starting_city(distances, fuel, mpg):
    available_miles = 0
    min_gas = 0
    min_city = 0

    for i, dist in enumerate(distances[1:], start=1):
        available_miles += fuel[i - 1] * mpg - distances[i - 1]
        if available_miles < min_gas:
            min_gas = available_miles
            min_city = i
    return min_city


if __name__ == '__main__':
    distances = [1, 3, 10, 6, 7, 7, 2, 4]
    fuel = [1, 1, 1, 1, 1, 1, 1, 1]
    mpg = 5
    print(f"The acutal result: {valid_starting_city(distances, fuel, mpg)}. Expected: {6}")