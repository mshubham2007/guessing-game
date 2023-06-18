# Guessing Game

This is a simple number guessing game built with Python and Flask.

## How to Run the Game

1. Ensure you have Python 3.x installed on your machine.

2. Clone this repository:

git clone https://github.com/mshubham2007guessing-game.git


3. Navigate to the project directory:

cd guessing-game


4. Install the required dependencies:

pip install -r requirements.txt


5. Run the game:

python app.py

6. Open your web browser and access the game at `http://localhost:5000`.

7. Guess the number and enjoy playing the game!

## How to Create a Docker Image

1. Install Docker on your machine following the official Docker documentation for your operating system.

2. Clone this repository and navigate to the project directory as described in the previous section.

3. Build the Docker image:

docker build -t guessing-game .

4. Run the Docker container:

docker run -d -p 5000:5000 guessing-game

5. Open your web browser and access the game at `http://localhost:5000`.

6. Guess the number and enjoy playing the game!

## License

This project is licensed under the [MIT License](LICENSE).