# Noah and Amara
import matplotlib.pyplot as plt
def plot_histo(data, n):
    plt.hist(data,bins=n)
    plt.ylabel('Counts')
    plt.title('Frequency of letters') 
    plt.show()
    
fh = open("StudentExercise.csv")
next(fh)
exercise = list()


for line in fh:
    ex_ls = line.split(",")
    exercise.append(ex_ls[0])

print(exercise)
