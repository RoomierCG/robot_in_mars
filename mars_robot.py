# Edgar Calle test
import re
import numpy

# Defining main function
def main():
    robot_controls()

def generate_terrain():
    REGEX=re.compile('^[0-9]*(x)[0-9]*$', re.IGNORECASE)

    user_input = input("Define the terrain:")

    if REGEX.match(user_input):
        arr = user_input.split('x')
        return arr

    return None

"""
    Controls
    L: Turn the robot left
    R: Turn the robot right
    F: Move forward on it's facing direction
"""
def ask_control():
    REGEX=re.compile('L|R|F', re.IGNORECASE)

    user_input = input("")
    user_input = user_input.upper()

    if REGEX.match(user_input):
        return user_input

    return None


def robot_controls():
    map = generate_terrain()

    arr_coordinate = ["north", "east", "south", "west"]
    coordinate = 0 # 0 north 1 east 2 south  3 west
    coordinateX = 1
    coordinateY = 1

    command = ask_control()

    for position in command:

        #robot orientation
        if position == 'L':
            coordinate -= 1

            if coordinate < 0:
                coordinate = 3

        elif position == 'R':
            coordinate += 1

            if coordinate > 3:
                coordinate = 0

        #robot movement
        elif position == 'F':

            # north 
            if coordinate == 0:
                coordinateY += 1

                if coordinateY > int(map[0]):
                    coordinateY = int(map[0])
            # east
            elif coordinate == 1:
                coordinateX += 1

                if coordinateX > int(map[1]):
                    coordinateX = int(map[1])
            # south 
            elif coordinate == 2:
                coordinateY -= 1
                
                if coordinateY < 1:
                    coordinateY = 1
            # west
            elif coordinate == 3:
                coordinateX -= 1

                if coordinateX < 1:
                    coordinateX = 1
    
    print(coordinateX, coordinateY, arr_coordinate[coordinate])        
    
    return numpy.zeros((coordinateX, coordinateY))

if __name__=="__main__":
    main()