import json
file = open('drivers.json')
data_drivers = json.load(file)
#*print(data_drivers['drivers']['VER'])

file2= open('races.json')
data_races= json.load(file2)


drivers_points={

}

raceNumber_points={

}
#adds drivers and their points into a dict
for driver in data_drivers['drivers']:
    drivers_points[data_drivers['drivers'][driver]['name']]=data_drivers['drivers'][driver]['points']
i=1
for race in data_races['races']:
    raceNumber_points[i]=data_races['races'][race]['max_points']
    i+=1


#* Get the first key in the dictionary.(name of the elad driver)
lead_driver = next(iter(drivers_points))

round_completed=int(input("Which was the latest completed round number: "))
j=1
to_delete=[]
#deletes all the past races
for race in raceNumber_points:
    if j<=round_completed:
        to_delete.append(j)
        j+=1
for race in to_delete:
    raceNumber_points.pop(race)

second_driver = next(iter([driver for driver in drivers_points.keys() if driver != lead_driver]))
gap_to_second = drivers_points[lead_driver] - drivers_points[second_driver]


possible_points=0
l=round_completed+1
for race in raceNumber_points:
    possible_points+=raceNumber_points[l]

#calculates the possible points
drivers_in_championship=[]

elimintaed_drivers=[]
for driver in drivers_points:
    if driver!=lead_driver:
        gap=drivers_points[lead_driver]-drivers_points[driver]

        if gap<possible_points:
            drivers_in_championship.append(driver)
            
        else:
            elimintaed_drivers.append(driver)

if len(drivers_in_championship)==0:
    print(f"{lead_driver} has won the championship")
else:
    print(f'{lead_driver} needs to outscore {second_driver} by {possible_points-gap_to_second} points to win the championship')
    print("""
    Drivers who can still win
    """)
    for driver in drivers_in_championship:
        print(driver)
    '''
    print("""
    Drivers who are eliminated
    """)
    for driver in elimintaed_drivers:
        print(driver)
    '''

