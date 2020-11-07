### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
def calculateArea(plot_width, plot_length):
	Area= plot_width * plot_length
	return Area


#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_width, plot_length, tile_width, tile_length):
    if tile_width < 0 or tile_length < 0 :
        return False
    
    if calculateArea(plot_width, plot_length) % (tile_width * tile_length) == 0 :
        return True
        if (tile_width * tile_length) > 0 :
            return True
            if (plot_width * plot_length) // (tile_width * tile_length) == True :
                return True
            else:
                return False
        else:
            return False
    else : 
        return False
#### End OF MARKER



### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###
def calculateTiles(plot_width, plot_length, tile_width, tile_length):
    if type(plot_width) == str :
        return "Invalid Input"
    elif type(plot_length) == str :
        return "Invalid Input"
    elif type(tile_width) == str :
        return "Invalid Input"
    elif type(tile_length) == str :
        return "Invalid Input" 
    
    if (plot_width) == 0 :
        return None
    elif (plot_length) == 0 :
        return None
    elif (tile_width) == 0 :
        return None
    elif (tile_length) == 0 :
        return None
    number_of_tiles = (plot_width * plot_length) // (tile_width * tile_length)
    if checkTilesFit(plot_width, plot_length, tile_width, tile_length) == True :
        return number_of_tiles
    else :
        return"Not Possible"
#### End OF MARKER
