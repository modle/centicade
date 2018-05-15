#!/usr/local/bin/python3.6

import random
import arcade
import timeit
import os

NATIVE_SPRITE_SIZE = 128
SPRITE_SCALING = 0.25
SPRITE_SIZE = int(NATIVE_SPRITE_SIZE * SPRITE_SCALING)

NUM_COLUMNS = 20
NUM_ROWS = 20
NUM_MUSHROOMS = 50

SCREEN_WIDTH = SPRITE_SIZE * NUM_COLUMNS
SCREEN_HEIGHT = SPRITE_SIZE * NUM_ROWS



MOVEMENT_SPEED = 8

TILE_EMPTY = 0
TILE_CRATE = 1
MAZE_WIDTH = 20
MAZE_HEIGHT = 20

def create_empty_grid(width, height, default_value=TILE_EMPTY):
    """ Create an empty grid. """
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            grid[row].append(default_value)
    return grid

def get_mushroom_coordinates(coordinates):
    x = random.randrange(0, SCREEN_WIDTH)
    y = random.randrange(80, SCREEN_HEIGHT - 80)

    coordinates.append((x, y))

    if len(coordinates) < NUM_MUSHROOMS:
        get_mushroom_coordinates(coordinates)

    return coordinates

# def make_mushroom_field():
#     mushroom_coordinates = []
#     mushroom_coordinates = get_mushroom_coordinates(mushroom_coordinates)
#     mushroom_field = create_empty_grid(SCREEN_WIDTH, SCREEN_HEIGHT)

#     for coordinate in mushroom_coordinates:
#         mushroom_field[coordinate[0]][coordinate[1]] = TILE_CRATE

#     return mushroom_field

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        """
        Initializer
        """
        super().__init__(width, height)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None
        self.mushroom_list = None

        # Used to scroll
        self.view_bottom = 0
        self.view_left = 0

        # Time to process
        self.processing_time = 0
        self.draw_time = 0


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.mushroom_list = arcade.SpriteList()

        mushroom_field_coordinates = []
        mushroom_field_coordinates = get_mushroom_coordinates(mushroom_field_coordinates)
        # mushroom_field = make_mushroom_field_recursion(MAZE_WIDTH, MAZE_HEIGHT)

        # print (mushroom_field_coordinates)

        for coordinate in mushroom_field_coordinates:

            mushroom = arcade.Sprite("images/mushroom-4.png", SPRITE_SCALING,
                                  repeat_count_x=1)
            mushroom.center_x = coordinate[0] # * SPRITE_SIZE + SPRITE_SIZE / 2
            mushroom.center_y = coordinate[1] # * SPRITE_SIZE + SPRITE_SIZE / 2
            mushroom.width = SPRITE_SIZE
            print(mushroom.center_x)

            self.mushroom_list.append(mushroom)

        print(self.mushroom_list)

        # for row in range(NUM_ROWS):
        #     column = 0

        #     while column < len(mushroom_field):
        #         while column < len(mushroom_field) and mushroom_field[row][column] == 0:
        #             column += 1
        #         start_column = column
        #         while column < len(mushroom_field) and mushroom_field[row][column] == 1:
        #             column += 1
        #         end_column = column - 1

        #         column_count = end_column - start_column + 1
        #         column_mid = (start_column + end_column) / 2

        #         wall = arcade.Sprite("images/grassCenter.png", SPRITE_SCALING,
        #                               repeat_count_x=column_count)
        #         wall.center_x = column_mid * SPRITE_SIZE + SPRITE_SIZE / 2
        #         wall.center_y = row * SPRITE_SIZE + SPRITE_SIZE / 2
        #         wall.width = SPRITE_SIZE * column_count
        #         self.wall_list.append(wall)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        # Draw all the sprites.
        self.mushroom_list.draw()
        # self.player_list.draw()

        # Draw info on the screen
        sprite_count = len(self.mushroom_list)

        output = f"Sprite Count: {sprite_count}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 20 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 40 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 60 + self.view_bottom,
                         arcade.color.WHITE, 16)

        self.draw_time = timeit.default_timer() - draw_start_time


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        pass

        # if key == arcade.key.UP:
        #     self.player_sprite.change_y = MOVEMENT_SPEED
        # elif key == arcade.key.DOWN:
        #     self.player_sprite.change_y = -MOVEMENT_SPEED
        # elif key == arcade.key.LEFT:
        #     self.player_sprite.change_x = -MOVEMENT_SPEED
        # elif key == arcade.key.RIGHT:
        #     self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass
        # if key == arcade.key.UP or key == arcade.key.DOWN:
        #     self.player_sprite.change_y = 0
        # elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
        #     self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """
        pass
        # print('update things')

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
