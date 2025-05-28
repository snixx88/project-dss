import streamlit as st

# ----------------------------- RULE SET 1: DISEASE DIAGNOSIS ----------------------------- #
diagnosis_rules = [
    # Existing rules
    {"conditions": {"fever": True, "cough": True, "fatigue": True}, "recommendation": "Flu"},
    {"conditions": {"fever": True, "rash": True, "joint_pain": True}, "recommendation": "Dengue"},
    {"conditions": {"headache": True, "sensitivity_to_light": True, "stiff_neck": True}, "recommendation": "Meningitis"},
    {"conditions": {"cough": True, "shortness_of_breath": True, "chest_pain": True}, "recommendation": "Pneumonia"},
    {"conditions": {"fever": True, "diarrhea": True, "vomiting": True}, "recommendation": "Food Poisoning"},
    {"conditions": {"sore_throat": True, "fever": True, "swollen_lymph_nodes": True}, "recommendation": "Strep Throat"},
    {"conditions": {"sneezing": True, "runny_nose": True, "itchy_eyes": True}, "recommendation": "Allergic Rhinitis"},
    {"conditions": {"nausea": True, "vomiting": True, "abdominal_pain": True}, "recommendation": "Gastroenteritis"},
    {"conditions": {"chest_pain": True, "shortness_of_breath": True, "sweating": True}, "recommendation": "Heart Attack"},
    {"conditions": {"fever": True, "night_sweats": True, "weight_loss": True}, "recommendation": "Tuberculosis"},
    {"conditions": {"headache": True, "blurred_vision": True, "nausea": True}, "recommendation": "Migraine"},
    {"conditions": {"fatigue": True, "pale_skin": True, "shortness_of_breath": True}, "recommendation": "Anemia"},
    {"conditions": {"joint_pain": True, "morning_stiffness": True, "swollen_joints": True}, "recommendation": "Rheumatoid Arthritis"},
    {"conditions": {"cough": True, "wheezing": True, "shortness_of_breath": True}, "recommendation": "Asthma"},
    {"conditions": {"burning_urination": True, "frequent_urination": True, "lower_abdominal_pain": True}, "recommendation": "Urinary Tract Infection"},

    # New short-combination rules
    {"conditions": {"fever": True, "cough": True}, "recommendation": "Upper Respiratory Infection"},
    {"conditions": {"vomiting": True, "diarrhea": True}, "recommendation": "Stomach Virus"},
    {"conditions": {"headache": True, "nausea": True}, "recommendation": "Tension Headache"},
    {"conditions": {"cough": True, "sore_throat": True}, "recommendation": "Common Cold"},
    {"conditions": {"rash": True, "itchy_eyes": True}, "recommendation": "Allergic Reaction"},
    {"conditions": {"joint_pain": True, "fatigue": True}, "recommendation": "Lupus"},
    {"conditions": {"abdominal_pain": True, "bloating": True}, "recommendation": "Indigestion"},
    {"conditions": {"fever": True, "body_ache": True}, "recommendation": "Viral Fever"},
    {"conditions": {"fatigue": True, "weight_loss": True}, "recommendation": "Thyroid Disorder"},
    {"conditions": {"runny_nose": True, "sneezing": True}, "recommendation": "Cold or Allergy"},
    {"conditions": {"sore_throat": True, "runny_nose": True}, "recommendation": "Pharyngitis"},
    {"conditions": {"cough": True, "wheezing": True}, "recommendation": "Bronchitis"},
    {"conditions": {"burning_urination": True, "frequent_urination": True}, "recommendation": "Bladder Infection"},
    {"conditions": {"chest_pain": True, "fatigue": True}, "recommendation": "Angina"},
    {"conditions": {"dizziness": True, "blurred_vision": True}, "recommendation": "Hypoglycemia"},
    {"conditions": {"fatigue": True, "constipation": True}, "recommendation": "Hypothyroidism"}, {"conditions": {"fatigue": True, "dizziness": True}, "recommendation": "Dehydration"},
    {"conditions": {"fever": True, "chills": True}, "recommendation": "Infection"},
    {"conditions": {"sore_throat": True, "runny_nose": True, "cough": True}, "recommendation": "Viral Upper Respiratory Infection"},
    {"conditions": {"abdominal_pain": True, "diarrhea": True}, "recommendation": "Irritable Bowel Syndrome"},
    {"conditions": {"joint_pain": True, "swelling": True}, "recommendation": "Arthritis"},
    {"conditions": {"nausea": True, "loss_of_appetite": True}, "recommendation": "Gastritis"},
    {"conditions": {"cough": True, "fatigue": True}, "recommendation": "Chronic Bronchitis"},
    {"conditions": {"fever": True, "headache": True}, "recommendation": "Viral Infection"},
    {"conditions": {"rash": True, "fever": True}, "recommendation": "Measles"},
    {"conditions": {"burning_urination": True, "back_pain": True}, "recommendation": "Kidney Infection"},
    {"conditions": {"shortness_of_breath": True, "fatigue": True}, "recommendation": "Chronic Obstructive Pulmonary Disease (COPD)"},
    {"conditions": {"chest_pain": True, "dizziness": True}, "recommendation": "Cardiac Arrhythmia"},
    {"conditions": {"vomiting": True, "loss_of_appetite": True}, "recommendation": "Peptic Ulcer"},
    {"conditions": {"nausea": True, "dizziness": True}, "recommendation": "Vertigo"},
    {"conditions": {"headache": True, "difficulty_concentrating": True}, "recommendation": "Tension Headache"},
    {"conditions": {"sensitivity_to_light": True, "nausea": True}, "recommendation": "Migraine"},
    {"conditions": {"fever": True, "abdominal_pain": True}, "recommendation": "Appendicitis"},
    {"conditions": {"bloating": True, "constipation": True}, "recommendation": "Constipation"},
    {"conditions": {"sore_throat": True, "ear_pain": True}, "recommendation": "Throat Infection"},
    {"conditions": {"cough": True, "night_sweats": True}, "recommendation": "Tuberculosis"},
    {"conditions": {"weight_loss": True, "frequent_urination": True}, "recommendation": "Diabetes"},
    {"conditions": {"itchy_skin": True, "rash": True}, "recommendation": "Eczema"},
    {"conditions": {"fever": True, "swollen_lymph_nodes": True}, "recommendation": "Mononucleosis"},
    {"conditions": {"abdominal_pain": True, "vomiting": True}, "recommendation": "Gallstones"},
    {"conditions": {"muscle_pain": True, "fatigue": True}, "recommendation": "Influenza"},
    {"conditions": {"fever": True}, "recommendation": "Possible Infection"},
{"conditions": {"cough": True}, "recommendation": "Possible Respiratory Issue"},
{"conditions": {"headache": True}, "recommendation": "General Headache"},

]


# ----------------------------- RULE SET 2: MEDICATION RECOMMENDATION ----------------------------- #
medication_rules = [
    # Flu
    {"conditions": {"disease": "Flu", "age_group": "adult"}, "recommendation": "Paracetamol and rest"},
    {"conditions": {"disease": "Flu", "age_group": "child"}, "recommendation": "Children's Tylenol and fluids"},

    # Dengue
    {"conditions": {"disease": "Dengue", "age_group": "adult"}, "recommendation": "Hydration and Acetaminophen"},
    {"conditions": {"disease": "Dengue", "age_group": "child"}, "recommendation": "Hydration and Pediatric Paracetamol"},

    # Meningitis
    {"conditions": {"disease": "Meningitis", "age_group": "adult"}, "recommendation": "Immediate hospitalization and IV antibiotics"},
    {"conditions": {"disease": "Meningitis", "age_group": "child"}, "recommendation": "Emergency care and IV antibiotics"},

    # Pneumonia
    {"conditions": {"disease": "Pneumonia", "age_group": "adult"}, "recommendation": "Azithromycin or Amoxicillin"},
    {"conditions": {"disease": "Pneumonia", "age_group": "child"}, "recommendation": "Pediatric antibiotics (Amoxicillin Suspension)"},

    # Food Poisoning
    {"conditions": {"disease": "Food Poisoning", "age_group": "adult"}, "recommendation": "ORS and Activated Charcoal"},
    {"conditions": {"disease": "Food Poisoning", "age_group": "child"}, "recommendation": "ORS and Zinc Tablets"},

    # Migraine
    {"conditions": {"disease": "Migraine", "age_group": "adult"}, "recommendation": "Ibuprofen or Sumatriptan"},
    {"conditions": {"disease": "Migraine", "age_group": "child"}, "recommendation": "Pediatric Ibuprofen and rest"},

    # Malaria
    {"conditions": {"disease": "Malaria", "age_group": "adult"}, "recommendation": "Artemisinin-based combination therapy"},
    {"conditions": {"disease": "Malaria", "age_group": "child"}, "recommendation": "Pediatric ACT under medical supervision"},

    # COVID-19
    {"conditions": {"disease": "COVID-19", "age_group": "adult"}, "recommendation": "Paracetamol, hydration, and isolation"},
    {"conditions": {"disease": "COVID-19", "age_group": "child"}, "recommendation": "Pediatric fever reducers and fluids"},

    # UTI
    {"conditions": {"disease": "Urinary Tract Infection", "age_group": "adult"}, "recommendation": "Ciprofloxacin or Nitrofurantoin"},
    {"conditions": {"disease": "Urinary Tract Infection", "age_group": "child"}, "recommendation": "Pediatric antibiotics after urine culture"},

    # Asthma
    {"conditions": {"disease": "Asthma", "age_group": "adult"}, "recommendation": "Inhaled bronchodilators (e.g., Salbutamol)"},
    {"conditions": {"disease": "Asthma", "age_group": "child"}, "recommendation": "Pediatric inhalers (Salbutamol Syrup or Nebulizer)"},

    # Sinusitis
    {"conditions": {"disease": "Sinusitis", "age_group": "adult"}, "recommendation": "Decongestants and Amoxicillin"},
    {"conditions": {"disease": "Sinusitis", "age_group": "child"}, "recommendation": "Nasal saline drops and pediatric antibiotics"},

    # Allergic Rhinitis
    {"conditions": {"disease": "Allergic Rhinitis", "age_group": "adult"}, "recommendation": "Antihistamines (e.g., Cetirizine)"},
    {"conditions": {"disease": "Allergic Rhinitis", "age_group": "child"}, "recommendation": "Pediatric antihistamines (e.g., Loratadine syrup)"},

    # Typhoid
    {"conditions": {"disease": "Typhoid", "age_group": "adult"}, "recommendation": "Cefixime or Azithromycin"},
    {"conditions": {"disease": "Typhoid", "age_group": "child"}, "recommendation": "Pediatric Cefixime and hydration"},

    # Bronchitis
    {"conditions": {"disease": "Bronchitis", "age_group": "adult"}, "recommendation": "Cough suppressants and rest"},
    {"conditions": {"disease": "Bronchitis", "age_group": "child"}, "recommendation": "Pediatric cough syrup and fluids"},

    # Strep Throat
    {"conditions": {"disease": "Strep Throat", "age_group": "adult"}, "recommendation": "Penicillin or Amoxicillin"},
    {"conditions": {"disease": "Strep Throat", "age_group": "child"}, "recommendation": "Pediatric antibiotics after throat swab"},

    # Additions
    {"conditions": {"disease": "Heart Attack", "age_group": "adult"}, "recommendation": "Aspirin and emergency cardiac care"},
    {"conditions": {"disease": "Heart Attack", "age_group": "child"}, "recommendation": "Immediate hospitalization (pediatric cardiology)"},

    {"conditions": {"disease": "Tuberculosis", "age_group": "adult"}, "recommendation": "Rifampicin, Isoniazid, Pyrazinamide, and Ethambutol"},
    {"conditions": {"disease": "Tuberculosis", "age_group": "child"}, "recommendation": "Pediatric TB regimen under supervision"},

    {"conditions": {"disease": "Anemia", "age_group": "adult"}, "recommendation": "Iron supplements and folic acid"},
    {"conditions": {"disease": "Anemia", "age_group": "child"}, "recommendation": "Iron syrup and vitamin supplementation"},

    {"conditions": {"disease": "Rheumatoid Arthritis", "age_group": "adult"}, "recommendation": "NSAIDs and DMARDs (e.g., Methotrexate)"},
    {"conditions": {"disease": "Rheumatoid Arthritis", "age_group": "child"}, "recommendation": "Pediatric rheumatology referral and NSAIDs"},

    {"conditions": {"disease": "Asthma", "age_group": "adult"}, "recommendation": "Inhaled corticosteroids and bronchodilators"},
    {"conditions": {"disease": "Asthma", "age_group": "child"}, "recommendation": "Salbutamol nebulizer and pediatric ICS"},

    {"conditions": {"disease": "Allergic Rhinitis", "age_group": "adult"}, "recommendation": "Loratadine or Cetirizine"},
    {"conditions": {"disease": "Allergic Rhinitis", "age_group": "child"}, "recommendation": "Loratadine syrup or nasal saline"},

    {"conditions": {"disease": "Gastroenteritis", "age_group": "adult"}, "recommendation": "ORS, antiemetics, and rest"},
    {"conditions": {"disease": "Gastroenteritis", "age_group": "child"}, "recommendation": "ORS, zinc, and pediatric antiemetics"},

    {"conditions": {"disease": "Migraine", "age_group": "adult"}, "recommendation": "NSAIDs, Sumatriptan, and rest"},
    {"conditions": {"disease": "Migraine", "age_group": "child"}, "recommendation": "Pediatric analgesics and quiet environment"},

    {"conditions": {"disease": "Diabetes", "age_group": "adult"}, "recommendation": "Metformin or insulin depending on type"},
    {"conditions": {"disease": "Diabetes", "age_group": "child"}, "recommendation": "Insulin therapy and diet planning"},

    {"conditions": {"disease": "Constipation", "age_group": "adult"}, "recommendation": "Laxatives and high-fiber diet"},
    {"conditions": {"disease": "Constipation", "age_group": "child"}, "recommendation": "Lactulose syrup and increased fluid intake"},

    {"conditions": {"disease": "Appendicitis", "age_group": "adult"}, "recommendation": "Surgical intervention and antibiotics"},
    {"conditions": {"disease": "Appendicitis", "age_group": "child"}, "recommendation": "Surgical evaluation and pediatric antibiotics"},

    {"conditions": {"disease": "Thyroid Disorder", "age_group": "adult"}, "recommendation": "Levothyroxine (for hypothyroid)"},
    {"conditions": {"disease": "Thyroid Disorder", "age_group": "child"}, "recommendation": "Pediatric endocrinology evaluation"},

    {"conditions": {"disease": "Lupus", "age_group": "adult"}, "recommendation": "Hydroxychloroquine and corticosteroids"},
    {"conditions": {"disease": "Lupus", "age_group": "child"}, "recommendation": "Specialist care and pediatric immunosuppressants"},
]
# ----------------------------- INFERENCE ENGINE ----------------------------- #
def infer(knowledge, rules):
    for rule in rules:
        if all(knowledge.get(k) == v for k, v in rule["conditions"].items()):
            return rule["recommendation"]
    return "No suitable recommendation found."

# ----------------------------- STREAMLIT UI ----------------------------- #
st.set_page_config(page_title="Smart Healthcare Expert System", page_icon="🩺")
st.title("🧠 Smart Healthcare Expert System")

# Sidebar menu
option = st.sidebar.radio("Choose Expert System", ["Disease Diagnosis", "Medication Recommendation"])

# ----------------------------- DISEASE DIAGNOSIS UI ----------------------------- #
if option == "Disease Diagnosis":
    st.header("🔍 Symptom Checker")
    fever = st.checkbox("🌡 Fever")
    cough = st.checkbox("🤧 Cough")
    fatigue = st.checkbox("😴 Fatigue")
    rash = st.checkbox("🤕 Rash")
    joint_pain = st.checkbox("🦴 Joint Pain")
    headache = st.checkbox("🤯 Headache")
    sensitivity_to_light = st.checkbox("💡 Sensitivity to Light")
    stiff_neck = st.checkbox("🧍‍♂️ Stiff Neck")
    shortness_of_breath = st.checkbox("😮‍💨 Shortness of Breath")
    chest_pain = st.checkbox("❤️ Chest Pain")
    diarrhea = st.checkbox("💩 Diarrhea")
    vomiting = st.checkbox("🤮 Vomiting")

    if st.button("Get Diagnosis"):
        knowledge = {
            "fever": fever,
            "cough": cough,
            "fatigue": fatigue,
            "rash": rash,
            "joint_pain": joint_pain,
            "headache": headache,
            "sensitivity_to_light": sensitivity_to_light,
            "stiff_neck": stiff_neck,
            "shortness_of_breath": shortness_of_breath,
            "chest_pain": chest_pain,
            "diarrhea": diarrhea,
            "vomiting": vomiting,
        }
        st.write("🔎 Symptoms Selected:", [k for k, v in knowledge.items() if v])
        result = infer(knowledge, diagnosis_rules)
        if "No suitable" in result:
            st.warning(result)
        else:
            st.success(f"🩺 Possible Diagnosis: {result}")

# ----------------------------- MEDICATION RECOMMENDATION UI ----------------------------- #
elif option == "Medication Recommendation":
    st.header("💊 Medication Suggestion")
    disease = st.selectbox("🦠 Diagnosed Disease", [
    "Flu", "Dengue", "Meningitis", "Pneumonia", "Food Poisoning",
    "Heart Attack", "Tuberculosis", "Anemia", "Rheumatoid Arthritis",
    "Asthma", "Allergic Rhinitis", "Gastroenteritis", "Migraine",
    "Diabetes", "Constipation", "Appendicitis", "Thyroid Disorder", "Lupus"])
    age_group = st.radio("👤 Age Group", ["adult", "child"])

    if st.button("Get Medication Advice"):
        knowledge = {
            "disease": disease,
            "age_group": age_group
        }
        st.write("📋 Selected Conditions:", knowledge)
        result = infer(knowledge, medication_rules)
        if "No suitable" in result:
            st.warning(result)
        else:
            st.success(f"💊 Recommended Medication: {result}")
