import sys 
sys.path.append("/...")
from main import df, country_list, bar_plot, scatter_plot, df_masked 
# NOTE Must import the file name by itself. This allows you to be able to use the dot notation to modify variables within the main file.
import main as main 
import streamlit as st 
import requests
from streamlit_lottie import st_lottie


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