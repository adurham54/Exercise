# Noah and Amara
import matplotlib.pyplot as plt
fh = open("StudentExercise.csv")
next(fh)
exercise = list()
above_ls = list()

def plot_histo(data, n):
    plt.hist(data,bins=n)
    plt.ylabel('Counts')
    plt.title('Frequency of letters') 
    plt.show()

nums_ls = list()

def average(ls):
    for num in ls:
        if num != '':
            num = float(num)
            nums_ls.append(num)
    return sum(nums_ls)/len(nums_ls)

def prop_above(ls):
    avg = average(ls)
    for num in ls:
        if float(num) > avg:
            above_ls.append(num)
    return len(above_ls)/len(ls)
     
for line in fh:
    ex_ls = line.split(",")
    if ex_ls[0] != '':
        exercise.append(ex_ls[0])

print(exercise)
print(average(exercise))
print(prop_above(exercise))
print(len(exercise))
