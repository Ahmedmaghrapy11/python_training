# list of states we want to cover
states_needed = set(["mt" , "wa" , "or", "id" , "nv" , "ut" , "ca" , "az"])
# a dictionary for the stations to choose from
# the keys are the station names and the values are the states they cover
stations ={
    "kOne" : set(["id" , "nv" , "ut"]),
    "kTwo" : set(["wa" , "id" , "mt"]),
    "kThree" : set(["or" , "nv" , "ca"]),
    "kFour" : set(["nv" , "ut"]),
    "kFive" : set(["ca" , "az"])
}

# final set of stations we will use
final_stations = set()

# loop over the stations dictionary to get the best station
while states_needed:
    best_station =None
    states_covered = set()
    for station , states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

# update states needed
states_needed -= states_covered

# add the best station for the final station set
final_stations.add(best_station)

# printing the final stations
print(final_stations)