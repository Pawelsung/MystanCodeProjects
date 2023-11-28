"""
File: babygraphics.py
Name: Paul
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    space = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    return GRAPH_MARGIN_SIZE + space * year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw top horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE)

    # Draw bottom horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # Draw vertical lines for each year
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # Calculate the y-coordinate spacing
    space_y = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK

    for i in range(len(lookup_names)):  # Loop through each name
        name = lookup_names[i]
        if name in name_data:  # Check if name is in the data
            color = COLORS[i % len(COLORS)]
            for j in range(len(YEARS)):   # Loop through each year
                x = get_x_coordinate(CANVAS_WIDTH, j)  # Get x-coordinate for the year
                year = str(YEARS[j])
                if year in name_data[name]:  # Check if name has a rank for the year
                    rank = int(name_data[name][year])
                    y = GRAPH_MARGIN_SIZE + space_y * rank  # Calculate y-coordinate based on rank
                    # Draw text for name and rank
                    canvas.create_text(x+TEXT_DX, y, text=f'{name} {rank}', fill=color, anchor=tkinter.SW)
                else:  # If name does not have a rank for the year
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE  # Set y-coordinate to bottom margin
                    # Draw text for name
                    canvas.create_text(x, y, text=f'{name} *', fill=color, anchor=tkinter.SW)
                if j > 0:
                    x1 = get_x_coordinate(CANVAS_WIDTH, j - 1)
                    year1 = str(YEARS[j - 1])
                    if year1 in name_data[name]:
                        rank1 = int(name_data[name][year1])
                    else:
                        rank1 = MAX_RANK
                    y1 = GRAPH_MARGIN_SIZE + space_y * rank1

                    # Draw line connecting the points
                    canvas.create_line(x1, y1, x, y, width=LINE_WIDTH, fill=color)

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
