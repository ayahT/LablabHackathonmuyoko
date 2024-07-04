# -*- coding: utf-8 -*-
"""muyoko.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ngx_yWCJGvcJOOIYavBzdSOsr92jKkz5
"""

#It's okay to feel sad or frustrated sometimes, but try to stay positive and look for the good in every situation.

"""# The Model Section

"""

#animation part imports
!nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader

!pip install TTS PyPDF2 torch

!pip install --upgrade --force-reinstall transformers

# Commented out IPython magic to ensure Python compatibility.
#import dependancy of animation
!update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.8 2
!update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.9 1
!sudo apt install python3.8

!sudo apt-get install python3.8-distutils

!python --version

!apt-get update

!apt install software-properties-common

!sudo dpkg --remove --force-remove-reinstreq python3-pip python3-setuptools python3-wheel

!apt-get install python3-pip

print('Git clone project and install requirements...')
!git clone https://github.com/Winfredy/SadTalker &> /dev/null
# %cd SadTalker
!export PYTHONPATH=/content/SadTalker:$PYTHONPATH
!python3.8 -m pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
!apt update
!apt install ffmpeg &> /dev/null
!python3.8 -m pip install -r requirements.txt

print('Download pre-trained models...')
!rm -rf checkpoints
!bash scripts/download_models.sh

!pip install --upgrade transformers # Upgrade transformers to work with the newer NumPy version

from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

"""# The Application Section"""

!pip install streamlit pyngrok

YOUR_AUTHTOKEN = "2iiKc5kgOze2rJctjTcj4rk8OO7_2cU2zPsZSpdsq9oRYSgvW"
!ngrok config add-authtoken $YOUR_AUTHTOKEN

# Commented out IPython magic to ensure Python compatibility.
# %%writefile animation.py
# import streamlit as st
# import matplotlib.pyplot as plt
# import os
# import subprocess
# from base64 import b64encode
# from io import BytesIO
# from PIL import Image
# 
# @st.cache_data
# def load_model():
#     # Dummy function to demonstrate caching
#     return "Loaded model"
# 
# def animation():
#     st.title("Convey a message to your child through animation.")
#     st.header("Upload Files")
#     st.write("First, upload an image and an audio file to generate the animation.")
# 
#     uploaded_image = st.file_uploader("Upload Image (PNG):", type=["png"], key="image_uploader")
#     uploaded_audio = st.file_uploader("Upload Audio (WAV):", type=["wav"], key="audio_uploader")
# 
#     def save_file(uploaded, path):
#         with open(path, 'wb') as f:
#             f.write(uploaded.getbuffer())
# 
#     def run_inference():
#         dmm_progress = st.progress(0)
#         mel_progress = st.progress(0)
#         audio2exp_progress = st.progress(0)
#         face_renderer_progress = st.progress(0)
# 
#         try:
#             result = subprocess.run(
#                 ['python3.8', 'inference.py',
#                  '--driven_audio', 'uploaded_audio.wav',
#                  '--source_image', 'uploaded_image.png',
#                  '--result_dir', './results',
#                  '--still', '--preprocess', 'full', '--enhancer', 'gfpgan'],
#                 capture_output=True, text=True, check=True,
#                 cwd=os.path.dirname(os.path.realpath(__file__)))
#             st.success("Inference script ran successfully!")
#             st.text(result.stdout)
# 
#             dmm_progress.progress(100)
#             mel_progress.progress(100)
#             audio2exp_progress.progress(100)
#             face_renderer_progress.progress(100)
#         except subprocess.CalledProcessError as e:
#             st.error("Inference script failed!")
#             st.text(e.output)
# 
#     if uploaded_image and uploaded_audio:
#         with st.spinner("Processing..."):
#             image_bytes = uploaded_image.read()
#             audio_bytes = uploaded_audio.read()
# 
#             # Save files in memory
#             with open('uploaded_image.png', 'wb') as f:
#                 f.write(image_bytes)
#             with open('uploaded_audio.wav', 'wb') as f:
#                 f.write(audio_bytes)
# 
#             st.header("Uploaded Image")
#             image = Image.open(BytesIO(image_bytes))
#             st.image(image, caption="Uploaded Image", use_column_width=True)
# 
#             run_inference()
# 
#             st.header("Generated Animation")
#             results = sorted(os.listdir('./results'))
#             if results and results[-1].endswith('.mp4'):
#                 mp4_name = os.path.join('./results', results[-1])
#                 with open(mp4_name, 'rb') as f:
#                     mp4 = f.read()
#                     data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
#                     st.markdown(f"""
#                         <div style="display: flex; justify-content: center;">
#                             <video width=1024 controls style="border-radius: 15px;">
#                                 <source src="{data_url}" type="video/mp4">
#                             </video>
#                         </div>
#                         """, unsafe_allow_html=True)
#             else:
#                 st.error("No mp4 files found in ./results/. Please check if the inference script ran successfully.")
#     else:
#         st.write("Please upload both an image and an audio file to generate the animation.")
#

# Commented out IPython magic to ensure Python compatibility.
# %%writefile voice.py
# import streamlit as st
# from TTS.api import TTS
# # Page 1: voice page
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
# 
# def voice():
#     st.title("Express what you want to say to your child, and it will be converted to a voice message.")
# 
#     # Upload speaker WAV file
#     speaker_wav = st.file_uploader("Upload Speaker WAV File", type=["wav"])
# 
#     # Input text to be converted to speech
#     text_input = st.text_area("Enter Text")
# 
#     if st.button("Generate Speech"):
#         if speaker_wav and text_input:
#             # Save uploaded WAV file to a temporary file
#             with open("speaker.wav", "wb") as f:
#                 f.write(speaker_wav.getbuffer())
# 
#             # Generate speech and save to output.wav
#             tts.tts_to_file(text=text_input, file_path="output.wav", speaker_wav="speaker.wav", language="en")
# 
#             # Display audio player for the generated speech
#             st.audio("output.wav")
#         else:
#             st.error("Please upload a speaker WAV file and enter text to generate speech.")
# 
#

# Commented out IPython magic to ensure Python compatibility.
# %%writefile story.py
# import streamlit as st
# import PyPDF2
# from transformers import pipeline
# from TTS.api import TTS
# 
# def extract_text_from_pdf(pdf_file):
#     reader = PyPDF2.PdfReader(pdf_file)
#     text = ''
#     for page_num in range(len(reader.pages)):
#         page = reader.pages[page_num]
#         text += page.extract_text()
#     return text
# 
# def story():
#     # Initialize the summarization pipeline
#     summarizer = pipeline("summarization", model="Falconsai/text_summarization")
# 
#     # Streamlit app
#     st.title("Share a brief story with your child using your own voice.")
# 
#     # File uploader for PDF
#     uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
# 
#     # File uploader for speaker audio
#     uploaded_audio = st.file_uploader("Upload a speaker audio file (WAV)", type="wav")
# 
#     if uploaded_file is not None and uploaded_audio is not None:
#         try:
#             # Extract text from the uploaded PDF
#             pdf_text = extract_text_from_pdf(uploaded_file)
# 
#             # Check if the extracted text is not empty
#             if not pdf_text.strip():
#                 st.error("The uploaded PDF file is empty or could not be read.")
#                 return
# 
# 
#             summary_results = summarizer(pdf_text, max_length=100, min_length=50, do_sample=False)
# 
#             # Check if summarizer returned results
#             if not summary_results:
#                 st.error("Summarization failed. No summary was returned.")
#                 return
# 
#             summary = summary_results[0].get('summary_text', '')
# 
#             # Check if summary is not empty
#             if not summary:
#                 st.error("Summarization failed. The summary is empty.")
#                 return
# 
#             # Display the summary in a text box
#             st.text_area("Generated Summary:", summary, height=300)
# 
#             # Save the uploaded speaker audio file
#             with open("speaker.wav", "wb") as f:
#                 f.write(uploaded_audio.getbuffer())
# 
#             # Initialize the TTS model
#             tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
# 
#             # Generate speech from the summarized text using the uploaded speaker audio
#             tts.tts_to_file(text=summary, file_path="output.wav", speaker_wav="speaker.wav", language="en")
# 
#             # Display audio player for the generated speech
#             st.audio("output.wav")
#         except Exception as e:
#             st.error(f"An error occurred: {e}")
#             st.error("Details: " + str(e))  # Additional error details
#     else:
#         st.write("Please upload both a PDF file and a speaker audio file.")
# 
#

# Commented out IPython magic to ensure Python compatibility.
# %%writefile song.py
# import streamlit as st
# 
# # Page 4: song page
# def song():
#     st.title("Sing a song to your child or choose their favorite song.")
# 
#     st.write("Select a voice and then a song:")
# 
#     voices = ["Anya", "Scootallo", "Sweetiebelle"]
# 
#     voice_to_songs = {
#         "Anya": {
#             "Twinkle, Twinkle, Little Star": "/content/twinkleanya.wav",
#             "Baby Shark": "/content/sharkanya.wav"
#         },
#         "Scootallo": {
#             "Twinkle, Twinkle, Little Star": "/content/twinklescootalloo.wav",
#             "Baby Shark": "/content/sharkscootallo.wav"
#         },
#         "Sweetiebelle": {
#             "Twinkle, Twinkle, Little Star": "/content/twinklesweetiebelle.wav",
#             "Baby Shark": "/content/shark1sweetiebelle.wav"
#         }
#     }
# 
#     selected_voice = st.selectbox("Select Voice", voices)
# 
#     if selected_voice:
#         available_songs = voice_to_songs[selected_voice]
#         selected_song_name = st.selectbox("Select Song", list(available_songs.keys()))
# 
#         if selected_song_name:
#             selected_song_path = available_songs[selected_song_name]
#             st.audio(selected_song_path)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# 
# import streamlit as st
# from animation import animation
# from story import story
# from voice import voice
# from song import song
# # Navigation
# 
# pages = {
#         "Animation": animation,
#         "Story": story,
#         "voice":voice,
#         "song":song
#     }
# 
# st.sidebar.title("Navigation")
# page = st.sidebar.selectbox("Go to", list(pages.keys()))
# 
#     # Execute the selected function
# pages[page]()
#

# Step 3: Run the Streamlit App in Colab
import os
from pyngrok import ngrok

# Kill any existing ngrok tunnels
ngrok.kill()

# Verify if any ngrok processes are still running (optional)
!ps aux | grep ngrok  # Check if any ngrok processes are running

# Setup a new ngrok tunnel
# Remove the 'region' parameter as it's not applicable for 'http' tunnels
# The 'ngrok.connect' function automatically authenticates using your configured authtoken.
tunnel = ngrok.connect(8501, proto="http", bind_tls=True,)
public_url = tunnel.public_url
print(f"Streamlit App URL: {public_url}")

# Run the Streamlit app
# Make sure 'your_app.py' is the correct filename and in the current directory
!streamlit run app.py

pdf_text = "Your long text from the PDF goes here..."
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

summary = summarizer(pdf_text, max_length=300, min_length=100, do_sample=False)[0]['summary_text']
print(summary)
