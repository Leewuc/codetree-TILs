def is_leap_year(year):
    if year % 4 == 0:                       # If the year is divisible by 4
        if year % 100 == 0:                 # If the year is divisible by 100
            if year % 400 == 0:             # If the year is divisible by 400
                return True                # Leap year
            else:
                return False               # Not a leap year
        else:
            return True                    # Leap year
    else:
        return False                       # Not a leap year

def count_leap_years(n):
    leap_year_count = 0
    for year in range(1, n + 1):            # Loop through years from 1 to n
        if is_leap_year(year):            # Check if the year is a leap year
            leap_year_count += 1         # Increment the leap year count
    return leap_year_count

# Example usage:
n = int(input())
leap_year_count = count_leap_years(n)
print(leap_year_count)