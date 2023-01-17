import streamlit as st
from pymongo import MongoClient
import os


headers = {
  "authorization" : st.secrets["db_uri"]
}

client = MongoClient(headers)


db = client["kindergarden"]

# Create a collection to store the submissions
submissions = db["applications"]


#SEO configuration
st.set_page_config (page_title = 'Lukhanyo Day Care Application Form',
                    page_icon ='📝', 
                    layout ='centered'
)

st.markdown("""
<style>
.stTextInput > label {
font-size:100%;
font-weight:bold;
color: #001833;
}
.stSelectbox > label {
font-size:100%;
font-weight:bold;
color: #001833;
}
.stDateInput > label {
font-size:100%;
font-weight:bold;
color: #001833;
}
div.stButton > button:first-child {
    background-color: #001833;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #FF4B4B;
    color:#000000;
    }
#MainMenu {
    visibility: hidden;
    }
footer {
    visibility: visible;
}
footer:before{
    content:'Copyright (c) 2023: Immensity Holdings';
    display:block;
    position:relative;
    color:#D33639;
}
</style>
""", unsafe_allow_html=True)


#using strimlit form to collect data from user
with st.form('data_form', clear_on_submit=True):
    st.image("logo.png", width=680)

    # Child's information
    child_name = st.text_input("Child's Full Name and Surname:", placeholder='Full Name and Surname')
    child_dob = st.date_input("Child's Date of Birth:")
    dob_object = str(child_dob)

    child_id = st.text_input("Child's ID Number:", placeholder='13 Digit SA ID Number',max_chars= 13)
    child_language = st.selectbox("Home Language:",['siSwati','isiZulu','Sotho','Tsonga','Xhosa','Ndebele','English','siTwana'])
    child_gender = st.selectbox("Child's Gender:", ["Male", "Female"])

    # Parent's information
    parent1_name = st.text_input("Parent, Guardian or Caregiver Name:", placeholder="Mother's Full Name")
    parent1_id = st.text_input("Parent /guardian /caregiver ID:", placeholder='13 Digit SA ID Number',max_chars= 13)
    parent1_email = st.text_input("Parent's Email", placeholder='example@lukhanyo.com')
    parent1_phone = st.text_input("Parent's Phone Number ",placeholder='0720810480',max_chars= 10)
    parent1_work = st.text_input("Place of work:", placeholder='Work Address')
    parent1_home = st.text_input("Home Address", placeholder='Home Address')
    parent1_income = st.text_input("Income per month:", placeholder='Optional')

    # Parent's information
    parent2_name = st.text_input("Parent, Guardian or Caregiver Name:", placeholder="Father's Full Name", key = 'name' )
    parent2_id = st.text_input("Parent /guardian /caregiver ID:", placeholder='13 Digit SA ID Number',max_chars= 13, key = 'id')
    parent2_email = st.text_input("Parent's Email", placeholder='example@lukhanyo.com',key='email')
    parent2_phone = st.text_input("Parent's Phone Number ",placeholder='0720810480',max_chars= 10, key = 'phone')
    parent2_work = st.text_input("Place of work:", placeholder='Work Address', key = 'work_address')
    parent2_home = st.text_input("Home Address", placeholder='Home Address', key='home_address')
    parent2_income = st.text_input("Income per month:", placeholder='Optional', key='income')

    # Medical information
    doctor_name = st.text_input("Doctor Name", placeholder="Doctor's Name")
    doctor_number = st.text_input("Doctor Number", placeholder= '0720810480',max_chars= 10)
    emergency_number = st.text_input("Emergency Number", placeholder = '0132570015',max_chars= 10)
    allergies = st.text_input("Allergies")
    medications = st.text_input("Medications")
    vaccinations = st.radio("Up to date on vaccinations",['Yes', 'No'], key = 'vaccination')
    school_fees = st.radio('I agree to pay the school fees of R400 per month and to follow the rules and regulations of the Lukhanyo Day Care center.',['Yes', 'No'], key = 'aggreement')





    #with open('Lukhanyo Inc (Final).pdf', "rb") as file:
    #    button = st.download_button('Download Contract',data = file, file_name='Lukhanyo Inc (Final).pdf', on_click=None)
if st.form_submit_button("Submit"):
        if not child_name:
            st.error("Child Name is a required field")
        elif not child_dob:
            st.error("Child Date of Birth is a required field")
        elif not child_gender:
            st.error("Child Gender is a required field")
        elif not parent1_name:
            st.error("Parent Name is a required field")
        elif not parent1_email:
            st.error("Parent Email is a required field")
        elif not parent1_phone:
            st.error("Parent Phone is a required field")
        else:
            # Store the submission in MongoDB
            
            submission = {
                "child_name": child_name,
                "child_dob": dob_object,
                "child_id": child_id,
                "child_language": child_language,
                "child_gender": child_gender,
                "mother_name": parent1_name,
                "mother_id": parent1_id,
                "mother_email": parent1_email,
                "mother_phone": parent1_phone,
                "mother_work": parent1_work,
                "mother_home": parent1_home,
                "mother_income": parent1_income,
                "father_name": parent2_name,
                "father_id": parent2_id,
                "father_email": parent2_email,
                "father_phone": parent2_phone,
                "father_work": parent2_work,
                "father_home": parent2_home,
                "father_income": parent2_income,
                "doctor_name": doctor_name,
                "doctor_number": doctor_number,
                "emergency_number": emergency_number,
                "allergies": allergies,
                "medications": medications,
                "vaccinations": vaccinations,
                "school_fees_aggreement": school_fees
            }
            submissions.insert_one(submission)
            st.success("Thank you! The application form submission received!!!")


