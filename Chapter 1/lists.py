# lists.py

movies1 = ["The Holy Grail",
           "The Life of Brian",
           "The Meaning of Life",
           "Ex-Machina"]
movies1.insert(1, 1975)
movies1.insert(3, 1979)
movies1.insert(5, 1983)
movies1.insert(7, 2014)
 
movies2 = ["The Holy Grail", 1975,
          "The Life of Brian", 1979,
          "The Meaning of Life", 1983]

for movie in movies1:
    print(movie)
