import streamlit as st
import joblib

#1 Guarantor or Debtor
veri_status_mapping1={"none":0,"co-applicant":1,"gaurantor":2}

#2 Type of Housing
veri_status_mapping2={"for free":0,"rent":1,"own":2}

#3 Working abroad or not
veri_status_mapping3={"No":0,"Yes":1}

#4 Owned property
veri_status_mapping4={"No property":0,"car or other property":1,"building society savings agreement/life insurance":2,"Real Estate":3}

#5 Type of job performed
veri_status_mapping5={"unskilled - resident":0,"unemployed/ unskilled - non-resident":1,"skilled employee / official":2,"management/ self-employed/highly qualified employee/ officer":3}

#6 Number of years of employment
veri_status_mapping6={"unemployed":0,"less than a year":1,"between 1 and 4 years":2,"greater than 4 years":3}

#7 amount in current account
veri_status_mapping7={"less than 0":0,"no current account":1,"between 0 and 200":2,"greater than 200":3}

#8 amount in savings account
veri_status_mapping8={"No savings account":0,"less than 100":1,"between 100 and 500":2,"between 500 and 1000":3,"greater than 1000":4}

#9 Loan History
veri_status_mapping9={'existing loans paid back duly till now':4,'critical account/other loans existing (not at this bank)':0,'delay in paying off loans in the past':1,
       'all loans at this bank paid back duly':3,
       'no loans taken/all loans paid back duly':2}

#10 Other loans plans taken
veri_status_mapping10={"none":2, "bank":1, "stores":0}

# -------------------------------------------------------------------------------

st.title('Welcome to Runaha 🏦')
# orange text

st.subheader('We are here to help you get the best loan counseling')
# -------------------------------------------------------------------------------

col1, col2 = st.columns(2)
with col1:
    # 1 loan amount taken
    loan_amount_taken = st.number_input(
        'Please enter the Loan amount you want',
        0
    )


with col2:
    # 2 age of the applicant in years
    age = st.number_input(
        'Please enter your age',
        0
    )

# percent income paid as installment
percent_income_paid_as_installment = st.slider(
    'Please enter the percentage income to debt ratio',
    0,
    100,
    10,
    help='Please enter the percentage of your income that is already being deducted from your salary'
) 

# owned property
map4_Owned_property = st.selectbox(
    'Please select the type of property you own',
    options=('No property', 'car or other property', 'building society savings agreement/life insurance', 'Real Estate'),
    help='Please select the type of property you own'
)


col1a, col2a = st.columns(2)
with col1a:
    map8_amount_in_savings_account = st.selectbox(
        'Please select the amount range in your savings account',
        options=('No savings account', 'less than 100', 'between 100 and 500', 'between 500 and 1000', 'greater than 1000'),
        help='Please select the amount range in your savings account'
    )

with col2a:
    map7_amount_in_current_account = st.selectbox(
        'Please select the amount range in your current account',
        options=('less than 0', 'no current account', 'between 0 and 200', 'greater than 200'),
        help='Please select the amount range in your savings account'
    )

# ------------------------------
st.subheader('Now let us look at your past performance to give you :orange[more personalised results]')
# ------------------------------

col1b, col2b = st.columns(2)
with col1b:
    # Number of loans taken from current bank
    number_of_loans_taken_from_current_bank = st.slider(
        'Number of loans taken from current bank',
        0,
        20,
        1,
        help='Please enter the number of loans taken from current bank'
    )

with col2b:
    # number of people who will provide maintainance
    number_of_people_who_will_provide_maintainance = st.slider(
        'Number of people who will provide maintainance',
        0,
        20,
        1,
        help='Please enter the number of people who will provide maintainance'
    )

# loan history
map9_loan_history = st.selectbox(
    'Please select your loan history',
    options=('existing loans paid back duly till now', 'critical account/other loans existing (not at this bank)', 'delay in paying off loans in the past', 'all loans at this bank paid back duly', 'no loans taken/all loans paid back duly'),
    help='Please select your loan history'
)

col1c, col2c = st.columns(2)
with col1c:
    # guarantor or debtor
    map1_guarantor_or_debtor = st.selectbox(
        'Please select the type of guarantor or debtor',
        options=('none', 'co-applicant', 'gaurantor'),
        help='Please select the type of guarantor or debtor'
    )   

with col2c:
    # other loans plans taken
    map10_other_loans_plans_taken = st.selectbox(
        'Please select the type of other loans plans taken',
        options=('none', 'bank', 'stores'),
        help='Please select the type of other loans plans taken'
    )

# ------------------------------
st.subheader('We :orange[totally believe you]! We just need a few more things to give you the most accurate results.')
# ------------------------------

col1d , col2d = st.columns(2)
with col1d:
    # time duration of loan
    time_duration_of_loan = st.slider(
        'Time duration of loan',
        0,
        20,
        1,
        help='Please enter the time duration of loan'
    )

with col2d:
    # years of employment
    map2_years_of_employment = st.selectbox(
        'Please select the number of years of employment',
        options=('unemployed', 'less than a year', 'between 1 and 4 years', 'greater than 4 years'),
        help='Please select the number of years of employment'
    )

col1e, col2e = st.columns(2)
with col1e:
    # type of housing
    map2_type_of_housing = st.selectbox(
        'Please select the type of housing',
        options=('rent', 'own', 'for free'),
        help='Please select the type of housing'
    )

with col2e:
    # type of job
    map6_type_of_job = st.selectbox(
        'Please select the type of job',
        options=('unskilled - resident', 'unemployed/ unskilled - non-resident', 'skilled employee / official', 'management/ self-employed/highly qualified employee/ officer'),
        help='Please select the type of job'
    )

# years of staying in current residence


map11_years_of_staying_in_current_residence  = st.number_input(
        'Please select the number of years of staying in current residence',
        0
    )
    
# working abroad or not
map3_working_abroad = st.checkbox(
    'I am working abroad',
    help='Please select if you are working abroad'
)
if map3_working_abroad:
    map3_working_abroad = 1
else:
    map3_working_abroad = 0

map1_guarantor_or_debtor = veri_status_mapping1[map1_guarantor_or_debtor]

map2_type_of_housing = veri_status_mapping2[map2_type_of_housing]

map4_Owned_property = veri_status_mapping4[map4_Owned_property]

map6_type_of_job = veri_status_mapping5[map6_type_of_job]

map7_amount_in_current_account = veri_status_mapping7[map7_amount_in_current_account]

map8_amount_in_savings_account = veri_status_mapping8[map8_amount_in_savings_account]

map9_loan_history = veri_status_mapping9[map9_loan_history]

map10_other_loans_plans_taken = veri_status_mapping10[map10_other_loans_plans_taken]

years_of_employment = veri_status_mapping6[map2_years_of_employment]



# Now add a submit button to the form:
if st.button('Check my chances'):
    st.write('Thank you')
    print(number_of_people_who_will_provide_maintainance)
    print(map9_loan_history)
    print(loan_amount_taken)
    print(map1_guarantor_or_debtor)
    print(years_of_employment)
    print(number_of_loans_taken_from_current_bank)
    print(age)
    print(map7_amount_in_current_account)
    print(map8_amount_in_savings_account)
    print(percent_income_paid_as_installment)
    print(map10_other_loans_plans_taken)
    print(map3_working_abroad)
    print(time_duration_of_loan)
    print(map4_Owned_property)
    print(map6_type_of_job)
    print(map2_type_of_housing)
    print(map11_years_of_staying_in_current_residence)
    scaler = joblib.load('minmaxscaler.joblib')
    model = joblib.load('rforrest.pkl')
    x = scaler.transform([[number_of_people_who_will_provide_maintainance,map9_loan_history,loan_amount_taken,map1_guarantor_or_debtor,years_of_employment,number_of_loans_taken_from_current_bank,age,
    map7_amount_in_current_account,map8_amount_in_savings_account,percent_income_paid_as_installment,veri_status_mapping10,map3_working_abroad,time_duration_of_loan,
    veri_status_mapping4,map6_type_of_job,map2_type_of_housing,map11_years_of_staying_in_current_residence]])

    """x=scaler.transform([[1.0000e+00, 0.0000e+00, 1.0477e+04, 0.0000e+00, 3.0000e+00,
       2.0000e+00, 4.2000e+01, 1.0000e+00, 2.0000e+00, 2.0000e+00,
       2.0000e+00, 1.0000e+00, 3.6000e+01, 0.0000e+00, 2.0000e+00,
       0.0000e+00, 4.0000e+00]])"""
    print(x)
    #print(veri_status_mapping10['bank'])
    """result = model.predict(x)
    print(model.predict(x))
    st.success('U {}'.format(result))"""