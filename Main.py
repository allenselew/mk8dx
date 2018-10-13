import pickle

print "Loading combination data..."
combinations = pickle.load(open("combination_data.pkl", "rb"))

print "%d %s" % (len(combinations), "combinations loaded.")
