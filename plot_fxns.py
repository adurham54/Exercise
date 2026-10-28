# function definitions for plotting
# to import - from plotting_fxns import *
# build dictionary: needs str as input.
import matplotlib.pyplot as plt
def build_dict(words):
    d = dict()
    for char in words:
        d[char] = d.get(char,0) + 1
    return d

# build histogram: nothing to return
def plot_histo(data, n):
    plt.hist(data,bins=n)
    plt.ylabel('Counts')
    plt.title('Frequency of letters') 
    plt.show()

#build bar graph: nothing to return
def plot_bar(d, plot_title):
    plt.bar(list(d.keys()), d.values())
    plt.ylabel('Counts')
    plt.title(plot_title) 
    plt.show()
