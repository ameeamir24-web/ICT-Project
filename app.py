import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Unit Converter & Material Density Checker",
    page_icon="⚙️",
    layout="centered"
)

# Title
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")

# Student Information
st.markdown("### Developed By")
st.write("**Name:** Ameer ud din")
st.write("**Roll Number:** 25-ME-232")

st.markdown("---")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Select Option",
    ["Unit Converter", "Material Density Checker"]
)

# ---------------- UNIT CONVERTER ----------------
if menu == "Unit Converter":
    st.header("🔄 Mechanical Unit Converter")

    conversion_type = st.selectbox(
        "Choose Conversion Type",
        ["Length", "Force", "Pressure"]
    )

    # LENGTH CONVERTER
    if conversion_type == "Length":
        value = st.number_input("Enter value", min_value=0.0)

        from_unit = st.selectbox("From", ["Meter", "Millimeter", "Centimeter"])
        to_unit = st.selectbox("To", ["Meter", "Millimeter", "Centimeter"])

        # Convert to meters first
        conversion_to_meter = {
            "Meter": 1,
            "Millimeter": 0.001,
            "Centimeter": 0.01
        }

        result = value * conversion_to_meter[from_unit] / conversion_to_meter[to_unit]

        st.success(f"Converted Value: {result:.4f} {to_unit}")

    # FORCE CONVERTER
    elif conversion_type == "Force":
        value = st.number_input("Enter force value", min_value=0.0)

        from_unit = st.selectbox("From Force Unit", ["Newton", "Kilonewton"])
        to_unit = st.selectbox("To Force Unit", ["Newton", "Kilonewton"])

        conversion_force = {
            "Newton": 1,
            "Kilonewton": 1000
        }

        result = value * conversion_force[from_unit] / conversion_force[to_unit]

        st.success(f"Converted Force: {result:.4f} {to_unit}")

    # PRESSURE CONVERTER
    elif conversion_type == "Pressure":
        value = st.number_input("Enter pressure value", min_value=0.0)

        from_unit = st.selectbox("From Pressure Unit", ["Pascal", "Kilopascal"])
        to_unit = st.selectbox("To Pressure Unit", ["Pascal", "Kilopascal"])

        conversion_pressure = {
            "Pascal": 1,
            "Kilopascal": 1000
        }

        result = value * conversion_pressure[from_unit] / conversion_pressure[to_unit]

        st.success(f"Converted Pressure: {result:.4f} {to_unit}")


# ---------------- DENSITY CHECKER ----------------
elif menu == "Material Density Checker":
    st.header("🧱 Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Cast Iron": 7200
    }

    material = st.selectbox("Select Material", list(materials.keys()))

    density = materials[material]

    st.info(f"Density of {material} is {density} kg/m³")

    st.markdown("### Density Classification")

    if density > 7000:
        st.success("This is a High Density Material.")
    elif density > 3000:
        st.warning("This is a Medium Density Material.")
    else:
        st.error("This is a Low Density Material.")

# Footer
st.markdown("---")
st.caption("Mechanical Engineering Mini Project using Streamlit")
