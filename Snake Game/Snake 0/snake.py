from random import randint

# Creating graphical user interfaces with Python
import tkinter as tk

# Pillow is a library that allows the game to load images and display them
from PIL import Image, ImageTk

# Uppercase == constant
MOVE_INCREMENT = 20
moves_per_second = 15
GAME_SPEED = 1000 // moves_per_second

# Creating the class Snake as a Canvas
class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width = 600, height = 620, background = "black", highlightthickness = 0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]

        self.food_position = self.set_new_food_position()

        self.score = 0

        self.direction = "Right"
        self.bind_all("<Key>", self.on_key_press)

        # Load the image of the snake and food into the game
        self.load_assets() 

        self.create_objects()

        self.after(GAME_SPEED, self.perform_actions)

    def load_assets(self):
        try:
            self.snake_body_image = Image.open("./assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("./assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)
        except IOError as error:
            print(error)
            root.destroy()

    def create_objects(self):
        self.create_text(
            100, 12, text = f"Score: {self.score} (speed: {moves_per_second})", tag = "score", fill = "#fff", font = ("TKDefaultFont", 14)
        )

        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position, image = self.snake_body, tag = "snake")

        self.create_image(*self.food_position, image = self.food, tag = "food")

        self. create_rectangle(7, 27, 593, 613, outline = "grey")

    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions[0]
        
        if self.direction == "Left":
            new_head_position = (head_x_position - MOVE_INCREMENT, head_y_position)
        elif self.direction == "Right":
            new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)
        elif self.direction == "Down":
            new_head_position = (head_x_position, head_y_position + MOVE_INCREMENT)
        elif self.direction == "Up":
            new_head_position = (head_x_position, head_y_position - MOVE_INCREMENT)  

        # Take the 1st element of the head and cut off the last element
        self.snake_positions = [new_head_position] + self.snake_positions[:-1] 

        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)

    def perform_actions(self):
        if self.check_collisions():
            self.end_game()
            return

        self.check_food_collision()

        self.move_snake()
         # Call the function after 75 ms
        self.after(GAME_SPEED, self.perform_actions)

    def check_collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]

        return (
                # If the snake moves out of the x-axis
            head_x_position in (0, 600)
                # If the snake moves out of the y-axis
            or head_y_position in (20, 620)
                # Whether the snake bites itself
            or (head_x_position, head_y_position) in self.snake_positions[1:]
        )

    def on_key_press(self, e):
        new_direction = e.keysym

        all_directions = ("Up", "Down", "Left", "Right")
        opposites = ({"Up", "Down"}, {"Left", "Right"})

        if (
            new_direction in all_directions
            and {new_direction, self.direction} not in opposites
        ):
            self.direction = new_direction

    def check_food_collision(self):
        if self.snake_positions[0] == self.food_position:
            self.score += 1
            self.snake_positions.append(self.snake_positions[-1])

            if self.score % 5 == 0:
                global moves_per_second
                moves_per_second += 1

            self.create_image(
                *self.snake_positions[-1], image = self.snake_body, tag = "snake"
            )

            self.food_position = self.set_new_food_position()
            self.coords(self.find_withtag("food"), self.food_position)

            score =  self.find_withtag("score")
            self.itemconfigure(
                score,
                text = f"Score : {self.score} (speed: {moves_per_second})",
                tag = "score"
                )

    def set_new_food_position(self):
        while True:
            x_position = randint(1, 29) * MOVE_INCREMENT
            y_position = randint(3,30) * MOVE_INCREMENT
            
            food_position = (x_position, y_position)

            if food_position not in self.snake_positions:
                return food_position

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text = f"Game Over! You scored {self.score}!",
            fill = "#fff",
            font = ("TkDefaultFont", 24)
        )

# Creating the application window
root = tk.Tk()
# Setting name for the app window
root.title("Snake Game") 
# Setting the app window unresizable                    
root.resizable(False, False)            

board = Snake()
board.pack()

# Start the app window
root.mainloop()                         