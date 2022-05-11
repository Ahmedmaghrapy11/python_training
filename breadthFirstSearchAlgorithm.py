from collections import deque

#represent data in a graph...
graph = {}
graph["you"] = ["alice" , "pop" , "claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#function to check if the person is a mango seller or not...
def person_is_seller(name):
    return name[-1] == 'm'

#function to find the mango seller in a person's network...
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    already_searched = []       #array for checked items...
    while search_queue:
        person = search_queue.popleft()
        if not person in already_searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                already_searched.append(person)     #mark person as already checked...
    return False

search("you")