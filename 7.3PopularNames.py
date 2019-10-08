def readgirlsnames_fromfiletolist(filename):
    girlsnamesfile = open(filename, 'r')
    girlsnameslist = []

    girlname = girlsnamesfile.readline()

    while girlname != "":
        girlname = girlname.rstrip('\n')  # strip \n from each name by using r strip
        # girlsnameslist.append(girlname) NEED??
        girlname = girlsnamesfile.readline()

    return girlsnameslist


def readboyssnames_fromfiletolist(filename):
    boysnamesfile = open(filename, 'r')
    boysnameslist = []

    boyname = boysnamesfile.readline()

    while boyname != "":
        boyname = boyname.rstrip('\n')  # strip \n from each name by using r strip
        # boysnameslist.append(boyname) NEED??
        boyname = boysnamesfile.readline()

    return boysnameslist


def get_user_search_names():
    user_search_name = input("What popular name are you looking for? ")
    usersearchname_list = []

    while user_search_name != '-1':
        user_search_name.append(user_search_name)
        user_search_name = input("Please enter the next name to look for or -1 to continue: ")

    return usersearchname_list


def search_for_names(usersearchname_list, complete_names_list):
    foundnames = []
    for usersearchname_listindex in range(len(usersearchname_list)):
        if usersearchname_list[usersearchname_listindex] in complete_names_list:
            foundnames.append(usersearchname_list[usersearchname_listindex])

    return foundnames


def printsearchresults(usersearchnames_list, foundnames):
    for usersearchnames_listindex in range(len):
        if usersearchnames_list[usersearchnames_listindex] in foundnames:
            print(usersearchnames_list[usersearchnames_listindex], "was found on the popular list. ")
    else:
        print(usersearchnames_list[usersearchnames_listindex], "is so beautifully different, it was not found" +
              "on this names list. ")


def main():
    girlsfilename = 'girlsnames.txt'
    boysfilename = 'boysnames.txt'

    girlsnameslist = readgirlsnamesfromfiletolist(girlsfilename)

    boysnameslist = readboysnamesfromfiletolist(boysfilename)

    complete_names_list = girlsnameslist + boysnameslist

    usersearchnames_list = get_user_search_names()

    foundnames_list = search_for_names(usersearchnames_list, complete_names_list)


main()

"""
# Read files into lists
# Strip \n from file values
# Search for values in lists

# Import the two Boy/Girl lists from the Module/assignment submission page. Add to your project file.
# Write a program that reads the contents of the two files into two separate lists. The user should be able
# to enter a boy's name or girl's name. The application should check both lists, and then display messages
# indicating whether the names were among the most popular if the name was on one of the lists or that the name
# was not on the list of popular names.

"""
