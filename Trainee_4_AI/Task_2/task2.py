#use pandas to work with the dataset
#matplotlib to create a scatterplot
# create a virtual environment for the dependencies
#cleaning the data: it seems that all columns have the same amount of non null items, other than removing nulls i dont really know what i should remove so i wont remove anything
# now that i'm plotting the data i see that there are some outliers messing up the data, should remove those
# ill remove values abouve 0.5 for the first plot and 1.0 for the second
# this is taking too long so ill skip it for now
# price boxplot again shows that most values are below 0.5 or maybe 0.6 (billion), with a couple outliers above that
# ill switch to task 3 since it seems easier and i want to make sure i get it done
import pandas as pd
import matplotlib.pyplot as plot
print("hello")
housedata = pd.read_csv("data.csv")
print(housedata.describe())
print(housedata.info())

yr_built = housedata["yr_built"]
floors = housedata["floors"]
price = housedata["price"]


plot.scatter(yr_built, price)
plot.title("year built vs price")
plot.show()

plot.scatter(floors, price)
plot.title("floors vs price")
plot.show()

plot.boxplot(price)
plot.title("price boxplot")
plot.show()

plot.imshow()