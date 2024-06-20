# Machine Learning-Based Intellectual Game

## Project Description

This project is a desktop application — an intellectual game where the user must guess the word chosen by the game. The game uses machine learning algorithms to provide hints and evaluate the similarity of the input words.

## Screenshots

### Main Screen
![Main Screen](https://github.com/maratshchur/CourseWork/blob/MyMain/Screenshots/photo_2023-10-30_17-20-32.jpg)

### Authorization Screen
![Authorization Screen](https://github.com/maratshchur/CourseWork/blob/MyMain/Screenshots/photo_2024-06-20_18-29-29.jpg)

### Tournament Creation Screen
![Tournament Creation Screen](https://github.com/maratshchur/CourseWork/blob/MyMain/Screenshots/photo_2024-06-20_18-29-39.jpg)

### Tournament Screen
![Tournament Screen](https://github.com/maratshchur/CourseWork/blob/MyMain/Screenshots/photo_2024-06-20_18-29-42.jpg)

## Features

### For Administrator

- **Word Creation**: The administrator can set a new word to be guessed.
- **Tournament Creation**: The administrator can create a new tournament.

### For User

- **Registration**: Users can register by entering their email and password.
- **Authorization**: Users can log in by entering their username and password.
- **Word Guessing**: Users input a word and receive an evaluation of its similarity to the target word.
- **Hint**: Users can receive a hint — a word closer in meaning to the target word.
- **Profile View**: Users can view their name, number of wins, and rating.
- **Top Players View**: A list of top players ranked by rating.
- **Messages View**: Users can see messages about tournament results.
- **Available Tournaments View**: A list of available tournaments for participation.
- **Tournament Details View**: Basic details of the selected tournament (name, description, duration, start date, number of rounds).
- **Tournament Participation**: The ability to participate in a tournament.

## Installation and Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/maratshchur/LogicOn.git
    ```

2. Navigate to the server directory:
    ```sh
    cd server
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Start the server:
    ```sh
    python manage.py runserver
    ```

5. To start the game, run the `start_page` file from the `Application` folder in the root directory of the project:
    ```sh
    python Application/start_page.py
    ```

## Technologies Used

- **Programming Language**: Python
- **GUI Library**: PyQt6
- **Database**: SQLite

## Contribution

We welcome contributions to the project! Please create a Pull Request or open an Issue for discussion.

## Contact

If you have any questions or suggestions, please contact us at [marat.shchur@gmail.com](mailto:marat.shchur@gmail.com).
