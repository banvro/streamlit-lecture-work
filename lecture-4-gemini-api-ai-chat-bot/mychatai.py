import google.generativeai as genai

API_KEY = "AIzaSyD9VvF3WZjNCpJr2rfm1cWb7JqkEg8jbn8"

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")   

query = "who build python and when python devloped"

responce = model.generate_content(query)

print(responce.text)