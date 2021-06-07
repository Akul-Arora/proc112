import csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random
import pandas as pd

df=pd.read_csv("temp.csv")
print(df)
data=df["temp"].tolist()
temp_mean= statistics.mean(data)
temp_stddev=statistics.stdev(data)
temp_median=statistics.median(data)
print("temp mean value :-",temp_mean,temp_median,temp_stddev)

def random_set_of_mean(counter):
    dataset = []  
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    temp_mean=statistics.mean(dataset)
    return temp_mean  

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)    
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines", name="MEAN GRAPH"))
    fig.show()
    
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()
population_mean = statistics.mean(data)
print("population mean:- ", population_mean)

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()    

