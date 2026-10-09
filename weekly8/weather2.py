def main():
    day1 = [26,26,26,2524,23,21,21]
    day2 = [20,19,19,18,18,17,17,16,16,18,20,22,24,25,26,27,27,27,27,26,25,23,22,21,20]
    day3 = [19, 18, 18, 17, 16, 16, 16, 16, 17, 20, 22, 23, 25, 26, 26, 27]
    # TO-DO: Define day1, day2, and day3 lists here
    # TO-DO: Print daily headers and call max_temperature / min_temperature

    print("Today")
    max_temperature(day1)
    min_temperature(day1)

    def max_temperature(temperatures):
        highest_temp = temperatures[0]
        for hour in temperatures:
            if hour > highest_temp:
                highest_temp = hour
        print(f"High {highest_temp}°")
        # TO-DO: Find and print the highest temperature in the list

    def min_temperature(temperatures):
        lowest_temp = temperatures[0]
        for hour in temperatures:
            if hour < lowest_temp:
                lowest_temp = hour
        print(f"low {lowest_temp}°")

    # TO-DO: Find and print the lowest temperature in the list

    print("Tomorrow")
    max_temperature(day2)
    min_temperature(day2)

    def max_temperature(temperatures):
        highest_temp = temperatures[0]
        for hour in temperatures:
            if hour > highest_temp:
                highest_temp = hour
        print(f"High {highest_temp}°")
        # TO-DO: Find and print the highest temperature in the list

    def min_temperature(temperatures):
        lowest_temp = temperatures[0]
        for hour in temperatures:
            if hour < lowest_temp:
                lowest_temp = hour
        print(f"low {lowest_temp}°")

    # TO-DO: Find and print the lowest temperature in the list

    print("The day after tomorrow")
    max_temperature(day3)
    min_temperature(day3)

def max_temperature(temperatures):
    highest_temp = temperatures[0]
    for hour in temperatures:
        if hour > highest_temp:
            highest_temp = hour
    print(f"High {highest_temp}°")
    # TO-DO: Find and print the highest temperature in the list

def min_temperature(temperatures):
    lowest_temp = temperatures[0]
    for hour in temperatures:
        if hour < lowest_temp:
            lowest_temp = hour
    print(f"low {lowest_temp}°")

    # TO-DO: Find and print the lowest temperature in the list

if __name__ == "__main__":
    main()
