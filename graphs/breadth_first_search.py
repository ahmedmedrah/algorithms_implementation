## credits to "grokking algorthms" book
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# silly function checks if the person's name ends with 'm'
def is_mango_seller(p):
    if p[-1] == 'm':
        return True
    return False    

def bfs(start, g):
    # create a queue of nodes to search
    to_search = deque(g[start])

    # keep history of searched nodes
    searched = [start]

    # while still have nodes to search
    while to_search:

        # get the next person in queue
        person = to_search.popleft()

        # if the person is not searched before
        if not person in searched:

            # check a person is a mango seller
            if is_mango_seller(person):
                print(f'{person} is mango seller')
                return True
            # else add that person to the history
            else:
                searched.append(person)
                # and add his neighbours to the search queue
                to_search += g[person]
    return False

bfs('you',graph)                    