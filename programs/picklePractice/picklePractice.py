
import pickle

a = { "lion": "yellow", "kitty": "red" }

with open('filename.pickle', 'wb') as handle:
	pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)


print(a == b)