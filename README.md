# AI-UN-SDG5-GenAI-API
AI-UN-SDG5 Generative AI API

This repository provides a FastAPI application to provide an API for the Google Gemini Generative AI processes used for the [AI-UN-SDG5 app](https://github.com/AI-UN-SDG5/AI-UN-SDG5-App), focusing on health-related support for PCOS management.

The app uses Google Gemini to generate insights for medical appointment notes as well as meals and workouts for users who need to manage these factors. Furthermore, the app provides an intelligent chabot that is able to maintain memory of previous messages in the chat history in order to adequately respond to health-related concerns about PCOS.

See the classes Chatbot/Chatbot.py, ContentGenerator/ContentGenerator.py and DbConnection.DbConnection

Before continuing with running this API, it is important to set up the accompanying database for which instructiosn can be found at [this repository](https://github.com/AI-UN-SDG5/AI-UN-SDG5_Data_Preparation). Save the database host, username, password, database name and port to later add as variables in the .env file.

## Instructions to run this API
## Instructions on how to run this application
1. Ensure that [git](https://git-scm.com/downloads) is installed on your device.
2. Ensure that [python 3](https://www.python.org/downloads/) is installed on your device.
3. Clone this repository at a safe path on your device with the command ```git clone https://github.com/AI-UN-SDG5/AI-UN-SDG5-GenAI-API```
4. Enter the repository with the command ```cd AI-UN-SDG5/AI-UN-SDG5-GenAI-API```
5. Create a virtual environment with the command ```python3 -m venv .venv```
6. Activate the virtual environment with the commmand  ```source .venv/bin/activate```
7. Install the dependencies with the command ```pip3 install -r requirements.txt```
8. Create a [Google Cloud platform or GCP](https://cloud.google.com/) project.
9. For this project, add a service account with "Owner" rights and create a json service account credentials file for this service account.
10. Encode this variable as a base64 string and save for later.
11. Create a Gemini API key for this GCP project and save for later.
12. Create a GCP Cloud storage bucket to store generated images and save the name of this bucket for later.
13. Create a .env file and add the respective variables which can be seen in the .env.example file:
    - GEMINI_API_KEY=
    - GCP_IMAGE_BUCKET
    - GCP_SA_KEY_STRING=
    - GOOGLE_PROJECT_ID=
    - GOOGLE_PROJECT_NAME=
    - DB_HOST=
    - DB_USER=
    - DB_PASSWORD=
    - DB_PORT=
    - DB_NAME=
14. Run the FastAPI app with the following command: ```uvicorn app.main:app --reload --host 0.0.0.0 --port 8000```
15. The app should now be running 