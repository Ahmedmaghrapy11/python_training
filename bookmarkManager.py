# make a list for the websites
myFavouriteWebsites = []

# maximum allowed websites
maximumWebs = 5

while maximumWebs > 0:
    # input the websites
    web = input("Enter your favourite websites without https:// -> ")
    # add the website to the list
    myFavouriteWebsites.append(f"https://{web.strip().lower()}")
    # decrement the maximum webs by one
    maximumWebs -= 1
    print(f"Website is added!\n{maximumWebs} places left in the list!")
    print(myFavouriteWebsites)
else:
    print("Bookmark is full!")

#check if the list is not empty
if len(myFavouriteWebsites) > 0:
    # sort the list
    myFavouriteWebsites.sort()

    # printing websites
    index = 0
    print("Printing websites in your bookmarks:")
    while index < len(myFavouriteWebsites):
        print(myFavouriteWebsites[index])
        index += 1
        