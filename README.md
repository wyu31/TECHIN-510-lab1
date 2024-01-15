# TECHIN 510 lab1_Wanling
This is a personal website of Wanling Yu for TECHIN 510 Lab 1.

It mentions the info below:  
1. A Profile Picture
2. About Me
3. Education Info
4. Work Experience
5. Hobbies and Interests
6. Interesting Projects
7. Contact Info


## How to Run
Open the terminal and run the following commands:

1. Create an environment using
```bash
# Open a terminal and navigate to my project folder.
cd myproject

# Set up a folder named '.venv' in the project, where the virtual environment and its dependencies are installed.  
python -m venv venv
```


2. Activate the environment
```bash
# Activate the environment with one of the following commands, depending on your operating system.

# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```


3. Install Streamlit in your environment
```bash
# In the terminal with your environment activated, type:
pip install -r requirements.txt
```


4. Run it
```bash
# Run the Streamlit app:
streamlit run app.py
# If this doesn't work, use the long-form command:
python -m streamlit run app.py
```


5. Close it
```bash
# To stop the Streamlit server, press Ctrl+C in the terminal.
# When you're done using this environment, return to your normal shell by typing:
deactivate
```


## What's Included
This is the main running application.
```bash
app.py
```


This document tells Git which files or directories to ignore in a project.
```bash
.gitignore
```

This file stores workflow configuration files of adding or updating the Azure App Service build and deployment workflow.
```bash
.github/workflows
```

This directory is where the virtual environment and its dependencies are installed.  
```bash
.venv
```

This file is used to list all the dependencies that the project needs to run correctly. More specifically, it includes the name of streamlit for installation with the terminal in this project.
```bash
.requreiments.txt
```

This file includes the text info of the basic introduction of this GitHub Repository, how to run, what's included, lessons learned, questions / uncertainties
```bash
README.md
```

These are the images used in the website.
```bash
Profile Picture_Square 2
P1.jpg
P2.jpg
P3.jpg
```


## Lessons Learned

### What should the .gitignore includes:

```bash
.venv
*.pyc
.DS_Store
```

### What is the Basic Terminal Command Sequence for Git Uploading:

```bash
git status  
git add .  
git status  
git commit -m "comments of the upadates"
git log
git pull origin main
git push origin main
```
### How to use Streamlit to create a simple website:
This includes using the terminal to create a virtual environment, multi-platform collaboration, visualizing images and text by coding, etc.

### How to use requirements.txt to manage Python dependencies:
This includes listing all dependencies in the 'requirements.txt' file, installing them by run 'pip install -r requirements.txt' in the terminal, and regular updating the file to maintain.

### How to use GitHub Actions to deploy a website to Azure App Service:
This includes creating a new resource group in region, creating a new App service, connecting to my GitHub account and repository, configuration and startup.

## Questions / Uncertainties
### How to improve image quality in streamlit?
Interpretation:  
In streamlit, I would limit the value of the image width when I didn't want the image size to be as large as the original one.  
However, I found that once I reduced the size of the image, the quality (resolution) of the image also dropped significantly.   
Hence, I'd like to know how I can reduce the size while maintaining the quality of the image.

### How do I adjust the line spacing?
Interpretation:  
I often felt that the default line spacing is too large or too small, and I would like to know if there is any opportunity to adjust it myself.

### How do I change the font?
Interpretation:  
It looks like there is only one default font in streamlit website writing, I'm wondering if it is possible to upload a local font to use.