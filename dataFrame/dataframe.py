#import pandas as pd
import pandas as pd

#list of strings 
lst = ["Geeks", "for", "Geeks", "is", "portal", "for", "Geeks"]

#Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)
print()
#Python Code Demonstrate Creating
#DataFrame from dict narray / lists
#By default addresses

#Initialize data of lists
datum = {
    'Name': ['Tom', 'Nick', 'Krish', "Jace"],
    'Age' : [20, 21, 19, 18]
}

#Create DataFrame
dp = pd.DataFrame(datum)

#Print the output
print(dp)
print()
#Define a dictionary containing employee data
data = {
    'Name' : ['Jai', 'Princi', 'Gaurav', 'Anuj'],
    'Age' : [27, 24, 22, 32],
    'Address' : ['Dehli', 'Kanpur', 'Allahabad', 'Kannauj'],
    'Qualification' : ['Msc', 'Ma', 'Mca', 'Phd']
}

#Convert the dictionary into DataFrame
dq = pd.DataFrame(data)

#select two columns
print(dq)
print()

#making data frame from csv file
data = pd.read_csv("nba.csv", index_col = "Team")

#Retrieving row by loc method
first = data.loc["Boston Celtics"]
second = data.loc["Toronto Raptors"]

print(first, "\n\n\n", second)