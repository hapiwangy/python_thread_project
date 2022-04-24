import pickle
# pickle example
d = {1:"Hey", 2:"There"}
msg = pickle.dumps(d)
print(msg)

# unpickle things
f = pickle.loads(msg)
print(f)