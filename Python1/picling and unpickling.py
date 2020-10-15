# Pickling
# import pickle
# l1 = [2, 3, 4, 5]
# s1 = 'Hello how are you'
# f1 = open('notes.txt', 'wb')
# pickle.dump(s1, f1)
# f1.close()


# unpickling
import pickle
un = open('notes.txt', 'rb')
print(pickle.load(un))
un.close()
