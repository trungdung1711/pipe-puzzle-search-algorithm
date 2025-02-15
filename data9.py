from state.pipe import Pipe
from state.grid import Grid
from state.direction import Direction
from state.type import PipeType


def data9() -> Grid:
    grid = Grid()
    
    pipe00 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.DOWN, (0, 0))
    pipe01 = Pipe(PipeType.STRAIGHT, Direction.RIGHT, (0, 1))
    pipe02 = Pipe(PipeType.T_SHAPE, Direction.UP, (0, 2))
    pipe03 = Pipe(PipeType.L_SHAPE, Direction.UP, (0, 3))

    pipe10 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.LEFT, (1, 0))
    pipe11 = Pipe(PipeType.STRAIGHT, Direction.RIGHT, (1, 1))
    pipe12 = Pipe(PipeType.T_SHAPE, Direction.RIGHT, (1, 2))
    pipe13 = Pipe(PipeType.STRAIGHT, Direction.RIGHT, (1, 3))

    pipe20 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.DOWN, (2, 0))
    pipe21 = Pipe(PipeType.STRAIGHT, Direction.LEFT, (2, 1))
    pipe22 = Pipe(PipeType.T_SHAPE, Direction.RIGHT, (2, 2))
    pipe23 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.DOWN, (2, 3))

    pipe30 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.LEFT, (3, 0))
    pipe31 = Pipe(PipeType.STRAIGHT, Direction.RIGHT, (3, 1))
    pipe32 = Pipe(PipeType.T_SHAPE, Direction.UP, (3, 2))
    pipe33 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.RIGHT, (3, 3))

    grid.set_pipe(0, 0, pipe00)
    grid.set_pipe(0, 1, pipe01)
    grid.set_pipe(0, 2, pipe02)
    grid.set_pipe(0, 3, pipe03)

    grid.set_pipe(1, 0, pipe10)
    grid.set_pipe(1, 1, pipe11)
    grid.set_pipe(1, 2, pipe12)
    grid.set_pipe(1, 3, pipe13)

    grid.set_pipe(2, 0, pipe20)
    grid.set_pipe(2, 1, pipe21)
    grid.set_pipe(2, 2, pipe22)
    grid.set_pipe(2, 3, pipe23)

    grid.set_pipe(3, 0, pipe30)
    grid.set_pipe(3, 1, pipe31)
    grid.set_pipe(3, 2, pipe32)
    grid.set_pipe(3, 3, pipe33)
    return grid