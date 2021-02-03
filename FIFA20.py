# Core Package
import streamlit as st

# EDA Packages
import pandas as pd
import numpy as np

# Visualization Packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

# Visulaization Packages 2
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as py

# Other Required Packages
import string
import webbrowser

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


url = 'https://raw.githubusercontent.com/305kishan/FIFA20-Analysis/main/players_20.csv'
data = pd.read_csv(url,sep=",")

data.drop(['sofifa_id','player_url','real_face','nation_position','nation_jersey_number','long_name']
          ,axis=1,inplace=True)

club_list = data['club'].to_list()
club_list = np.unique(club_list).tolist()

country_list = data['nationality'].to_list()
country_list = np.unique(country_list).tolist()


# FUNCTION TO FILTER OUT A CLUB WITH SELECTED ATTRIBUTES IN DATAFRAME
def club(x):
    return data[data['club']==x][['short_name', 'team_jersey_number','player_positions','overall','potential',
                              'nationality','age','value_eur','wage_eur','contract_valid_until']]

# FUNCTION TO FILTER OUT A COUNTRY WITH SELECTED ATTRIBUTES IN DATAFRAME
def country(x):
    return data[data['nationality']==x][['short_name','overall','potential','player_positions','age',
                                         'value_eur']]

# SELECTS LENGTH OF DATASET OF THE INPUT CLUB
def club_strength(x):
    r,c = x.shape
    return r

# ADDS THE VALUE OF ENTIRE SQUAD OF A CLUB
def club_value(x):
    squadvalue = 0
    for i in range(0, len(x)):
        squadvalue+=x.iloc[i]['value_eur']
    
    squadvalue = squadvalue/1000000
    return squadvalue

# SUMMATION OF PLAYERS WAGES
def club_wage(x):
    squadwage = 0
    for i in range(0, len(x)):
        squadwage+=x.iloc[i]['wage_eur']
    
    squadwage = squadwage/1000000
    return squadwage

# RETURNS AVG AGE OF PLAYERS OF A CLUB
def average_age(x):
    avg_age = x["age"].mean()
    avg_age = round(avg_age,1)
    return avg_age

# RETURNS AVG OVR OF PLAYERS
def average_ovr(x):
    avg_ovr = x["overall"].mean()
    avg_ovr = int(avg_ovr)
    return avg_ovr


# FUNCTION TO SHOW SQUAD STRENGTH
def country_playerscount(x):
    r,c = x.shape
    return r

# FUNCTION TO PLOT AGE
def plot_age(data1):
    plt.figure(figsize= (15,7))
    ax = sns.countplot(x='age', data=data1, palette='bright')
    ax.set_title(label='Count of Players on Basis of Age', fontsize=18)
    ax.set_xlabel(xlabel='Age', fontsize=16)
    ax.set_ylabel(ylabel='Count', fontsize=16)
    st.pyplot()

# FUNCTION TO PLOT OVR
def plot_ovr(data1):
    plt.figure(figsize= (15,7))
    ax = sns.countplot(x='overall', data=data1, palette='bright')
    ax.set_title(label='Count of Players on Basis of OVR', fontsize=18)
    ax.set_xlabel(xlabel='OVR', fontsize=16)
    ax.set_ylabel(ylabel='Count', fontsize=16)
    st.pyplot()

# FUNCTION TO PLOT NATIONALITY
def plot_nationality(data1):
    plt.figure(figsize= (15,7))
    ax = sns.countplot(x='nationality', data=data1, palette='bright')
    ax.set_title(label='Count of Players on Basis of NATIONALITY', fontsize=18)
    ax.set_xlabel(xlabel='Nationality', fontsize=16)
    ax.set_ylabel(ylabel='Count', fontsize=16)
    plt.xticks(rotation=30, fontsize=12)
    st.pyplot()

# FUNCTION TO PLOT CONTRACT EXPIRY
def plot_contractexp(data1):
    plt.figure(figsize= (15,7))
    ax = sns.countplot(x='contract_valid_until', data=data1, palette='bright')
    ax.set_title(label='Count of Players on Basis of Contract Expiration', fontsize=18)       
    ax.set_xlabel(xlabel='Contract Expiration', fontsize=16)
    ax.set_ylabel(ylabel='Count', fontsize=16)
    plt.xticks(rotation=30, fontsize=12)
    st.pyplot()
 
# FUNCTION TO PLOT POSITIONS
def plot_position(data1):
    plt.figure(figsize= (15,7))
    ax = sns.countplot(x='player_positions', data=data1, palette='bright')
    ax.set_title(label='Count of Players on Basis of Positions', fontsize=18)          
    ax.set_xlabel(xlabel='Positions', fontsize=16)
    ax.set_ylabel(ylabel='Count', fontsize=16)
    plt.xticks(rotation=60, fontsize=12)           
    st.pyplot()
    


def main():
    st.title("FIFA 20 CLUB & COUNTRY ANALYSIS")
    st.markdown("---")
    
    activities = ['CLUB', 'COUNTRY'] # CHOOSE EITHER ONE
    choice = st.sidebar.selectbox("Select", activities) #CREATING A SIDE NAVIGATION FORM
    
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    
    if st.sidebar.button("Show Club Names"):
        st.sidebar.write(club_list)
        
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    
    if st.sidebar.button("Show Country Names"):
        st.sidebar.write(country_list)
    
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    
    st.sidebar.write("Reach Me Here!")

    link = '[GitHub](https://github.com/305kishan)'
    st.sidebar.markdown(link, unsafe_allow_html=True)
    
    link = '[Kaggle](https://www.kaggle.com/kishan305)'
    st.sidebar.markdown(link, unsafe_allow_html=True)
    
    link = '[LinkedIn](https://www.linkedin.com/in/305kishan/)'
    st.sidebar.markdown(link, unsafe_allow_html=True)
    
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)    
    
            
    if choice == 'CLUB':
        st.header('CLUB ANALYSIS')
        st.markdown("<br>", unsafe_allow_html=True)
        
        input_club = st.text_input("Enter A Club Name","Real Madrid")
        input_club = string.capwords(input_club)
        
        if input_club not in club_list: #CHECKING INPUT VALIDITY
            st.text("Club Name Not Found in DataBase")
        elif st.button("SUBMIT"): # IF INPUT IS VALID PROCEEDING TO FURTHER STEPS
            data1 = club(input_club).reset_index(drop=True)
            
            # DISPLAYING DATA HEADER
            st.write(data1.head())
            
            # NUMBER OF PLAYERS IN SQUAD
            input_club_strength = club_strength(data1)
            st.write('Current Squad Strength of ',input_club, 'is', input_club_strength, ' Players')
            
            # SQUAD VALUE IN MILLION EUROS
            input_club_value = club_value(data1)
            st.write('Current Squad Value of', input_club, 'is',input_club_value, ' Millions Euro')
            
            # SQUAD WAGES IN MILLION EUROS
            input_club_wage = club_wage(data1)
            st.write(input_club, 'Spends ',input_club_wage,' Millions Euros Per week as Wages to its Players')
            
            # AVERAGE AGE OF PLAYERS
            input_club_average_age = average_age(data1)
            st.write(input_club,'Squad\'s have an average age of',input_club_average_age,'Years')
            
            # AVERAGE OVR OF PLAYERS
            input_club_average_ovr = average_ovr(data1)
            st.write(input_club, 'Squad\'s have an average OVR of ',input_club_average_ovr)
            
            # PLOTTING OF DATA
            st.subheader('PLOTS')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            
            # AGE WISE PLAYER COUNT
            plot_age(data1)
            
            # OVR WISE PLAYER COUNT
            plot_ovr(data1)
            
            # NATIONALITY WISE PLAYER COUNT
            plot_nationality(data1)
            
            # CONTRACT EXPIRATION WISE PLAYER COUNT
            plot_contractexp(data1)
            
            # POSITION WISE PLAYER COUNT
            plot_position(data1)
            
            # DISPLAYING PLAYERS NAME & OVR
            tempdf = data1.sort_values(by='overall')
            fig = px.bar(tempdf, x='short_name', y='overall', color='overall')
            fig['layout']['yaxis1'].update(title='', range=[60, 100], dtick=5, autorange=False)
            fig.update_layout(title='OVR of Players',
                             xaxis_title="Player's Name",
                             yaxis_title="OVR")
            st.plotly_chart(fig)
            
            # DISPLAYING PLAYERS NAME & POTENTIAL
            tempdf = data1.sort_values(by='potential')
            fig = px.bar(tempdf, x='short_name', y='potential', color='potential')
            fig['layout']['yaxis1'].update(title='', range=[60, 100], dtick=5, autorange=False)
            fig.update_layout(title='Potential of Players',
                             xaxis_title="Player's Name",
                             yaxis_title=" Potential")
            st.plotly_chart(fig)
            
            # DISPLAYING PLAYERS NAME & WAGES
            tempdf = data1.sort_values(by='wage_eur')
            fig = px.bar(tempdf, x='short_name', y='wage_eur', color='wage_eur')
            fig.update_layout(title='Weekly wages of Players',
                             xaxis_title="Player's Name",
                             yaxis_title="Wage in Euro")
            st.plotly_chart(fig)
            
            # DISPLAYING PLAYERS NAME & VALUES
            tempdf = data1.sort_values(by='value_eur')
            fig = px.bar(tempdf, x='short_name', y='value_eur', color='value_eur')
            
            fig.update_layout(title='Values of Players',
                             xaxis_title="Player's Name",
                             yaxis_title="Value in Euro")
            st.plotly_chart(fig)
            
            # DISPLAYING PLAYERS NAME & VALUES
            tempdf = data1.sort_values(by='contract_valid_until')
            fig = px.bar(tempdf, x='short_name', y='contract_valid_until', color='contract_valid_until')
            fig['layout']['yaxis1'].update(title='', range=[2019, 2026], dtick=5, autorange=False)
            fig.update_layout(title='Contract of Players',
                             xaxis_title="Player's Name",
                             yaxis_title="Contract Expiration")
            st.plotly_chart(fig)
    
    
    if choice == 'COUNTRY':
        st.header('COUNTRY ANALYSIS')
        st.markdown("<br>", unsafe_allow_html=True)
        
        input_country = st.text_input("Enter A Country  Name","India")
        input_country = string.capwords(input_country)
        
        if input_country not in country_list: #CHECKING INPUT VALIDITY
            st.text("Country Name Not Found in DataBase")
        elif st.button("SUBMIT"): # IF INPUT IS VALID PROCEEDING TO FURTHER STEPS
            data1 = country(input_country).reset_index(drop=True)
            
            # COUNT OF PLAYERS FROM A COUNTRY
            input_country_playerscount = country_playerscount(data1)
            st.write('Number of Players from ',input_country, 'is', input_country_playerscount, ' Players')
            
            # COMBINED PLAYERS VALUE
            input_country_value = club_value(data1)
            st.write('Current Combined Player\'s Value of', input_country,' is ',input_country_value, ' Millions Euro')
            
            # AVG AGE OF SQUAD
            input_country_avg_age = average_age(data1)
            st.write(input_country, 'Player\'s have an average age of ',input_country_avg_age, ' Years')
            
            # AVG OVR
            input_country_avg_ovr = average_ovr(data1)
            st.write(input_country, 'Player\'s have an average OVR of ',input_country_avg_ovr)
            
            # PLOTTING OF DATA
            
            # COUNT OF PLAYERS WITH DIFF AGES
            plot_age(data1)
            
            # COUNT OF PLAYERS WITH DIFFERENT OVRs
            plot_ovr(data1)
            
            
    
    
if __name__=="__main__":
    main()
