
import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import plotly.subplots as sp 
import datetime as DT
import io
import numpy as np


st.set_page_config(page_title= 'Customer Analysis', page_icon=':bar_chart: ',
                   layout='wide',
                   initial_sidebar_state='expanded',
                   )


st.markdown(
    """
    <style>
    /* Set the page width */
    .stApp {
        max-width: 2000px;
    }

    /* Set the background color */
    body {
        background-color: #f2f2f2;
    }
     /* Add custom navigation bar */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: right;
        background-color: #f9f9f9;
        padding: 5px;
    }
    .logo {
        height: 40px;
    }

    /* Customize subheader styles */
    .custom-subheader {
        font-size: 30px;
        font-weight: bold;
        color: #ff0000; /* Change the text color to red */

    }
    /* Customize markdown styles */
    .custom-markdown {
        font-size: 16px;
        color: #333333; /* Change the text color to dark gray */
    }
    /* Customize table styles */
    .dataframe {
        font-size: 14px;
        border: 1px solid #ccc;
        border-collapse: collapse;
        margin: 10px;
    }
    .dataframe th, .dataframe td {
        padding: 6px 10px;
        border: 1px solid #ccc;
    }
    .dataframe th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="navbar">
        <img class="logo" src="https://cdn-assets.theforage.com/icons/kpmg_icons/sprocket_central_logo.png">
        
    </div>
    """,
    unsafe_allow_html=True
)


table_style = """
<style>
    .dataframe {
        font-size: 14px;
        border: 1px solid #ccc;
        border-collapse: collapse;
        margin: 10px;
    }
    .dataframe th, .dataframe td {
        padding: 6px 10px;
        border: 1px solid #ccc;
    }
    .dataframe th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
</style>
"""
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """




df = pd.read_excel(io='Kpmgnew.xlsx',
                  engine = 'openpyxl',
                  sheet_name = 'Transactions'
                  )






#find and replace
column_name= 'gender'
find_value= 'F'
replace_value = 'Female'
df[column_name]= df[column_name].replace(find_value, replace_value)

column_name= 'gender'
find_value= 'M'
replace_value = 'Male'
df[column_name]= df[column_name].replace(find_value, replace_value)

#Remove blacks in dataset
#To ask Mwavu why this is not executing what i want



#filters
#st.sidebar.header('Filter here')
#gender= st.sidebar.multiselect(
    #'Select gender:',
   # options=df["gender"].unique(),
    ##default=df["gender"].unique()


##st.sidebar.header('Filter here')
#wealth_segment= st.sidebar.multiselect(
    ##'Select wealth_segment:',
    ###options=df["wealth_segment"].unique(),
    #default=df["wealth_segment"].unique()



#job_industry_category= st.sidebar.multiselect(
    #'Select job_industry_category:'
    #options=df["job_industry_category"].unique(),
    #default=df["job_industry_category"].unique()



#state= st.sidebar.multiselect(
    #'Select state:'
    #options=df["state"].unique(),
    #default=df["state"].unique()


#df.selection = df.query(
    #"gender == @gender & wealth_segment == @wealth_segment & job_industry_category == @job_industry_category & state == @state"



# print(df)


#query method
#gender
df_female= df.query("gender == 'Female'")
df_male= df.query("gender == 'Male'")
#wealthsegment
df_Masscustomer = df.query("wealth_segment == 'Mass Customer'")
df_AffluentCustomer = df.query("wealth_segment == 'Affluent Customer'")
df_HighNetWorth = df.query("wealth_segment == 'High Net Worth'")
#car owners




#st.dataframe(df)




#Mainpage






# Bike Related Purchases Based on Gender

st.markdown("<h1 style='font-size: 30px;'>Sprocket Customer List Analysis</h1>", unsafe_allow_html=True)

Total_Bike_Related_Purchases_made_by_Females = int(df_female["past_3_years_bike_related_purchases"].sum())

Total_Bike_Related_Purchases_made_by_Males = int(df_male["past_3_years_bike_related_purchases"].sum())



left_column, right_column= st.columns(2)
#with left_column:
    #st.subheader('Total Bike Related Purchases Made By Female:')
    #st.subheader(f"US $ {Total_Bike_Related_Purchases_made_by_Females:,}")

#with left_column:
    #st.subheader('Total Bike Related Purchases Made By Males:')
    #st.subheader(f"US $ {Total_Bike_Related_Purchases_made_by_Males:,}")

with left_column:
    gender_data = df.groupby('gender')["past_3_years_bike_related_purchases"].sum().reset_index()
    fig= px.pie(gender_data, names= "gender", values= 'past_3_years_bike_related_purchases') 
    fig.update_layout(title="Bike Related Purchases Based on Gender", height=400, width=400)
    st.plotly_chart(fig)

with left_column:
    jobindustry_data = df.groupby('job_industry_category')["Profit"].sum().reset_index()
    fig= px.bar(jobindustry_data, x= "job_industry_category", y= "Profit", orientation='v',
                color_discrete_sequence=['#ff0000'],
                template='plotly_white')
    fig.update_traces(marker=dict(color='blue'))
    fig.update_layout( plot_bgcolor= 'rgba(0,0,0,0)', title="Profits Based on Customer's Job Industry", height=500, width=400)
    st.plotly_chart(fig)



with right_column:
    bins= [20,35,50,65,80,95]
    df['Age group'] = pd.cut(df['Age'], bins=bins, labels=['20-34','35-49','50-64', '65-79','80-94'])
    pd.to_numeric('Profit', errors='ignore')
    grouped_data = df.groupby(['Age group','wealth_segment'])['Profit'].sum().reset_index()
    fig = px.bar(grouped_data, x='Age group', y='Profit', color='wealth_segment', barmode='group')
    fig.update_layout(title="Profits Based on Wealth Segment grouped by Age Cluster", height=400, width=500)
    st.plotly_chart(fig)

with right_column:
    df_nsw = df.query("state == 'NSW'")
    CustomersinNSW = df_nsw['state'].count()
    df_vic = df.query("state == 'VIC'")
    CustomersinVIC = df_vic['state'].count()
    df_que = df.query("state == 'QLD'")
    CustomersinQUE = df_que['state'].count()
    data = {
    'Customers Based in New South Wales ': [CustomersinNSW],
    'Customers Based in Victoria': [CustomersinVIC],
    'Customers Based in Queensland': [CustomersinQUE]
    }
    statedats = pd.DataFrame(data)
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(statedats)

    


    df_carowners= df.query("owns_car == 'No'")
    #df['car_owners'] = int(df_carowners['owns_car'].count())
    carownersbased_states = df_carowners.groupby('state').size().reset_index(name='counts')
    fig= px.pie(carownersbased_states, names= "state", values = 'counts' ) 
    fig.update_layout(title="Customers With No Cars Based State", height=400, width=400)
    st.plotly_chart(fig)


# New Customers To target in New Custoers List

st.markdown("---")

nsl = pd.read_excel('Kpmgnew.xlsx', 'NewCustomerList',index_col=0)

nsl['DOB'] = pd.to_datetime(nsl['DOB'],format="%Y-%m-%d")
now=pd.Timestamp.now()
st.write("Current date:", now)
nsl['Age'] = (((now - nsl['DOB']).dt.days)/365).round(0)
#nsl['DOB'] = nsl['DOB'].where(nsl['DOB'] < now, nsl['DOB'] -  np.timedelta64(100, 'Y'))
#nsl['Agee'] = ( now- nsl['DOB']).astype('timedelta64[ns]')

#Filter wealth_segment - Mass Customer
options = ['Mass Customer', 'High Net Worth','Affluent Customer']
nsl_df = nsl[nsl['wealth_segment'].isin(options)]

options = ['NSW', 'VIC']
nsl_dff = nsl_df[nsl_df['state'].isin(options)]

options = ['Manufacturing', 'Financial Services', 'Health']
nsl_dfff = nsl_dff[nsl_dff['job_industry_category'].isin(options)]

options = ['No']
nsl_dffff = nsl_dfff[nsl_dfff['owns_car'].isin(options)]

options = ['Female']
nsl_dfffff = nsl_dffff.loc[nsl_dffff['past_3_years_bike_related_purchases'] > 40 & nsl_dffff['gender'] .isin(options)]



nsl_dfffff['Age']= pd.to_numeric(nsl_dfffff['Age'])
age_group = st.slider('Select Age Group', int(nsl_dfffff['Age'].min()), int(nsl_dfffff['Age'].max()), (35, 49))
filtered_data = nsl_dfffff[(nsl_dfffff['Age'] >= age_group[0]) & (nsl_dfffff['Age'] <= age_group[1])]


#st.write(filtered_data)


columns_to_exclude = ['DOB', 'job_title','deceased_indicator', 'owns_car','tenure', 'address',
                      'postcode', 'country','property_valuation','Rank', 'Value']


filtered_data_excluded = filtered_data.drop(columns = columns_to_exclude)
#filtered_data_excluded1 = filtered_data_excluded.drop(columns='Unnamed')

filtered_data_excluded = filtered_data_excluded.loc[:, ~filtered_data_excluded.columns.str.contains('^Unnamed')]

st.markdown('### New Customers To Target')

st.dataframe(filtered_data_excluded)






