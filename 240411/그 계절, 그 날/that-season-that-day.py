def is_leap_year(year):
    if (year%4 == 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) or not (year % 4 == 0 and year % 100 == 0):
        return True
    return False

def get_season(year, month, day):
    seasons = {
        (3, 4, 5): "Spring",
        (6, 7, 8): "Summer",
        (9, 10, 11): "Fall",
        (12, 1, 2): "Winter"
    }
    
    if month > 12 or day > 31:
        return -1
    
    if month == 2 and day > 29:
        return -1
    
    if month == 2 and day == 29 and is_leap_year(year):
        return "Winter"
    
    for season_months, season_name in seasons.items():
        if month in season_months:
            return season_name

# Read input
year, month, day = map(int, input().split())

# Get season
print(get_season(year,month,day))