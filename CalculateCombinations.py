from Constants import *
import pickle
import os

chunk = 100.0/len(RACERS)
percentage = 0
combinations = []

for racer in RACERS:
    print '%s' % round(percentage, 2) + "%"
    for kart in KARTS:
        for wheel in WHEELS:
            for glider in GLIDERS:
                combinations.append(racer + kart + wheel + glider)
    percentage += chunk
print '%s %d %s' % ("Compilation complete;", len(combinations), "combinations found.")

print '%s %s%s' % ("Pickling combinations to", os.getcwd(), os.sep + "combination_data.pkl...")
pickle.dump(combinations, open('combination_data.pkl', 'wb'))
