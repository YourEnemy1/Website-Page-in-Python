from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs
import base64

st.set_page_config(page_title="My Webpage", page_icon=":world_map:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local Css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)   
local_css("style/style.css")


# Set Background Image
def set_bg(main_bg):
    # set bg name
    main_bg_ext = "jpg"
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg(main_bg="./images/bg_image1.jpg")

# --- Load Assets ---
lottie_coding = load_lottieurl("https://lottie.host/ccd351fa-6625-4172-9082-8133922133d6/V9YuUtgXl2.json")
lottie_email = load_lottieurl("https://lottie.host/cf262121-a926-4935-b875-de2f0c5e1443/egpAV4JoPj.json")
img_project1 = Image.open("images/Basketball_Counter_App.png")
img_project2 = Image.open("images/JumpGame.png")
img_project3 = Image.open("images/PythonPONG.png")
img_Profile = Image.open("images/Profile.jpg")

# --- Side Bar Section ---
with st.sidebar:
        tabs = on_hover_tabs(tabName=['Home', 'Project' ,'About', 'Feedback'], 
                             iconName=['home', 'link', 'info', 'mail'],
                             styles = {'navtab': {'background-color':'#009EFF',
                                                  'color': '#0014FF',
                                                  'font-size': '18px',
                                                  'transition': '1s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'
                                                  },
                                       'tabOptionsStyle': {':hover :hover': {'color': '#F4D160',
                                                                      'cursor': 'pointer'}
                                                          },
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'
                                                   },
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'
                                                    }
                                        },
                             key="1" ,default_choice=0)

# --- Home Section ---
if tabs =='Home':
    with st.container():
        column_left, column_right = st.columns((2,1))
        with column_left:
            st.write("---")
            st.title("Welcome to my Webpage")
            st.subheader("Hi :wave:, I am Richmond E. Hinggo")
            st.write("I am a Computer Engineering students from SNSU")
            st.write("To know my projects visit my github link below.")
            st.write("[Github Link Here](https://github.com/YourEnemy1)")
            st.write("Or hover to the left to see more of my content.")
        with column_right:
            st.write("---")
            st.write("##")
            st.image(img_Profile)

# --- Projects Section ---
elif tabs == 'Project':
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            st.image(img_project1)
        with text_column:
            st.subheader("Basketball Score Counter App")
            st.write(
                """ 
                This is a Basketball Score Counter made in Html, Css and Java Script. 
                """
                """ 
                This web app is not fully finish. 
                """
                """
                This is a sample for fun web app only. 
                """
            )
            st.markdown("[Project Link](https://github.com/YourEnemy1/Basketball-Score-Counter)")

        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            st.image(img_project2)
        with text_column:
            st.subheader("Jump Game in python")
            st.write(
                """ 
                This is a Jump Game made in python. 
                """
                """ 
                This python game is not fully finish. But this game is playable.
                """
                """
                The game can be download in github link below.
                """
            )
            st.markdown("[Project Link](https://github.com/YourEnemy1/Jump-Game)")

        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            st.image(img_project3)
        with text_column:
            st.subheader("PONG in python")
            st.write(
                """ 
                This is a Ping Pong Game made in python. 
                """
                """ 
                This python game is not fully finish. But this game is playable.
                """
                """
                The game can be download in github link below.
                """
            )
            st.markdown("[Project Link](https://github.com/YourEnemy1/Python-PONG)")
        

# --- About Section ---
elif tabs == 'About':
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((2,0.8))
        with left_column:
            st.header("About Me")
            st.write("##")
            st.write("""
                I am a computer engineering student in Surigao del Norte State University.
                - I am currently studying Python, Java, Html and Css.
                - All of my projects is not final and currently ongoing.
                - I'm going to finish this soon.
            """)
            st.write("For the meantime you can watch this youtube video to learn more about how to make a webpage!")
            st.write("[Youtube](https://youtube.com/c/CodingIsFun)")
        with right_column:
            st_lottie(lottie_coding, height=450, key="coding")

# --- Feedback form Section ---
elif tabs == 'Feedback':
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Feedback Message me!")
            st.write("##")
            contact_form = """
            <form action="https://formsubmit.co/comekhazee2017@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
            </form>
            """
        left_column, right_column = st.columns((2,0.5))
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_email, height=250, key="email")
