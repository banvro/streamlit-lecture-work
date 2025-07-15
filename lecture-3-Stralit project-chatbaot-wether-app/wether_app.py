import streamlit as st 
import requests

st.title("🌧️ My Wether App")

cities_name = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata",
    "Surat", "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane",
    "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna", "Vadodara",
    "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot",
    "Kalyan-Dombivli", "Vasai-Virar", "Varanasi", "Srinagar", "Aurangabad", "Dhanbad",
    "Amritsar", "Navi Mumbai", "Allahabad (Prayagraj)", "Ranchi", "Howrah",
    "Coimbatore", "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur", "Madurai",
    "Raipur", "Kota", "Guwahati", "Chandigarh", "Solapur", "Hubballi–Dharwad",
    "Bareilly", "Moradabad", "Mysore", "Gurgaon (Gurugram)", "Aligarh",
    "Jalandhar", "Tiruchirappalli", "Bhubaneswar", "Salem", "Mira‑Bhayandar",
    "Thiruvananthapuram (Trivandrum)", "Bhiwandi", "Saharanpur", "Gorakhpur",
    "Guntur", "Bikaner", "Amravati", "Noida", "Jamshedpur", "Bhilai",
    "Warangal", "Mangalore", "Cuttack", "Firozabad", "Kochi (Cochin)", "Bhavnagar",
    "Dehradun", "Durgapur", "Asansol", "Nanded", "Kolhapur", "Ajmer", "Gulbarga",
    "Jamnagar", "Ujjain", "Loni", "Siliguri", "Jhansi", "Ulhasnagar", "Nellore",
    "Jammu", "Sangli-Miraj & Kupwad", "Belgaum (Belagavi)", "Ambattur", "Tirunelveli",
    "Malegaon", "Gaya", "Jalgaon", "Udaipur", "Maheshtala", "Mohali"
]

API_KEY = "33c8d612fd9e334126f2ec99c5b12661"



choice = st.selectbox("Choose Your City", cities_name)


if choice:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={choice}&appid={API_KEY}"

    responce = requests.get(url)

    if responce.status_code == 200:
        st.write("API working")
        # st.json(responce.json())

        wether_info = responce.json()

        # st.write(wether_info["weather"][0]["main"])

        st.json(wether_info)

        # col1, col2 = st.columns(2)

        # with col1:
        #     st.header(f)
    
    else:
        st.write("Somthing went wrong")