import streamlit as st

# ----------------------------- RULE SET 1: CROP RECOMMENDATION ----------------------------- #
# Realistic crop recommendations based on agricultural guidelines
# ----------------------------- FIXED: CROP RULES (More Coverage) ----------------------------- #
crop_rules = [
    {"conditions": {"soil": "loamy", "rainfall": "high", "temperature": "moderate"}, "recommendation": "Rice"},
    {"conditions": {"soil": "loamy", "rainfall": "medium", "temperature": "hot"}, "recommendation": "Sugarcane"},
    {"conditions": {"soil": "loamy", "rainfall": "low", "temperature": "hot"}, "recommendation": "Cotton"},
    {"conditions": {"soil": "loamy", "rainfall": "low", "temperature": "cool"}, "recommendation": "Mustard"},
    {"conditions": {"soil": "loamy", "rainfall": "medium", "temperature": "moderate"}, "recommendation": "Sunflower"},

    {"conditions": {"soil": "sandy", "rainfall": "low", "temperature": "hot"}, "recommendation": "Millet"},
    {"conditions": {"soil": "sandy", "rainfall": "medium", "temperature": "moderate"}, "recommendation": "Groundnut"},
    {"conditions": {"soil": "sandy", "rainfall": "high", "temperature": "moderate"}, "recommendation": "Maize"},
    {"conditions": {"soil": "sandy", "rainfall": "medium", "temperature": "cool"}, "recommendation": "Peas"},
    {"conditions": {"soil": "sandy", "rainfall": "low", "temperature": "cool"}, "recommendation": "Chickpea"},

    {"conditions": {"soil": "clay", "rainfall": "medium", "temperature": "cool"}, "recommendation": "Wheat"},
    {"conditions": {"soil": "clay", "rainfall": "high", "temperature": "hot"}, "recommendation": "Paddy"},
    {"conditions": {"soil": "clay", "rainfall": "low", "temperature": "cool"}, "recommendation": "Barley"},
    {"conditions": {"soil": "clay", "rainfall": "medium", "temperature": "moderate"}, "recommendation": "Soybean"},
    {"conditions": {"soil": "clay", "rainfall": "high", "temperature": "moderate"}, "recommendation": "Banana"},
]

# ----------------------------- FIXED: FERTILIZER RULES (More Matches) ----------------------------- #
fertilizer_rules = [
    # --- Rice ---
    {"conditions": {"crop": "Rice", "soil": "loamy", "deficiency": "nitrogen"}, "recommendation": "Urea or Ammonium Sulphate"},
    {"conditions": {"crop": "Rice", "soil": "loamy", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Rice", "soil": "loamy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Rice", "soil": "loamy", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},
    {"conditions": {"crop": "Rice", "soil": "sandy", "deficiency": "nitrogen"}, "recommendation": "Urea"},
    {"conditions": {"crop": "Rice", "soil": "sandy", "deficiency": "phosphorus"}, "recommendation": "Single Super Phosphate"},
    {"conditions": {"crop": "Rice", "soil": "sandy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Rice", "soil": "sandy", "deficiency": "zinc"}, "recommendation": "Zinc EDTA"},
    {"conditions": {"crop": "Rice", "soil": "clay", "deficiency": "nitrogen"}, "recommendation": "Ammonium Nitrate"},
    {"conditions": {"crop": "Rice", "soil": "clay", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Rice", "soil": "clay", "deficiency": "potassium"}, "recommendation": "Sulfate of Potash"},
    {"conditions": {"crop": "Rice", "soil": "clay", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate (25kg/ha)"},

    # --- Wheat ---
    {"conditions": {"crop": "Wheat", "soil": "loamy", "deficiency": "nitrogen"}, "recommendation": "Split application of Urea"},
    {"conditions": {"crop": "Wheat", "soil": "loamy", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Wheat", "soil": "loamy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Wheat", "soil": "loamy", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},
    {"conditions": {"crop": "Wheat", "soil": "sandy", "deficiency": "nitrogen"}, "recommendation": "Urea"},
    {"conditions": {"crop": "Wheat", "soil": "sandy", "deficiency": "phosphorus"}, "recommendation": "SSP"},
    {"conditions": {"crop": "Wheat", "soil": "sandy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Wheat", "soil": "sandy", "deficiency": "zinc"}, "recommendation": "Zinc EDTA"},
    {"conditions": {"crop": "Wheat", "soil": "clay", "deficiency": "nitrogen"}, "recommendation": "Ammonium Nitrate"},
    {"conditions": {"crop": "Wheat", "soil": "clay", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Wheat", "soil": "clay", "deficiency": "potassium"}, "recommendation": "SOP"},
    {"conditions": {"crop": "Wheat", "soil": "clay", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},

    # --- Sugarcane ---
    {"conditions": {"crop": "Sugarcane", "soil": "loamy", "deficiency": "nitrogen"}, "recommendation": "Apply Urea in 2 split doses"},
    {"conditions": {"crop": "Sugarcane", "soil": "loamy", "deficiency": "phosphorus"}, "recommendation": "DAP at planting"},
    {"conditions": {"crop": "Sugarcane", "soil": "loamy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Sugarcane", "soil": "loamy", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},
    {"conditions": {"crop": "Sugarcane", "soil": "sandy", "deficiency": "nitrogen"}, "recommendation": "Urea"},
    {"conditions": {"crop": "Sugarcane", "soil": "sandy", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Sugarcane", "soil": "sandy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Sugarcane", "soil": "sandy", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},
    {"conditions": {"crop": "Sugarcane", "soil": "clay", "deficiency": "nitrogen"}, "recommendation": "Urea"},
    {"conditions": {"crop": "Sugarcane", "soil": "clay", "deficiency": "phosphorus"}, "recommendation": "SSP"},
    {"conditions": {"crop": "Sugarcane", "soil": "clay", "deficiency": "potassium"}, "recommendation": "SOP"},
    {"conditions": {"crop": "Sugarcane", "soil": "clay", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},

    # --- Groundnut ---
    {"conditions": {"crop": "Groundnut", "soil": "loamy", "deficiency": "nitrogen"}, "recommendation": "Minimal N needed, use compost or FYM"},
    {"conditions": {"crop": "Groundnut", "soil": "loamy", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Groundnut", "soil": "loamy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Groundnut", "soil": "loamy", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},
    {"conditions": {"crop": "Groundnut", "soil": "sandy", "deficiency": "nitrogen"}, "recommendation": "Apply compost or urea"},
    {"conditions": {"crop": "Groundnut", "soil": "sandy", "deficiency": "phosphorus"}, "recommendation": "SSP"},
    {"conditions": {"crop": "Groundnut", "soil": "sandy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Groundnut", "soil": "sandy", "deficiency": "zinc"}, "recommendation": "Zinc EDTA"},
    {"conditions": {"crop": "Groundnut", "soil": "clay", "deficiency": "nitrogen"}, "recommendation": "Organic manure"},
    {"conditions": {"crop": "Groundnut", "soil": "clay", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Groundnut", "soil": "clay", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Groundnut", "soil": "clay", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},

    # --- Maize ---
    {"conditions": {"crop": "Maize", "soil": "loamy", "deficiency": "nitrogen"}, "recommendation": "Urea in split doses"},
    {"conditions": {"crop": "Maize", "soil": "loamy", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Maize", "soil": "loamy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Maize", "soil": "loamy", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},
    {"conditions": {"crop": "Maize", "soil": "sandy", "deficiency": "nitrogen"}, "recommendation": "Ammonium Nitrate"},
    {"conditions": {"crop": "Maize", "soil": "sandy", "deficiency": "phosphorus"}, "recommendation": "SSP"},
    {"conditions": {"crop": "Maize", "soil": "sandy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Maize", "soil": "sandy", "deficiency": "zinc"}, "recommendation": "Zinc EDTA"},
    {"conditions": {"crop": "Maize", "soil": "clay", "deficiency": "nitrogen"}, "recommendation": "Urea"},
    {"conditions": {"crop": "Maize", "soil": "clay", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Maize", "soil": "clay", "deficiency": "potassium"}, "recommendation": "SOP"},
    {"conditions": {"crop": "Maize", "soil": "clay", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},

    # --- Cotton ---
    {"conditions": {"crop": "Cotton", "soil": "loamy", "deficiency": "nitrogen"}, "recommendation": "Urea"},
    {"conditions": {"crop": "Cotton", "soil": "loamy", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Cotton", "soil": "loamy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Cotton", "soil": "loamy", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},
    {"conditions": {"crop": "Cotton", "soil": "sandy", "deficiency": "nitrogen"}, "recommendation": "Urea"},
    {"conditions": {"crop": "Cotton", "soil": "sandy", "deficiency": "phosphorus"}, "recommendation": "SSP"},
    {"conditions": {"crop": "Cotton", "soil": "sandy", "deficiency": "potassium"}, "recommendation": "MOP"},
    {"conditions": {"crop": "Cotton", "soil": "sandy", "deficiency": "zinc"}, "recommendation": "Zinc EDTA"},
    {"conditions": {"crop": "Cotton", "soil": "clay", "deficiency": "nitrogen"}, "recommendation": "Ammonium Nitrate"},
    {"conditions": {"crop": "Cotton", "soil": "clay", "deficiency": "phosphorus"}, "recommendation": "DAP"},
    {"conditions": {"crop": "Cotton", "soil": "clay", "deficiency": "potassium"}, "recommendation": "SOP"},
    {"conditions": {"crop": "Cotton", "soil": "clay", "deficiency": "zinc"}, "recommendation": "Zinc Sulphate"},
]

# ----------------------------- INFERENCE ENGINE ----------------------------- #
def infer(knowledge, rules):
    for rule in rules:
        if all(knowledge.get(k) == v for k, v in rule["conditions"].items()):
            return rule["recommendation"]
    return "No suitable recommendation found."

# ----------------------------- STREAMLIT UI ----------------------------- #
st.set_page_config(page_title="Smart Agriculture Expert System", page_icon="🌱")
st.title("🌾 Smart Agriculture Expert System")

# Sidebar menu
option = st.sidebar.radio("Choose Expert System", ["Crop Recommendation", "Fertilizer Recommendation"])

# ----------------------------- CROP RECOMMENDATION UI ----------------------------- #
if option == "Crop Recommendation":
    st.header("🚜 Crop Recommendation Engine")
    soil = st.selectbox("🧱 Soil Type", ["loamy", "sandy", "clay"])
    rainfall = st.selectbox("🌧 Rainfall Level", ["low", "medium", "high"])
    temperature = st.selectbox("🌡 Temperature", ["cool", "moderate", "hot"])

    if st.button("Get Crop Recommendation"):
        knowledge = {
            "soil": soil,
            "rainfall": rainfall,
            "temperature": temperature
        }
        st.write("🔍 You entered:", knowledge)
        result = infer(knowledge, crop_rules)
        if "No suitable" in result:
            st.warning(result)
        else:
            st.success(f"✅ Recommended Crop: {result}")

# ----------------------------- FERTILIZER RECOMMENDATION UI ----------------------------- #
elif option == "Fertilizer Recommendation":
    st.header("🌿 Fertilizer Recommendation Engine")
    crop = st.selectbox("🌾 Crop", ["Rice", "Wheat", "Sugarcane", "Groundnut", "Maize", "Cotton"])
    soil = st.selectbox("🧱 Soil Type", ["loamy", "sandy", "clay"])
    deficiency = st.selectbox("💧 Nutrient Deficiency", ["nitrogen", "phosphorus", "potassium", "zinc"])

    if st.button("Get Fertilizer Recommendation"):
        knowledge = {
            "crop": crop,
            "soil": soil,
            "deficiency": deficiency
        }
        st.write("🔍 You entered:", knowledge)
        result = infer(knowledge, fertilizer_rules)
        if "No suitable" in result:
            st.warning(result)
        else:
            st.success(f"✅ Recommended Fertilizer: {result}")
