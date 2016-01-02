"""
Given a list, this recorsive function prints out on the shell
the items of the list.
If there are nested lists, then this function will recurse and
iterate through the items of the list, so that all the elements
will be printed out.
"""

movies = ["The Holy Grail",
          1975,
          "Terry Jones & Terry Gilliam",
          91,
          ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

def print_lol(the_list, level=0):
    for item in the_list:
        if isinstance(item, list):
            if level != 0:
                print_lol(item, level+1)
            else:
                print_lol(item, level)
        else:
            for num in range(level):
                print("\t", end='')
            print(item)

print_lol(movies, 0)
