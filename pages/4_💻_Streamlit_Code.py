import streamlit as st 

st.set_page_config(
    page_title = "Streamlit Code",
    page_icon = "💿"
)

# Cleaning the Data Demonstration 
st.title("Streamlit Python Code :page_facing_up: :snake: :shower:")
st.subheader("The Code Was Created in Visual Code")
st.write("Here is the code that was used to make the Streamlit  project. Note the code here is simply for reference. There may be very subtle omissions from the code. See the Github page for the most complete, and accessible version of the project.")


cleaner = '''
import pandas as pd 
import plotly.express as px 
import streamlit as st
import numpy as np 
import math
import streamlit.components.v1 as components
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# Code Created by ALonzo R. SweetDataPie.com
# Main Page Filter By Parameters
# Second Page Filter By Countryy 
# Cleaning The Data Code Process in Jupyter Labs
# Fourth Page All Code Posted For Visual Code/ Streamlit 

def load_lottieurl(url):
    """If the lottie file does not display the image return nothing. This will prevent errors when trying to display the Lottie Files.
    Requires importing packages streamlit_lottie and requests"""
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()

def lottie_credit(credit):
    return st.markdown(f"<p style='text-align: center; color: gray;'>{credit}</p>", unsafe_allow_html=True)




st.header("World Population Data 2020 :earth_africa: :earth_asia: :globe_with_meridians:") 
st.subheader("Information About The Dataset :closed_book:")

col1, col2 = st.columns(2)
#st_lottie(lottie_coding, height = 400, key = "coding")


with col1:
    st.write("The dataset is from the website Kaggle. It uploaded by a user named Muhammed Tausif. He retrieved the data from WorldoMeter. WorldoMeter credits the United Nations Population division for the dataset.")
    st.write("Here is  a breakdown of the dataset taken from Tausif's description in his own words:")
    st.write("*'World Population data with respect to each country/entity in the world. It contains 235 records in total, and 11 columns that contain data about total population till 2020, yearly change, net change, density, land area, migrants, fertility rate, med age, urban population, and world share of the population.'* - **Muhammed Tausif**")

with col2:
    globe = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_b1imuadj.json")
    st_lottie(globe, height = 300, key = "coding")
    # st.markdown("<p style='text-align: center; color: gray;'>Credit: Sebastian Garcia Taborda on LottieFiles</p>", unsafe_allow_html=True)
    lottie_credit("Credit: Sebastian Garcia Taborda on LottieFiles")



# Import The Dataset
df = pd.read_csv("world_population_2020_cleaned.csv")


#
#df = pd.to_numeric(df["Population": "World Share"], downcast =  "float") ##May not be needed
#Key Columns Defined for The Sliders

filter = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_va0hiq2z.json")

col3, col4 = st.columns(2)


with col3:
    st.subheader("Filters")
    st.write("There are different filters that you can use to find different results. Country names can be used as a filter but this will be displayed at the end of the document due to how demanding it is.")

with col4:
    st_lottie(filter, height = 100, key = "coding2")
    lottie_credit("Credit: API Test on LottieFiles.")
    
    



#Population Selection Function
def slide_prep(column_name, integer =  False):
    """ Puts the chosen data column and turns it into a list. Can return a float or an integer. Only integers when set to true."""
    i = column_name
    j = df[i].dropna().unique().tolist()
    k = [float(item) for item in j]

    if integer == True:
        return [math.floor(item) for item in j]
    else:
        return k
    
    

# Prepped Data Will Have a "p" showing that it has been prepped.
population_p = slide_prep("Population", True)
fert_p = slide_prep("Fert. Rate")
med_age_p = slide_prep("Med. Age", True)
rank_pop =  slide_prep("no", True)
urban_p = slide_prep("Urban Pop %")
net_mi_p = slide_prep("Net Migration", True)
net_c_p = slide_prep("Net Change", True)
yearly_change_p = slide_prep("Yearly Change")
#density_p = slide_prep(df.columns[5], True)

# Get List of Every Country 
country_list = df["Country"].unique().tolist()



def slider_func(prep_data, name = " " ,steps = 1):
    """ This function allows a range slider to be created given that a df column is given as integers or floats.
        The code gives the user the ability to name the slider and defines the steps.
    """
    #Markdown is used to make the title of the slider to be bold. That is not available in st. slider.
    st.markdown(f"***Choose {name} Range:***")
    selection = st.slider(f"{name}",
    min_value = min(prep_data),
    max_value = max(prep_data), 
    value = (min(prep_data), 
    max(prep_data)),
    step = steps
    

    )
    # The range must be displayed at the bottom. This is because the markdown range can overlap and become illegible.
    #  Numbers starting at a thousand also have comma seperators. 
    # These features are not  built into streamlit yet as far as I know. 
    # From and to are used to avoid confusion between negative values and the dash of the range.

    selection_formatted = [format(selection[0], ","), format(selection[1], ",")]
    steps_formatted =  format(steps, ",")
    #st.write(f"""*{name} Range: From: {selection_formatted[0]} To: {selection_formatted[1]}""")
    new_line = "\n"
    st.write(f"""**From:** {selection_formatted[0]}""")
    st.write(f"""**To:** {selection_formatted[1]}""")
    st.write(f"**Slider Step Interval:**  {steps_formatted}")
    
    #Horizontal Rule or line break
    # Would Use The HTML/CSS Way but it takes up too much space: see the commented out line below for the code. Need to import streamlit components. Code is below
    #components.html("""<hr style="height:05px;border:none;color:#333;background-color:#333; padding-bottom: 3px" /> """)
    st.markdown("""---""")
    #Provides soace between the different selectors
    st.write(""" 



    """)
    # Return selection allows the mask to be assigned to the variable. 
    return selection

# Problem with this Section and mismmatching data types 
# Creation of The Sliders

st.subheader(":star: Open This Tab to Filter The Data :open_file_folder: :eyes: :star:")
#st.info("Note that all of the ranges are applied simultaneously.")
with st.container():
    with st.expander("Filter the fields to find countries that falls within these ranges."):
        pop_sli = slider_func(population_p, "Population", 1000000)
        fer_sli = slider_func(fert_p, "Fertility", 0.1)
        med_sli = slider_func(med_age_p, "Median Age", 1)
        rank_sli = slider_func(rank_pop, "Rank of Population")
        urban_sli = slider_func(urban_p, "Urban Population Percentage", 0.1)
        mig_sli = slider_func(net_mi_p, "Net Migration", 1000)
        net_sli = slider_func(net_c_p, "Net Change in Population", 10000)
        year_sli = slider_func(yearly_change_p, "Yearly Percent Change in Population", 0.05)

# Country Select CONVENTIONAL Select Basic Code Improved With Container Next line has no select all feature
#country_select = st.multiselect("Select which countries you want to view.", country_list, default  = country_list)






# Creation of The Masks
# There may be a way to do this pythonically.
mask = df["Population"].between(*pop_sli) & df["Fert. Rate"].between(*fer_sli) & df["Med. Age"].between(*med_sli) & df["no"].between(*rank_sli) & df["Urban Pop %"].between(*urban_sli) & df["Net Migration"].between(*mig_sli) & df["Net Change"].between(*net_sli) & df["Yearly Change"].between(*year_sli)
#& (df["Fert. Rate"].between(*fer_sli))

df[mask]

# Data with the filters added 
df_masked = df[mask]
#df_masked.rename(columns = {df_masked.columns[] : "Density People Per Sq KM"}, inplace = True)


# Create The Visualizations 

#Bar Chart Function
def bar_plot(y, emoji =  ""):
    st.subheader(f"{y} 2020 Bar Chart {emoji}")
    bar = px.bar(df_masked, x = "Country", y =  y, color = "Country")
    st.plotly_chart(bar)


# Scatter Plot Function 
def scatter_plot(x, y, emoji_code = ""):
    "Gets the X and Y axis both by their respective column names. Creates a subheader of a title, where an emoji may be passed in if specified."
    st.subheader(f"{y} vs. {x} Scattegraph {emoji_code}")
    chart =  px.scatter(df_masked, x = x , y = y, color = "Country")
    st.plotly_chart(chart)


# NOTE Start of the visualization section. 
st.header("Visualization Section :bar_chart:")
st.write("Here you can visualize the data of the countries that meet the criteria, that can be modified above.")

analysis =  load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_VeqtOe.json")

st_lottie(analysis, height = 400 , key = "coding3")


def chart_explanation(subheader, analysis, video = None, picture = None, picture_caption = None):
    """Create a collaspeable header of analysis using two  strings. 
    The first string is the title of the caption that functions as a title. 
    The second string is the explanation that is passed within st.write() within the tab.
    The video optionally enables you to embed a video. The last two optional variables allows you to embed a picture and a caption. A caption is  require to make a picture to explain/give credit."""
    st.caption(subheader)
    with st.container():
        with st.expander("Click for Analysis/Hints"):
            st.write(analysis)

            if video != None:
                try:
                    st.video(video)
                finally:
                    print(f"The video {video} is not available.")

            if picture != None and picture_caption != None:
                try:
                    image = Image.open(picture)

                    st.image(image, caption = picture_caption)
                finally:
                    print(f"The image: '{picture}' is not available.")

                


# Population Bar Chart
bar_plot("Population", ":earth_americas: :busts_in_silhouette:")
chart_explanation("Population Bar Chart Analysis", "The dataframe listed shows the observations (or rows of countries) in descending order based on population. Use the rank slider to determine what range of ranks you will like to see.")

# Fertility Rate 
bar_plot("Fert. Rate", ":womens: :baby: :baby_bottle:")
chart_explanation("Fertility Rate Bar Chart Analysis",
"""Countries with high populations do not tend to have high fertility rates. Population growth is a temporary according to the demographic transition model. 
Succintly the demographic transition model asserts that as countries become more advanced their population's growth rate decreases. \n \n \n 
For example as societies advance infant mortality goes down. This causes parents to have less children because a greater percentage of them will reach adulthood, instead of dying before reaching one year old.
Also as societies industrialize, and advance children become more of a liability than an asset. In a rural country children can be a source of almost free labor. However children who are reared in urbanized countries are more expensive to raise. These children also typically do not bring in income nor food to their parents.
In advanced societies women also have greater access to education and family planning devices. This allows them to be able to postpone starting a family (assuming they choose to have one) and they typically have less children.
\n \n However this does not always describe every country's situation perfectly. For example China's fertility rate is low partially due to  the one child policy that lasted from 1980-2016 according to Britannica. There are tens of millions of more males than females in China, which prompts some parents to endow their sons with expensive living spaces and other trappings in hopes that they can find a wife. Competition is fierce because females there are scarce. Also more Chinese men are opting to find women in other Asian countries due to the aforementioned reasons.
An understanding of supply and demand would make it hard to fault Chinese females and their parents to have high expectations for their suitors. However this does not bode well for China, a country that now offers incentives for married couples to have children.
\n \n This information comes from my repetoire that can be attributted to my coursework in Economics, Human Geography and Economic Demography. Resources explaining phenomena further are included in this drop down section.
""",
"https://www.youtube.com/watch?v=qfPlljpoHgQ",
"demographic_tm.png",
"Graphic of the demographic transition model created by Our World In Data.")

#Net Change
bar_plot("Net Change")
chart_explanation("Net Change Bar Chart Analysis", "The range for the net change is very large for the data set is very large. It ranges from a negative value to over positive 13 million.")

#Net Change Percent 
bar_plot("Yearly Change", "(Population % Change)")
chart_explanation("Yearly Percentage Change Bar Chart" , "The yearly percent change helps equalize the data. China had the biggest net change by millions. Despite this China's percentage change increase is less than half a percent. Niger had the biggest percentage increase in population up at about 3.84% from  2019. Lithuania had the largest decline in population at about -1.35% population loss.")

#  Population Vs. Land Area
# Value error is given for a matching title that was verified using the "find" edge browser feature. 
# Utilize a different way to select a column.

# Fertility Rate vs. Median Age 
scatter_plot("Med. Age", "Fert. Rate", ":womens: :baby: :baby_bottle:")
chart_explanation("Fertilty Rate vs. Median Age Analysis", """Fertility and median age has a negative correlation. This is because as the population ages, it is more difficult to have children. Young people tend to be more fertile than older people. Older women who have undergone menopause would have great difficulty conceiving though it is technically not impossible.
\n \n Replacement level is considered to be 2.1 children per woman. This is considered replacement level. Replacement level means that the women have enough children to replace both the father and mother. Since the children are younger they will presumably carry on the family's legacy barring an untimely death.
Fertility rate is considered to be 2.1 for a similar reason. Statistically infant mortality has to be factored in by researchers. By having the replacement level at 2.1 the population still replaces  itself after factoring in infant mortality. 
\n \n Median age signifies that about half of  the population is above the median age, and 50% is below it. This  gives a lot more information than the mean which can more easily skewed. With this in mind typically the younger the median age is the higher the fertility rate is. 
This is because a large swath of the country was born recently indicating people are having children. It also signifies that a large number of the population has in their prime child bearing years, or have their most fecund years ahead of them. 
When the median is high it signifies that a large part of the population are most likely done having kids.

\n \n Japan is in population crisis. Their fertility rate for the year 2020 was 1.4 which is one of the lowest in the world. Per the dataset used here they have the highest median population age in the world at 48. This means that the youngest half of the population can include people who are past their most fertile years. This will make it hard for Japan to replenish it's dwindling population. 
This is exacerbated by the fact that Japan nationalistic cultural landscape makes immigrating to the country quite difficult. The BBC had a segment of why Japan has a low fertility rate, its current effects, and how it does not bode well for the island.
"""
, video = "https://www.youtube.com/watch?v=yArB4rgA1hM")

# Population Vs Land Area
scatter_plot("Land Area (Km²)", "Population")



# Population vs. Urban Pop %
scatter_plot("Urban Pop %", "Population", ":busts_in_silhouette: :office:")
chart_explanation("Population vs. Urban Population %", "It is tempting to hypothesize that Urban population percentage would increase with population. However this proves to be to be a heuristic at best. This is almost graph is a great example of there being almost no correlation between the y and x.")

# Land Area vs. Density 
scatter_plot("Urban Pop %", df_masked.columns[5] )
chart_explanation("Density vs. Urban Population Scattergraph", "This chart shows that density does not have a discernable correlation between the Density and Urban Population Percentage.")

# Net Change vs Net Migration 
scatter_plot("Net Migration", "Net Change")
chart_explanation("Net Change vs. Net Migration Analysis", """We can make a simple equation concerning the net change of a country: \n \n
*** Net Change = (Births - Deaths) +  Net Migration ***  \n \n
The dataset does not gives us births and deaths. In for this analysis we don't really need those values. \n \n 
Let's take a look at Japan again. The Net Change was -383,000 people, which includes 71,000 immigrants coming into the country. This means that more people are dying than are being born. The immigration metric is not enough to make up for the lack of babies coming from Japanese parents.
""")


# Population vs. Density
scatter_plot("Population", df_masked.columns[5])



# Density Vs Land Area 
scatter_plot( df_masked.columns[6] , df_masked.columns[5])
chart_explanation("Density vs. Land Area Analysis", """The smallest countries have some of the highest densities. This makes a lot of sense. This is because the less space there is the more densely packed the inhabitants will have to be. The relationship between the y and x is inverse, and even apppears to be logarithmic.
\n \n The least dense country is Russia. Russia is the 9th largest country according to this dataset. Russia is also the largest country in terms of square kilometers in the dataset. With all of this excess space available per person it makes sense how Russia is not densely populated.""")


# The Last Image Before the End of the Document 
st.image("world_image.png", caption = "Location 3D Illustration by IconScout Store")





# NOTE Originally the country filter was going to be incorporated into the filter on the main page. 
# To fascilitate adhoc analysis the country filter was placed on a seperate page. 

# # Country Select Container
# st.subheader("Country Selector")
# with st.container():
#     with st.expander("See States"):
#         all = st.checkbox("Select All")


#         if all:
#             selected_options = st.multiselect("Select one or more options:", country_list, country_list)

#         else:
#             selected_options = st.multiselect("Select one or more options:", country_list)
        





'''

cleaner2 = '''
import sys 
sys.path.append("/...")
from main import df, country_list, bar_plot, scatter_plot, df_masked 
# NOTE Must import the file name by itself. This allows you to be able to use the dot notation to modify variables within the main file.
import main as main 
import streamlit as st 
import requests
from streamlit_lottie import st_lottie

# Note similar set_page_configurations was used for the other pages, even though it is not shown. 
st.set_page_config(
    page_title = "Country Filter",
    page_icon = "🌎"
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



# Use this picture for map and phone respectively.
# https://assets4.lottiefiles.com/packages/lf20_bx5reiuc.json
# https://assets5.lottiefiles.com/packages/lf20_vuai8mk4.json

st.title("Choose Countries to Analyze")
st.write("Use this page's dropdown to select which countries you would like to analyze. By default none are selected.")


phone_select = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_vuai8mk4.json")
globe_select = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_mq11wjtp.json")


# col1 = st.column(1)

# with col1:
#     st_lottie(phone_select, height = 400, key = "coding")
#     lottie_credit("Credit: Viraj Nemlekar by Viraj Nemlekar")



st_lottie(globe_select, height = 400, key = "coding2")
lottie_credit("Credit: Earth&Pins Max Shturma LottieFiles")







# NOTE For this page we are going to make the list of countries in alphabetical order. 
# It makes it easier for users to find which countries they need. 
country_list = sorted(country_list)


# Country Select Container
st.subheader("Country Selector")
st.write("To clear all selected countries look for the x symbol in the dropdown menu.")
with st.container():
    with st.expander("See States"):
        all = st.checkbox("Select All")


        if all:
            country_select = selected_options = st.multiselect("Select one or more options:", country_list, country_list)

        else:
            country_select = selected_options = st.multiselect("Select one or more options:", country_list)

# NOTE: This df_masked is not the same as the one that is located in the main file. 
# This is a masking concerning selected countries in the drop down. 
# In order to overwrite the df_masked in the main file we have to import the file by itself. See the note placed while importing.
# Then we must overwrite with the eponymous (or even a different name as long as main.df_masked = df_masked of this file) name df_masked so that the right filters are applied to it.

mask = df["Country"].isin(country_select)
df_masked = df[mask]

df_masked.sort_values(by = ["Country"], ascending = True, inplace = True)

df_masked

main.df_masked = df_masked


# Now the functions can be called in from the main page. 
# The best part about this is that we do not have to write the defining of the functions twice. 
# If we want to change something the change will automatically will be applied to this page's chart also. 
# Now the calling of the functions can be duplicated here. 

# Population Bar Chart
bar_plot("Population", ":earth_americas: :busts_in_silhouette:")


#Net Change
bar_plot("Net Change")

#Net Change Percent 
bar_plot("Yearly Change", "(Population % Change)")

# Fertility Rate vs. Median Age 
scatter_plot("Med. Age", "Fert. Rate", ":womens: :baby: :baby_bottle:")

# Population Vs Land Area
scatter_plot("Land Area (Km²)", "Population")

# Population vs. Urban Pop %
scatter_plot("Urban Pop %", "Population", ":busts_in_silhouette: :office:")

# Land Area vs. Density 
scatter_plot("Urban Pop %", df_masked.columns[5] )

# Net Change vs Net Migration 
scatter_plot("Net Migration", "Net Change")

# Population vs. Density
scatter_plot("Population", df_masked.columns[5])

# Density Vs Land Area 
scatter_plot( df_masked.columns[6] , df_masked.columns[5])



'''









st.subheader("Main Code")
st.code(cleaner)
st.subheader("Country Filtering Code")
st.code(cleaner2)