# 1
# Import necessary libraries
import pandas as pd
from matplotlib import pyplot as plt

# load rankings data
wood_coasters = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
# load rankings data
steel_coasters = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")
print(steel_coasters.head(5))
print(wood_coasters.head(5))

# 2
# Create a function to plot rankings over time for 1 roller coaster

def one_coaster_plot(dataframe, name, park):
    df = dataframe[(dataframe["Name"] == name) & (dataframe["Park"] == park)]
    plt.plot(df["Year of Rank"], df["Rank"], marker="o")
    plt.xlabel("Year of Rank")
    plt.ylabel("Rank")
    plt.title(f"{name} at {park}")
    plt.show()

# 3
# Create a plot of El Toro ranking over time
print(one_coaster_plot(wood_coasters, "El Toro", "Six Flags Great Adventure"))

# Create a plot of El Toro and Boulder dash hurricanes
def two_coaster_plot(dataframe_1, name_one, park_one, dataframe_2, name_two, park_two):
    df_1 = dataframe_1[(dataframe_1["Name"] == name_one) & (dataframe_1["Park"] == park_one)]
    df_2 = dataframe_2[(dataframe_2["Name"] == name_two) & (dataframe_2["Park"] == park_two)]
    plt.clf()
    plt.plot(df_1["Year of Rank"], df_1["Rank"], marker="o")
    plt.plot(df_2["Year of Rank"], df_2["Rank"], marker="o")
    plt.xlabel("Year of Rank")
    plt.ylabel("Rank")
    plt.title(f"{name_one} vs. {name_two} Ranking")
    plt.legend([name_one, name_two])
    plt.show()

print(two_coaster_plot(wood_coasters, "El Toro", "Six Flags Great Adventure", wood_coasters, "Boulder Dash",
                   "Lake Compounce"))

# 4
# Create a function to plot top n rankings over time
def plot_top_n(rankings_df,n):
  top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
  fig, ax = plt.subplots(figsize=(10,10))
  for coaster in set(top_n_rankings['Name']):
    coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
    ax.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'],label=coaster)
  ax.set_yticks([i for i in range(1,6)])
  plt.title("Top 10 Rankings")
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.legend(loc=4)
  plt.show()
  plt.clf()

# Create a plot of top n rankings over time
print(plot_top_n(wood_coasters, 5))

# 5
# load roller coaster data
coasters = pd.read_csv("roller_coasters.csv")
print(coasters.head(5))

# 6
# Create a function to plot histogram of column values
def coaster_histogram(dataframe, column):
    selected_column = dataframe[column]
    plt.clf()
    plt.hist(selected_column.dropna())
    plt.title(f"Roller Coaster Histogram: {column}")
    plt.xlabel(f"{column}")
    plt.ylabel("Count")
    plt.show()

# Create histogram of roller coaster speed
print(coaster_histogram(coasters, "speed"))

# Create histogram of roller coaster length
print(coaster_histogram(coasters, "length"))

# Create histogram of roller coaster number of inversions
print(coaster_histogram(coasters, "num_inversions"))

# Create a function to plot histogram of height values
def height_histogram(dataframe):
    df = dataframe[dataframe["height"] <= 140]['height'].dropna()
    plt.clf()
    plt.hist(df)
    plt.title("Roller Coaster Histogram: height")
    plt.xlabel("height")
    plt.ylabel("count")
    plt.show()

# Create a histogram of roller coaster height
print(height_histogram(coasters))

# 7
# Create a function to plot inversions by coaster at park
def bar_chart(dataframe, park_name):
    park_coaster = dataframe[dataframe["park"] == park_name]
    park_coaster = park_coaster.sort_values("num_inversions", ascending=False)
    coaster_name = park_coaster["name"]
    inversions = park_coaster["num_inversions"]
    plt.clf()
    plt.bar(range(len(inversions)), inversions)
    plt.xlabel("Roller Coasters")
    plt.ylabel("Number of Inversions")
    plt.title(f"Number of Inversions at {park_name}")
    ax = plt.subplot()
    ax.set_xticks(range(len(coaster_name)))
    ax.set_xticklabels(coaster_name, rotation=40)
    plt.show()

# Create barplot of inversions by roller coasters
print(bar_chart(coasters, "Holiday Park"))

# 8
# Create a function to plot a pie chart of status.operating
def pie_chart(dataframe):
    df_status_open = dataframe[dataframe["status"] == "status.operating"]
    df_status_closed = dataframe[dataframe["status"] == "status.closed.definitely"]
    count_open = len(df_status_open)
    count_closed = len(df_status_closed)
    coaster_status = [count_open, count_closed]
    plt.clf()
    plt.pie(coaster_status, autopct="%d%%")
    plt.title("Status of Roller Coaster")
    plt.legend(["Coaster Open", "Coaster Closed"], loc=1)
    plt.axis("equal")
    plt.show()

# Create pie chart of roller coasters
print(pie_chart(coasters))

# 9
# Create a function to plot scatter of any two columns
def scatterplot(dataframe, column_1, column_2):
    col_1 = dataframe[column_1]
    col_2 = dataframe[column_2]
    plt.clf()
    plt.scatter(col_1, col_2)
    plt.xlabel(column_1)
    plt.ylabel(column_2)
    plt.title(f"Scaterplot of Roller Coasters: {column_1} vs {column_2}")
    plt.show()

print(scatterplot(coasters, "length", "num_inversions"))

# Create a function to plot scatter of speed vs height
def height_scatter(dataframe):
    df = dataframe[dataframe["height"] < 140]
    plt.clf()
    plt.scatter(df["height"], df["speed"])
    plt.xlabel("Height")
    plt.ylabel("Speed")
    plt.title("Scaterplot of Roller Coasters: Height vs. Speed")
    plt.show()

# Create a scatter plot of roller coaster height by speed
print(height_scatter(coasters))