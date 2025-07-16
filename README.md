# Positive Meme Generator

This is a simple web application that generates a positive meme to brighten your day. You can tell the app how your day is going, and it will respond with a fun GIF and a cheerful message.

## How it Works

The application is built with Python and Flask. Here's a quick overview of the process:

1.  **User Input**: The main page asks you to describe your day in one word.
2.  **Meme Generation**: When you submit your response, the app:
    *   Fetches a random "positive vibes" GIF from the Tenor API.
    *   Generates a custom message based on whether your input was a positive, negative, or neutral word.
3.  **Display**: The app then displays the GIF and the message on a new page.

## Features

*   **Dynamic Meme Generation**: Get a different meme every time.
*   **Personalized Messages**: The message you receive is tailored to your input.
*   **Simple and Fun**: A quick and easy way to get a little dose of positivity.

## How to Run Locally

To run this application on your local machine, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/romarvz/Positive_Meme_Generator.git
    cd Positive_Meme_Generator
    ```

2.  **Install the dependencies**:
    ```bash
    pip install Flask requests python-dotenv
    ```

3.  **Set up your API key**:
    - Copy `.env.example` to `.env`
    - Get a free API key from [Tenor API](https://developers.google.com/tenor/guides/quickstart)
    - Replace `your_tenor_api_key_here` in `.env` with your actual API key

4.  **Run the application**:
    ```bash
    python app.py
    ```

5.  **Open your browser**:
    Navigate to `http://127.0.0.1:5000/` to use the app.

## Technologies Used

*   **Python**: The core programming language.
*   **Flask**: A lightweight web framework for Python.
*   **Tenor API**: Used to fetch random GIFs.
*   **HTML/CSS**: For the front-end structure and styling.
