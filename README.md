# Music Recommendations Bot

Allows users to input an artist's name and then recieve 20 recommendations based on user input utilizing the spoitfy for developers web API.

## Instructions
1. Clone the repository: "git clone https://github.com/Tyler-Arciniaga/Music-Recommendation-Bot"
2. Create and activate a virtual environment:
3.     "python -m venv venv"
        "venv\Scripts\activate" (WINDOWS)
        "source venv/bin/activate" (MAC)
4. Install required dependencies: "pip install -r requirements.txt"
5. Go to [Spotify Developer Dashboard](https://developer.spotify.com/)
6. Log in with Spotify account or create a new account
7. Click on "Create an App"
8. Fill in required information for app (in this case only the WEB API will be used)
9. Once your app is created you will see your Client ID and Client Secret in app settings:
10. After obtaining client credentials create a .env file in root of project directory and follow format:
    ```python
    client_id = your_client_id_here
    client_secret = your_client_secret_here
11. Run Flask development server: "python3 main.py"
12. Web application will be available at "https://localhost:8000"
 
# Example Photos:

# Kendrick Lamar
<img width="1469" alt="Screen Shot 2024-10-11 at 10 28 50 PM" src="https://github.com/user-attachments/assets/29424232-c2bd-40c4-91d2-3d527bc0178e">

<img width="1468" alt="Screen Shot 2024-10-08 at 10 48 08 AM" src="https://github.com/user-attachments/assets/b5a71033-323d-43b8-ac77-37d9e096c4f7">

# Michael Jackson
<img width="1470" alt="Screen Shot 2024-10-11 at 10 29 01 PM" src="https://github.com/user-attachments/assets/0f79fab2-fdc0-47db-8b80-a0fa71e41646">

<img width="1470" alt="Screen Shot 2024-10-08 at 10 49 48 AM" src="https://github.com/user-attachments/assets/c2c40e9e-12d3-4e75-9b0a-30a9c3c341f4">

