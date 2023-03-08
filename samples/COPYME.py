# This script takes some sample data and does a short EDA
# Please create a copy of the file, rename, make changes (optional)
# Create a new branch and push your changes (new file) to the repo
# Then open a PR on GitHub and have it approved

import pandas as pd
import matplotlib as plt
import seaborn as sns

# Read the data
# source: https://www.kaggle.com/tiredgeek/predict-bo-trial

ev = pd.read_csv("https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD")

ev.head()

# Create plot of frequency of each make
g = sns.countplot(x="Model Year", data=ev)
g.set_xticklabels(g.get_xticklabels(), rotation=90, ha="right")





