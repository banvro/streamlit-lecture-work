import google.generativeai as genai

genai.configure(api_key="AIzaSyCc97v8PAgOGtzVW_Qcc17ZI4Hwu8ek7-M")

model = genai.GenerativeModel('gemini-2.5-flash')

prompt = "Who created Python and when? Please answer in 3 lines."

response = model.generate_content(
    prompt, 
    generation_config={
        "temperature": 0.5,
        "max_output_tokens": 300,
        # Remove or carefully set stop_sequences
        "stop_sequences": ["\n\n"]  # Remove this
    }
)

print(response.text)
