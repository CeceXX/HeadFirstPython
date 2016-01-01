# forin-if.py

movies = ["The Holy Grail",
          1975,
          "Terry Jones & Terry Gilliam",
          91,
          ["Graham Chapman", ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]

for item in movies:
    if isinstance(item, list):
        for sub_item in item:
            if isinstance(sub_item, list):
                for sub_sub_item in sub_item:
                    print(sub_sub_item)
            else:
                print(sub_item)
    else:
        print(item)

