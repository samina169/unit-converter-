import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Unit Converter",
    page_icon="📏",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("📏 Universal Unit Converter")
st.markdown("Convert between different units easily!")

# Dictionary of conversion factors
conversion_factors = {
    'Length': {
        'Meters': 1,
        'Kilometers': 1000,
        'Centimeters': 0.01,
        'Millimeters': 0.001,
        'Inches': 0.0254,
        'Feet': 0.3048,
        'Yards': 0.9144,
        'Miles': 1609.34
    },
    'Weight': {
        'Grams': 1,
        'Kilograms': 1000,
        'Milligrams': 0.001,
        'Pounds': 453.592,
        'Ounces': 28.3495
    },
    'Temperature': {
        'Celsius': 1,
        'Fahrenheit': 1,
        'Kelvin': 1
    },
    'Area': {
        'Square Meters': 1,
        'Square Kilometers': 1000000,
        'Square Feet': 0.092903,
        'Square Miles': 2589988.11,
        'Acres': 4046.86
    }
}

# Temperature conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

# Create the conversion interface
category = st.selectbox("Select Category", list(conversion_factors.keys()))

if category == 'Temperature':
    # Special handling for temperature
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(conversion_factors[category].keys()))
    with col2:
        to_unit = st.selectbox("To", list(conversion_factors[category].keys()))
    
    value = st.number_input("Enter value", value=0.0)
    
    if st.button("Convert"):
        if from_unit == to_unit:
            result = value
        elif from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            result = celsius_to_fahrenheit(value)
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            result = fahrenheit_to_celsius(value)
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            result = celsius_to_kelvin(value)
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            result = kelvin_to_celsius(value)
        elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
            result = celsius_to_kelvin(fahrenheit_to_celsius(value))
        elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
            result = celsius_to_fahrenheit(kelvin_to_celsius(value))
        
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
else:
    # Handling for other categories
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(conversion_factors[category].keys()))
    with col2:
        to_unit = st.selectbox("To", list(conversion_factors[category].keys()))
    
    value = st.number_input("Enter value", value=0.0)
    
    if st.button("Convert"):
        # Convert to base unit first, then to target unit
        base_value = value * conversion_factors[category][from_unit]
        result = base_value / conversion_factors[category][to_unit]
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")

# Add some information about the converter
st.markdown("---")
st.markdown("""
### About this Converter
- Supports multiple categories: Length, Weight, Temperature, and Area
- Easy to use interface
- Accurate conversions
- Real-time results
""") 