import streamlit as st
import pickle as pkl
import numpy as np
import plotly.express as px
import pandas as pd
import geocoder


def get_device_location():
    # Use the geocoder library to get the device's location based on IP address
    location = geocoder.ip("me")

    if location.latlng:
        return location.latlng
    else:
        st.warning("Unable to determine device location.")
    return None


def main():
    st.title("Multiple diseases prediction for users")
    with open(
        r"C:\Users\Admin\B.E MAJOR PROJECT\Project-Material-BE\pickle files\multiple_disease.sav",
        "rb",
    ) as file:
        loaded_model = pkl.load(file)

    model = loaded_model["model"]
    label_encoder = loaded_model["label_encoder"]

    device_location = get_device_location()

    # Read the CSV data into a Pandas DataFrame
    df = pd.read_csv(r"C:\Users\Admin\B.E MAJOR PROJECT\Project-Material-BE\Data files\hospital_directory.csv")

    # Check if the DataFrame contains a column with comma-separated 'latitude,longitude'
    # Split the 'coordinates' column into separate 'latitude' and 'longitude' columns
    df[["latitude", "longitude"]] = df["Location_Coordinates"].str.split(
        ",", expand=True
    )
    # Convert the 'latitude' and 'longitude' columns to numeric
    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

    # Create a map using Plotly Express
    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        hover_name=df.columns[3],
        hover_data={"Location": True},  # Display the first column as the hover text
        title="Nearby Hospitals, zoom in for more details",
        mapbox_style="open-street-map",
        zoom=15,  # You can adjust the zoom level as needed
        center=dict(lat=device_location[0], lon=device_location[1]),
    )

    # Display the map in Streamlit

    # getting input data from the user
    # Columns for input fields

    col1, col2, col3 = st.columns(3)

    display_yes_no = ("No", "Yes")

    options_yes_no = list(range(len(display_yes_no)))

    print(options_yes_no)

    with col1:
        itching = st.selectbox(
            "Does the user/patient have itching problem ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=1,
        )

    with col2:
        skin_rash = st.selectbox(
            "Does the user/patient have skin rash ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=2,
        )

    with col3:
        continuous_sneezing = st.selectbox(
            "Does the user/patient have continuous sneezing problem ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=3,
        )

    with col1:
        shivering = st.selectbox(
            "Does the user/patient have shivering in body ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=4,
        )

    with col2:
        joint_pain = st.selectbox(
            "Does the user/patient have joint pain ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=5,
        )

    with col3:
        stomach_pain = st.selectbox(
            "Does the user/patient have stomach pain ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=6,
        )

    with col1:
        acidity = st.selectbox(
            "Does the user/patient have acidity ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=7,
        )

    with col2:
        vomiting = st.selectbox(
            "Does the user/patient performed vomiting ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=8,
        )

    with col3:
        fatigue = st.selectbox(
            "Does the user/patient had fatigue ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=9,
        )

    with col1:
        weight_gain = st.selectbox(
            "Does the user/patient have gained weight ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=10,
        )

    with col2:
        anxiety = st.selectbox(
            "Does the user/patient have anxiety problem ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=11,
        )

    with col3:
        mood_swings = st.selectbox(
            "Does the user/patient have mood swings problem ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=12,
        )

    with col1:
        weight_loss = st.selectbox(
            "Does the user/patient have lost weight ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=13,
        )

    with col2:
        restlessness = st.selectbox(
            "Does the user/patient have restlessness ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=14,
        )

    with col3:
        irregular_sugar_level = st.selectbox(
            "Does the user/patient have irregular sugar level problem? ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=15,
        )

    with col1:
        cough = st.selectbox(
            "Does the user/patient have cough ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=16,
        )

    with col2:
        high_fever = st.selectbox(
            "Does the user/patient have high fever ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=17,
        )

    with col3:
        breathlessness = st.selectbox(
            "Does the user/patient have breathlessness ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=18,
        )

    with col1:
        sweating = st.selectbox(
            "Does the user/patient have sweating problem ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=19,
        )

    with col2:
        dehydration = st.selectbox(
            "Does the user/patient have dehydration ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=20,
        )

    with col3:
        indigestion = st.selectbox(
            "Does the user/patient have indigestion problem ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=21,
        )

    with col1:
        headache = st.selectbox(
            "Does the user/patient have headache problem ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=22,
        )

    with col2:
        nausea = st.selectbox(
            "Does the user/patient have suffered from nausea ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=23,
        )

    with col3:
        loss_of_appetite = st.selectbox(
            "Does the user/patient have a loss of appetite ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=24,
        )

    with col1:
        back_pain = st.selectbox(
            "Does the user/patient have back pain ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=25,
        )

    with col2:
        constipation = st.selectbox(
            "Does the user/patient have constipation ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=26,
        )

    with col3:
        abdominal_pain = st.selectbox(
            "Does the user/patient have abdominal pain ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=27,
        )

    with col1:
        diarrhoea = st.selectbox(
            "Does the user/patient have diarrhoea ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=28,
        )

    with col2:
        mild_fever = st.selectbox(
            "Does the user/patient have mild fever ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=29,
        )

    with col3:
        yellow_urine = st.selectbox(
            "Does the user/patient have yellow urine ?",
            options_yes_no,
            format_func=lambda x: display_yes_no[x],
            key=30,
        )

    # # code for prediction
    user_diagnosis = """"""

    # creating a button for prediction

    if st.button("Test Results"):
        inputFeatures = [
            itching,skin_rash,continuous_sneezing,shivering,joint_pain,stomach_pain,acidity,vomiting,fatigue,
            weight_gain,anxiety,mood_swings,weight_loss,restlessness,irregular_sugar_level,cough,high_fever,
            breathlessness,sweating,dehydration,indigestion,headache,nausea,loss_of_appetite,back_pain,
            constipation,abdominal_pain,diarrhoea,mild_fever,yellow_urine,
        ]

        input_data_as_numpy_array = np.asarray(inputFeatures)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        new_data_predictions = model.predict(input_data_reshaped)
        new_data_predictions_decoded = label_encoder.inverse_transform(
            new_data_predictions
        )

        output = str(new_data_predictions_decoded).strip("['']")

        if output == "(vertigo) Paroymsal Positional Vertigo":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies -\n 
                1. Epley maneuver: This is a series of head movements that can help reposition displaced inner ear crystals causing vertigo.\n
                2. Stay hydrated to maintain fluid balance in the inner ear.
                        """
        elif output == "AIDS":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                There are no home remedies for treating AIDS. \n
                Consult a healthcare professional for appropriate medical management."""
        elif output == "Fungal infection":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Keep the affected area clean and dry.\n
                2. Use antifungal creams or powders.\n
                3. Wear loose, breathable clothing."""
        elif output == "Allergy":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Identify and avoid allergens.\n
                2. Use saline nasal rinses for nasal allergies.\n
                3. Consume honey (local, raw) to potentially alleviate seasonal allergies."""
        elif output == "GERD":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Avoid trigger foods and large meals.\n
                2. Elevate the head of your bed.\n
                3. Consume smaller, more frequent meals."""
        elif output == "Chronic cholestasis":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Follow a low-fat diet.\n
                2. Stay hydrated.\n
                3. Consume small, frequent meals."""
        elif output == "Drug Reaction":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Discontinue the suspected medication and seek medical attention.\n
                2. Take antihistamines for allergic reactions."""
        elif output == "Peptic ulcer diseae":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Avoid spicy and acidic foods.\n
                2. Consume smaller, more frequent meals.\n
                3. Manage stress through relaxation techniques."""
        elif output == "Diabetes":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n 
                1. Maintain a healthy diet and exercise regularly.\n
                2. Monitor blood sugar levels regularly.\n
                3. Include bitter gourd in the diet, which may help regulate blood sugar."""
        elif output == "Gastroenteritis":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Stay hydrated with electrolyte-rich fluids.\n
                2. Follow the BRAT diet (bananas, rice, applesauce, toast).\n
                3. Rest and avoid dairy and caffeine."""
        elif output == "Bronchial Asthma":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Use a humidifier to maintain indoor humidity.\n
                2. Consume honey with warm water to soothe the respiratory tract.\n
                3. Practice deep breathing exercises."""
        elif output == "Hypertension":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Adopt a low-sodium diet.\n
                2. Exercise regularly.\n
                3. Manage stress through relaxation techniques."""
        elif output == "Migraine":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Identify and avoid triggers.\n
                2. Apply cold or warm compresses to the head.\n
                3. Practice relaxation techniques."""
        elif output == "Cervical spondylosis":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Apply hot or cold packs to the affected area.\n
                2. Maintain good posture.\n
                3. Perform neck exercises to improve flexibility."""
        elif output == "Paralysis (brain hemorrhage)":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Seek emergency medical attention.\n
                2. Follow rehabilitation exercises as prescribed.\n
                3. Support emotional well-being through counseling."""
        elif output == "Jaundice":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Stay hydrated with water and electrolyte-rich beverages.\n
                2. Consume a diet rich in fruits and vegetables.\n
                3. Avoid alcohol and fatty foods."""
        elif output == "Malaria":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - 
                1. Use mosquito nets and repellents.\n
                2. Take antimalarial medications as prescribed.\n
                3. Stay in well-screened or air-conditioned accommodations."""
        elif output == "Chicken pox":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Oatmeal baths can soothe itching.\n
                2. Keep nails short to prevent scratching and infection.\n
                3. Use calamine lotion for skin relief."""
        elif output == "Dengue":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n 
                1. Stay hydrated with oral rehydration solutions.\n
                2. Get plenty of rest.\n
                3. Monitor platelet count and seek medical attention if necessary."""
        elif output == "Typhoid":
            user_diagnosis = f""" The person is having symptoms of {output}\n 
                You can use the following home remedies - \n 
                1. Take prescribed antibiotics.\n 
                2. Consume a well-cooked and hygienic diet.\n 
                3. Stay hydrated with oral rehydration solutions."""
        elif output == "hepatitis A":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Rest: Get plenty of rest to allow your body to recover.\n
                2. Hydration: Stay hydrated with water and electrolyte-rich beverages.\n
                3. Avoid Alcohol: Avoid alcohol consumption to reduce strain on the liver."""
        elif output == "Hepatitis B":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Consult a healthcare professional for appropriate medical management.\n
                2. Get vaccinated for Hepatitis B.\n
                3. Practice safe sex and avoid sharing needles."""
        elif output == "Hepatitis C":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Consult a healthcare professional for appropriate medical management.\n
                2. Get vaccinated.\n
                3. Practice safe sex and avoid sharing needles."""
        elif output == "Hepatitis D":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Consult a healthcare professional for appropriate medical management.\n
                2. Get vaccinated.\n
                3. Practice safe sex and avoid sharing needles."""
        elif output == "Hepatitis E":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Consult a healthcare professional for appropriate medical management.\n
                2. Get vaccinated.\n
                3. Practice safe sex and avoid sharing needles."""
        elif output == "Alcoholic hepatitis":
            user_diagnosis = f""" The person is having symptoms of {output}\n
            You can use the following home remedies - \n
                1. Abstain from alcohol.\n
                2. Consume a balanced diet rich in vitamins and minerals.\n
                3. Stay hydrated with water and electrolyte-rich beverages."""
        elif output == "Tuberculosis":
            user_diagnosis = f""" The person is having symptoms of {output}\n 
                You can use the following home remedies - \n 
                1. Follow the prescribed medication regimen.\n 
                2. Practice good respiratory hygiene.\n 
                3. Maintain a well-balanced diet."""
        elif output == "Common Cold":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Stay hydrated with warm fluids.\n
                2. Use saline nasal drops for congestion.\n
                3. Rest and get plenty of sleep."""
        elif output == "Pneumonia":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Get plenty of rest.\n
                2. Stay hydrated with warm fluids.\n
                3. Use a humidifier to ease breathing."""
        elif output == "Dimorphic hemmorhoids(piles)":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Consume a high-fiber diet to prevent constipation.\n
                2. Use sitz baths for comfort.\n
                3. Apply witch hazel or aloe vera gel to the affected area."""
        elif output == "Heart attack":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Seek emergency medical attention immediately.\n
                2. Chew aspirin if recommended by a healthcare professional.\n
                3. Stay calm and sit down while waiting for help."""
        elif output == "Varicose veins":
            user_diagnosis = f""" The person is having symptoms of {output}\n 
                You can use the following home remedies - \n 
                1. Elevate legs when resting.\n 
                2. Exercise regularly to improve circulation.\n 
                3. Wear compression stockings"""
        elif output == "Hypothyroidism":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Consume foods rich in iodine.\n
                2. Manage stress through yoga or meditation.\n
                3. Avoid stimulants like caffeine."""
        elif output == "Hypoglycemia":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Consume small, frequent meals.\n
                2. Include complex carbohydrates in your diet.\n
                3. Carry a snack for quick glucose boost."""
        elif output == "Osteoarthristis":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Exercise regularly to strengthen muscles.\n
                2. Apply hot or cold packs to affected joints.\n
                3. Maintain a healthy weight."""
        elif output == "Arthritis":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Maintain a healthy weight to reduce stress on joints.\n
                2. Apply cold or hot packs to affected joints.\n
                3. Exercise regularly with low-impact activities like swimming or walking."""
        elif output == "Acne":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Keep the skin clean by washing it with a mild cleanser.\n
                2. Use topical treatments with ingredients like benzoyl peroxide or salicylic acid.\n
                3. Apply a honey and cinnamon mask, as both have anti-inflammatory properties."""
        elif output == "Urinary tract infection":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies -\n 
                1. Stay hydrated with water.\n 
                2. Drink cranberry juice to help prevent UTIs.\n 
                3. Urinate frequently and maintain good hygiene."""
        elif output == "Psoriasis":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Keep the skin moisturized.\n
                2. Use medicated creams or ointments as prescribed.\n
                3. Avoid triggers like stress and alcohol."""
        elif output == "Impetigo":
            user_diagnosis = f""" The person is having symptoms of {output}\n
                You can use the following home remedies - \n
                1. Keep the affected area clean.\n
                2. Apply antibiotic ointment as prescribed.\n
                3. Avoid scratching and keep nails short."""

    st.success(user_diagnosis)

    if st.button("Show Map for Nearby Hospitals"):
        # Display the map only if the "Show Map" button is clicked
        st.plotly_chart(fig)

if __name__ == "_main_":
    main()