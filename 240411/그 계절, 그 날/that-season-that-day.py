def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def get_season(year, month, day):
    seasons = {
        (3, 4, 5): "Spring",
        (6, 7, 8): "Summer",
        (9, 10, 11): "Fall",
        (12, 1, 2): "Winter"
    }
    
    if month < 1 or month > 12 or day < 1 or day > 31:
        return -1
    
    if month == 2 and day > 29:
        return -1
    
    if month == 2 and day == 29 and not is_leap_year(year):
        return -1
    
    for season_months, season_name in seasons.items():
        if month in season_months:
            return season_name

# Read input
year, month, day = map(int, input().split())

# Get season
season = get_season(year, month, day)

# Print result
if season == -1:
    print(-1)
else:
    print(season)