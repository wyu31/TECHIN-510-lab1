import streamlit as st
st.image('Profile Picture_Square 2.jpg', caption=None, width=200, channels='RGB', output_format='PNG')
st.title('_My name is_ :blue[Wanling Yu] :fish:')
st.header(' :red[Design] :blue[|] :orange[Engineering] :blue[|] :violet[Technology]', divider='rainbow')
st.header('About me :sunglasses:', divider='rainbow')
multi = '''**Design Goal:** Create **Innovative** and **Real-world** products  
**Background:** Academic and Practical experience in **Industiral** and **UX/UI** Design'''
st.markdown(multi)
st.header('Eduaction :mortar_board:', divider='rainbow')
multi = '''**BEng in Product Design and Manufacture** @ University of Nottingham Ningbo China    
**MS in Technology Innovation** @ University of Washington'''
st.markdown(multi)
st.header('Work Experience :female-technologist:', divider='rainbow')
multi = '''**UX / UI Design Intern** @ Femooi  
**Public Education Intern** @ Huamao Museum of Art Education'''
st.markdown(multi)
st.header('Hobbies & Interests :smiling_face_with_3_hearts:', divider='rainbow')
multi = '''Fabricator :hammer_and_wrench:  
Cafe Enthusiast :coffee:  
Music Lover :notes:  
Beginner Baker :cake:  &  Bartender :cocktail:  
'''
st.markdown(multi)
st.header('Interesting Projcts :space_invader:', divider='rainbow')
col1, col2, col3 = st.columns(3)
with col1:
    st.image('P1.jpg', caption=None, width=180, channels='RGB', output_format='PNG')
with col2:
    st.image('P2.jpg', caption=None, width=180, channels='RGB', output_format='PNG')
with col3:
    st.image('P3.jpg', caption=None, width=180, channels='RGB', output_format='PNG')
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("Go to HydroPrompt", "https://bob991105.wixsite.com/techin511-a17-final")
with col2:
    st.link_button("Go to MusicPlayer", "https://www.instagram.com/s/aGlnaGxpZ2h0OjE4MDM4MDc1NjAyNTE4MjIx?story_media_id=3215152829488395702&igsh=NzY1OWxma2d3dnNh")
with col3:
    st.link_button("Go to MeditationHolder", "https://www.instagram.com/p/CzYDBLXOCCc/?igsh=MWtwanZiMXg0b3NsNQ==")
st.header('Contact me :speech_balloon:', divider='rainbow')
multi = '''**Email :e-mail: :** wyu31@uw.edu  
**Phone :telephone_receiver: :** +1 425 647 7164  
**Instagram :eye: :** wanling_yuu'''
st.markdown(multi)