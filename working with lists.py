#here is a tutorial on working with lists
lucky_numbers =[2,15,7,4,9,11,11]
friends =["Collins", "Wawish", "Brian", "Njogu", "Flo", "Flo", "Joy"]
print(friends)
print(friends[2:]) #prints elements from second index onwards
print(friends[2:5]) #prints elements from first index to fifth(but not including fifth)
#inserting a new element to the list
    # At the end-usng append fn
friends.append("Joseph")
print(friends)
friends.append("Maurice")
print(friends)

#inserting a new element to the list
    # At esired place-usng insert fn
friends.insert(6,"Christine")
print(friends)
friends.insert(7,"Jonah")
print(friends)

# deleting an element from the list
#use remove fn
friends.remove("Jonah")
print(friends)

# deleting an elements from the end of the list
#use pop fn
friends.pop()
print(friends)


# deleting all elements from the list
#use clear fn
friends.clear()
print(friends)


#To find out no of times an element in the list has been repeated 
#Use count fn
lucky_numbers.count(11)
print(lucky_numbers)

#To sort a list
lucky_numbers.sort()
print(lucky_numbers)

#sorting a list in reverse
lucky_numbers.reverse()
print(lucky_numbers)

#To find out whether an element is in the list 
#Use index fn
print(friends.index("Japheth"))










