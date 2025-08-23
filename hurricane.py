# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
conversion = {"M": 1000000,
             "B": 1000000000}

# test function by updating damages
def convert_damages_data(damages):
    conversion = {"M": 1_000_000, "B": 1_000_000_000}
    updated_damages = []

    for damage in damages:
        if damage == "Damages not recorded":
            updated_damages.append(damage)
        elif "M" in damage:
            updated_damages.append(float(damage[:-1]) * conversion["M"])
        elif "B" in damage:
            updated_damages.append(float(damage[:-1]) * conversion["B"])
    return updated_damages


print(convert_damages_data(damages))


# 2 
# Create a Table
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    """Construct a dictionary of hurricanes with nested details."""
    hurricanes = {}

    for i in range(len(names)):
        hurricanes[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damage": damages[i],
            "Deaths": deaths[i]
        }
    
    return hurricanes
# Create and view the hurricanes dictionary
hurricanes=create_hurricane_dict(names,months,years,max_sustained_winds, areas_affected, damages, deaths)

# 3
# Organizing by Year
def organize_by_year(hurricanes_by_name):
    """Convert hurricane dictionary (key = name) into dictionary (key = year)."""
    hurricanes_by_year = {}

    for hurricane in hurricanes_by_name.values():
        year = hurricane["Year"]

        # If year not in dictionary yet, create a new empty list
        if year not in hurricanes_by_year:
            hurricanes_by_year[year] = []

        # Append hurricane dictionary to the list for that year
        hurricanes_by_year[year].append(hurricane)

    return hurricanes_by_year

# create a new dictionary of hurricanes with year and key
by_year=organize_by_year(hurricanes)

# 4
# Counting Damaged Areas
def count_affected_areas(hurricanes_by_name):
    """Count how often each area is affected by hurricanes."""
    area_counts = {}

    for hurricane in hurricanes_by_name.values():
        for area in hurricane["Areas Affected"]:
            if area not in area_counts:
                area_counts[area] = 1
            else:
                area_counts[area] += 1

    return area_counts
# create dictionary of areas to store the number of hurricanes involved in
affected_areas=count_affected_areas(hurricanes)
print(affected_areas)

# 5 
# Calculating Maximum Hurricane Count
def most_affected_area(area_counts):
    """Find the area most frequently affected by hurricanes."""
    max_area = None
    max_count = 0

    for area, count in area_counts.items():
        if count > max_count:
            max_area = area
            max_count = count

    return max_area, max_count
# find most frequently affected area and the number of hurricanes involved in
max_area, max_area_count = most_affected_area(affected_areas)
print(max_area, max_area_count)

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricanes_by_name):
    """Find the hurricane that caused the greatest number of deaths."""
    max_deaths = 0
    deadliest = None

    for name, hurricane in hurricanes_by_name.items():
        if hurricane["Deaths"] > max_deaths:
            max_deaths = hurricane["Deaths"]
            deadliest = name

    return deadliest, max_deaths

# find highest mortality hurricane and the number of deaths
deadliest,most_deaths=deadliest_hurricane(hurricanes)

print(deadliest, most_deaths)
# 7
# Rating Hurricanes by Mortality

def rate_by_mortality(hurricanes_by_name, mortality_scale):
    """Group hurricanes by mortality rating."""
    hurricanes_by_mortality = {rating: [] for rating in range(6)}  # 0–5 ratings

    for hurricane in hurricanes_by_name.values():
        deaths = hurricane["Deaths"]

        # Determine mortality rating
        if deaths == 0:
            rating = 0
        elif deaths <= mortality_scale[1]:
            rating = 1
        elif deaths <= mortality_scale[2]:
            rating = 2
        elif deaths <= mortality_scale[3]:
            rating = 3
        elif deaths <= mortality_scale[4]:
            rating = 4
        else:
            rating = 5

        # Store hurricane under this rating
        hurricanes_by_mortality[rating].append(hurricane)

    return hurricanes_by_mortality




# categorize hurricanes in new dictionary with mortality severity as key
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
mortality_rating=rate_by_mortality(hurricanes,mortality_scale)

print(mortality_rating[5])

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
canes_with_damages = {}
for cane in hurricanes:
    cane_damages = hurricanes[cane]["Damage"]
    if cane_damages != 'Damages not recorded':
        multiplier = 1
        if cane_damages.endswith('B'):
            multiplier = conversion["B"]
        elif cane_damages.endswith('M'):
            multiplier = conversion["M"]

        canes_with_damages[cane] = float(cane_damages[:-1]) * multiplier

print(canes_with_damages)
# find highest damage inducing hurricane and its total cost
def highest_damage(hurricanes):
    max_damage_value = max(hurricanes.values())
    return max_damage_value

most_costly_cane = highest_damage(canes_with_damages)
print(most_costly_cane)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def hurricanes_by_damage(damages):
    ratings = {}
    damage_scale = {
        0: 0,
        1: 100000000,
        2: 1000000000,
        3: 10000000000,
        4: 50000000000}
    for scale in damage_scale:
        ratings[scale] = ['No records']
    for damage in damages:
        for scale in damage_scale:
            upper_bound = damage_scale[scale]
            if (damages[damage] <= upper_bound):
                if 'No records' in ratings[scale][0]:
                    ratings[scale].remove('No records')
                ratings[scale].append(hurricanes[damage])
                break
            elif scale == max(damage_scale.keys()):
                ratings[5] = []
                ratings[5].append(hurricanes[damage])
    return ratings

hurricanes_by_damage = hurricanes_by_damage(canes_with_damages)
print(hurricanes_by_damage[1])
