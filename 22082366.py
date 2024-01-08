#DataSourceLink : https://www.kaggle.com/datasets/rafsunahmad/terrorist-attacks-data-since-1970-2023
#GithubLink : https://github.com/stanleygundapu/DataHandlingandvisualization.git

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming your data is in a CSV file, load it into a DataFrame
df = pd.read_csv('terrorist-attacks.csv')

# Filter the DataFrame for the last 10 years
df_last_10_years = df[df["Year"] >= df["Year"].max() - 9]

# Set a custom color palette
custom_palette = ['#FF5733' , '#FFD700' , '#FF6347' , '#FF4500' ,
                  '#8A2BE2' , '#800000' , '#FF1493' , '#DC143C']

# Set the custom color palette
sns.set_palette(custom_palette)

# Create a figure with subplots and set background color
fig , axes = plt.subplots(nrows=3 , ncols=2 , figsize=(15 , 15) ,
                         facecolor='#f3f3f3')  # Set background color here

# Plot 1: Terrorist attacks over the last 10 years
sns.lineplot(x="Year" , y="Terrorist attacks" , data=df , ax=axes[0 , 0])
axes[0 , 0].set_title("Terrorist Attacks Over Years" , weight='bold')

# Plot 2: Terrorism deaths over the last 10 years
sns.lineplot(x="Year" , y="Terrorism deaths" , data=df , ax=axes[0 , 1])
axes[0 , 1].set_title("Terrorism Deaths Over Years" , weight='bold')

# Plot 3: Bar chart of attack methods over the last 10 years
attack_methods = df_last_10_years.iloc[: , 6:14].sum()
sns.barplot(x=attack_methods.index , y=attack_methods.values , ax=axes[1 , 0])
axes[1 , 0].set_title("Distribution of Attack Methods Over the Last 10 Years" ,
                     weight='bold')
axes[1 , 0].set_xticklabels(axes[1 , 0].get_xticklabels(),
                           rotation=30 , ha='right' , fontsize=10)

# Plot 4: Stacked bar chart of death ages over the last 10 years
death_ages = df_last_10_years.iloc[: , 14:21]
selected_columns = ['Terrorist Death Type : Suicide' , 'Terrorist Death Type : Killed']
death_ages_by_year = death_ages[selected_columns]
death_ages_by_year = death_ages_by_year.groupby(df_last_10_years["Year"]).sum()
death_ages_by_year.plot(kind="bar" , stacked=True , ax=axes[1 , 1])
axes[1 , 1].set_xticklabels(axes[1 , 1].get_xticklabels() , rotation=0 ,
                           ha='right' , fontsize=10)
axes[1 , 1].set_title("Distribution of Death Ages Over the Last 10 Years" ,
                     weight='bold')

# Add a dashboard title
fig.suptitle("Terrorist Attacks Dashboard - Last 10 Years",
             fontsize=16 , weight='bold' , backgroundcolor='#333333' , color='white')

# Add a text grid as a separate subplot with a background color
text_grid = axes[2 , 1]
text_grid.axis('off')  # Turn off axis for text grid
text = "1. There is a rise and fall in terrorist acts from 1970 and 2010, \n" \
       "however following that year, there is an abrupt increase in \n" \
       "incidents. 2020 saw a decrease in attacks. \n" \
       "2. The number of terrorist deaths increased and decreased between \n" \
       "1970 and 2010, although there was a sharp increase in deaths following \n" \
       "that year. 2020 will see a decline in deaths.\n" \
       "3. The majority of ways that terrorists attack are with bombs and explosions.\n" \
       "4. The cause of death of terrorist due to suicide is low than killing."
text_grid.text(0 , 0.5 , text , fontsize=12 , multialignment='left' ,
               backgroundcolor='#f3f3f3')  # Set text grid background color

text_grid = axes[2 , 0]
text_grid.axis('off')  # Turn off axis for text grid
text = "Student Name: Stanley Moses Gundapu\n" \
       "Student Id: 22082366"
text_grid.text(0 , 0.5 , text , fontsize=12 , multialignment='left' ,
               weight='bold' , backgroundcolor='#f3f3f3')  # Set text grid background color

plt.savefig('22082366.png' , bbox_inches='tight' , pad_inches=0.5)
# Adjust layout
fig.tight_layout(rect=[0 , 0.03 , 1 , 0.95])
plt.subplots_adjust(hspace=0.5 , wspace=0.3)
# plt.show()
