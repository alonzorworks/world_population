import streamlit as st 
import requests
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(
    page_title = "Code Cleaning in Jupyter Labs 🧪",
    page_icon = "💧"
)

def load_lottieurl(url):
    """If the lottie file does not display the image return nothing. This will prevent errors when trying to display the Lottie Files.
    Requires importing packages streamlit_lottie and requests"""
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()

def lottie_credit(credit):
    return st.markdown(f"<p style='text-align: center; color: gray;'>{credit}</p>", unsafe_allow_html=True)




# Cleaning the Data Demonstration 
st.title("The Data Cleansing Process :pencil: :shower:")
st.subheader("Jupyter Labs Was Used to Clean The Data :microscope:")

col1, col2 = st.columns(2)

cleaner = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_n1qlsec7.json")
sprayer = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_6k0vh2px.json")




with col1:
        st.write("All of the cleaning was done in Python. Of course the data could have been cleansed in the same file, but it is more convenient to do it in a Jupyter Labs/Notebooks and simply export the data out. Cleaning was needed to make the null values compatible with Pandas. Also the percent signs and the commas in the dataset had to be removed. I also renamed some columns. The code is provided below. Enjoy.")
        st.write("Keep in mind some additional cleaning was done in the main Python file in Streamlit. This code is also provided in a seperate section. The code is broken up into different sections that represents different cells in Jupyter Labs (JL). JL is very similar to Jupyter Notebooks. The link to the dataset is provided and the code should work out of the box if the file is downloaded and named correctly. There will also be a GitHub repository available of the project.")

with col2:
    st_lottie(cleaner, height = 400, key = "coding")
    lottie_credit("Credit: Design Convete LottieFiles")


# st_lottie(sprayer, height = 400, key = "coding2")
# lottie_credit("Credit: Jeffrey Christropher Lottie Files")




# st.write("All of the cleaning was done in Python. Of course the data could have been cleansed in the same file, but it is more convenient to do it in a Jupyter Lab Notebook and simply export the data out. Cleaning was needed to make the null values compatible with Pandas. Also the percent signs and the commas in the dataset had to be removed. I also renamed some columns. The code is provided below. Enjoy.")
# st.write("Keep in mind some additional cleaning was done in the main Python file in Streamlit. This code is also provided in a seperate section. The code is broken up into different sections that represents different cells in Jupyter Labs (JL). JL is very similar to Jupyter Notebooks. The link to the dataset is provided and the code should work out of the box if the file is downloaded and named correctly. There will also be a GitHub repository available of the project.")



cleaner = """
# Original Dataset Credit
#https://www.kaggle.com/datasets/muhammedtausif/world-population-by-countries

import pandas as pd 
import plotly.express as px 
import streamlit as st
import numpy as np 
import math

# View of the original dataset/dataframe 
# Will be reimported later to include all of the cleaning in one step.
#Viewing the df reminds us whether or not there were percentages in a particular column.
df = pd.read_csv("world-pop-2020.csv")
df.head()



"""

cleaner2 = """
# Original Dataset Credit
#https://www.kaggle.com/datasets/muhammedtausif/world-population-by-countries

df = pd.read_csv("world-pop-2020.csv")

df.rename(columns = {"Country (or dependency)": "Country", "Population 2020": "Population", "Migrants (net)": "Net Migration"}, inplace = True)

# Two Lines of code attempt clean up 
df.replace("N.A", np.nan, inplace = True)
df.replace("N.A.", np.nan, inplace = True)
#Test replacing blanks with nulls
df.replace("", np.nan, inplace = True)



pct_remove = ["World Share", "Yearly Change", "Urban Pop %"]
comma_fix =  ["Population", "Net Change", "Land Area (Km²)", "Net Migration", "Density  (P/Km²)"]

df.rename(columns = {"Yearly Change" : "Yearly Change %", "World Share" : "World Share %", "Land Area (Km²)" : "Land Area (Km^2)", "Density  (P/Km²)": "Density  (P/Km²)"})

# Gets rid of the percentage signs which helps the code function
for i in pct_remove:
    df[i] = df[i].str.rstrip("%").astype("float")

# Clean up the columns with commas in them. They should all be integers. 
# Successful Archetypal Code In the lower comment is made into a for loop. 
#df["Population"] = df["Population"].str.replace(",", "").astype("int")

for i in comma_fix:
    df[i] = df[i].str.replace("," , "").astype("float").round()
    # Floats are used to keep compatibility with the numpy nulls, without further conversion.




"""

cleaner3 = """
# Checks to see how the data was transformed.
df.head()
"""

cleaner4 = """
# Index is used to take away the arbitrary index column.
df.to_csv("world_population_2020_cleaned.csv", index = False)
"""

col3, col4 = st.columns(2)

with col3:
    st_lottie(sprayer, height = 400, key = "coding2")
    lottie_credit("Credit: Jeffrey Christropher Lottie Files")

with col4:
    st.subheader("Importing The Dataset")
    st.write("With some notes included. (Nothing major).")
    st.code(cleaner)


st.subheader("Cell That Cleans The Data")
st.write("This code turns the nulls into numpy null that can be recognized in Python. It also gets rid of the commas and the percent symbols that causes issues within the dataset.")
st.code(cleaner2)
st.code(cleaner3)

cleaners = Image.open("cleaner_set.jpg")

# Note the image had to be imported to the main directory of this project. 
# Not the main folder.
st.image(cleaners , caption = "Credit: macrovector on freepik")