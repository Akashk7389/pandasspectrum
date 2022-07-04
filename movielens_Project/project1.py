import numpy as np
import pandas as pd 
import csv

# movies = np.loadtxt('movies.dat', unpack = True)
# print(movies)

df = pd.read_csv("movies.dat", sep="\t",engine="python")
print (df)