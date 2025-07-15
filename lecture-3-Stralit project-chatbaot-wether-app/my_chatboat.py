import streamlit as st 
import wikipedia

st.title("🤖 My ChatBOT")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_responce(user_inp):
    lower_inp = user_inp.lower()

    if "how are you" in lower_inp:
        return "am good! thank you for asking.."
    
    elif "who build you" in lower_inp:
        return "bot ai"
    
    # elif ""
    
    else:
        try:
            answer = wikipedia.summary(lower_inp, sentences = 2)

            return answer + " 🤖"
        
        except Exception:
            return "Somethong Went wrong with bot...!"



user_inp = st.chat_input("How can i help you?")

if user_inp:
    st.session_state.chat_history.append(("user", user_inp))
    reponcees = get_responce(user_inp)
    st.session_state.chat_history.append(("bot", reponcees))

for key, data in st.session_state.chat_history:
    
    with st.chat_message(key):
        st.markdown(data)