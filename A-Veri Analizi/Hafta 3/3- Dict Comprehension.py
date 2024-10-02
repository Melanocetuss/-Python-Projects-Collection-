#Dict Comprehension

dictionary = {"a":1,
              "b":2,
              "c":3,
              "d":4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v**2 for (k,v) in dictionary.items()}

{k.upper():v for (k,v) in dictionary.items()}

{k.upper():v**2 for (k,v) in dictionary.items()}

