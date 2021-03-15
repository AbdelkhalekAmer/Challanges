class ANSWERS:
    YES = 'YES'
    NO = 'NO'

class DIRECTIONS:
    UP = 'up'
    RIGHT = 'right'
    DOWN = 'down'
    LEFT = 'left'

class Position:
    def __init__(self, x, y) -> None:
        self.X = x
        self.Y = y

class STEPS:
    G = 'G'
    R = 'R'
    L = 'L'

def does_circular_exist_in_commands(commands):
    for command in commands:
        yield does_circular_exist_in_command(command)

def does_circular_exist_in_command(command) -> str:
    current_position = Position(0,0)
    direction = DIRECTIONS.UP
    total_processed_command_iterations = command.count(STEPS.G)
    processed_command_iterations = 0
    
    while(processed_command_iterations < total_processed_command_iterations):
        for step in command:
            if step == STEPS.G: go_toward_direction(direction, current_position)
            if step == STEPS.R: direction = turn_right(direction)
            if step == STEPS.L: direction = turn_left(direction)
            print(f'Command {command}: robot is looking at {direction} in ({current_position.X},{current_position.Y}).')
        processed_command_iterations += 1
    
    if current_position.X == 0 and current_position.Y == 0: return ANSWERS.YES
    else: return ANSWERS.NO
    
def go_toward_direction(direction, position):
    if direction == DIRECTIONS.UP: position.Y += 1
    if direction == DIRECTIONS.RIGHT: position.X += 1
    if direction == DIRECTIONS.DOWN: position.Y -= 1
    if direction == DIRECTIONS.LEFT: position.X -= 1

def turn_right(direction) -> str:
    if direction == DIRECTIONS.UP: return DIRECTIONS.RIGHT
    if direction == DIRECTIONS.RIGHT: return DIRECTIONS.DOWN
    if direction == DIRECTIONS.DOWN: return DIRECTIONS.LEFT
    if direction == DIRECTIONS.LEFT: return DIRECTIONS.UP

def turn_left(direction) -> str:
    if direction == DIRECTIONS.UP: return DIRECTIONS.LEFT
    if direction == DIRECTIONS.RIGHT: return DIRECTIONS.UP
    if direction == DIRECTIONS.DOWN: return DIRECTIONS.RIGHT
    if direction == DIRECTIONS.LEFT: return DIRECTIONS.DOWN

def main():
    commands = ["G","R","L","GGGGR"]
    results = list(does_circular_exist_in_commands(commands))
    print('\n'.join(results))

main()