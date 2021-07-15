# with credits to "Grokking Algorithms" book

states_needed = set(["a", "b", "c", "d", "e", "f", "g", "h"])

stations = {}
stations["Cairo"] = set(["d", "e", "f"])
stations["Alexandria"] = set(["b", "d", "a"])
stations["ismaillia"] = set(["c", "e", "g"])
stations["Al Buheira"] = set(["e", "f"])
stations["Aswan"] = set(["g", "h"])

final_stations = set()

# while there are states left to cover
while states_needed :
    best_station = None
    covered_states = set()
    # find the best station that covers the most number of states
    for station, states in stations.items():
        # get the intersection between the the states we need to cover and the states that the station covers
        covered = states & states_needed  
        if len(covered) > len(covered_states):
            best_station = station
            covered_states = covered
    # update the states need to be covered by removing what is already covered
    states_needed.difference_update(covered_states)
    # add the best station to our soulution
    final_stations.add(best_station)

print(final_stations)    
