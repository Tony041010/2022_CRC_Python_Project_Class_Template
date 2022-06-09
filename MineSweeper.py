import random
import re
import time

# Board object to represent the minesweeper game
class Board:
    def __init__(self, dim_size, num_bombs):
        # keep track of these parameters
        

        # create the board using helper function

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row, col) tuples into this set
        # if we dig at 0, 0, then self.dug = {(0,0)}
        pass

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # using a two-dimentions list (lists in lists)

        # generate a new board
        
        # like this :
        # [[None, None,......, None],
        # [None, None,......, None],
        # [None, None,......, None],
        # [None, None,......, None]]

        # plant the bombs
        
                # this means we've actually planted a bomb there already
        pass


    def assign_values_to_board(self):
        # assign a number 0-8 for all the empty spaces, which represents how many neighboring bombs there are.
        # We can precompute these and it'll save us some effort checking what's around the board later on
        pass
    
    def get_num_neighboring_bombs(self, row, col):
        # iterate through eac of the neighboring positions and sum number of bombs
        # top left : (row-1, col-1)
        # top middle : (row-1, col)
        # top right : (row-1, col+1)
        # left : (row, col-1)
        # middle : (row, col)
        # right : (row, col+1)
        # bottom left : (row+1, col-1)
        # bottom middle : (row+1, col)
        # bottom right : (row+1, col+1)

        # make sure to not go out of bounds!

        pass

    def dig(self, row, col):
        # dig at the certain location
        # return True if  it's a successful dig, False if a bomb has been dug

        # a few scenarios:
        # it a bomb -> game over
        # dig at location with neighborin bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors

         # keep track of where we've dug


                     # don't dig where you've already dug
        pass

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this functions returns
        # we'remusing it to return a string that shows the board to the player

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep



# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1 : Create the board and plant the bombs
    

    # Step 2 : Show the user the board and ask for where they want to dig
    # Step 3(a) : If the location is a bomb, show "game over" message
    # Step 3(b) : If the location is not a bomb, dig recursively until each square is at least next to the bomb
    # Step 4 : Repeat steps 2 and 3(a)/(b) until there are no more places to dig -> VICTORY!


    
    # 2 ways to end loop, lets check which one
    pass        



if __name__ == '__main__': # even the content of it is only one line code, it's still a good practice
    play()