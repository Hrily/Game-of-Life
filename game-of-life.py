import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import convolve2d
import matplotlib.animation as animation
import patterns

grid_size = 50
time_interval = 100

shape = (grid_size, grid_size)
initial_board = tf.random_uniform(shape, minval=0, maxval=2, dtype=tf.int32)
empty_board = tf.random_uniform(shape, minval=0, maxval=1, dtype=tf.int32)

pattern = patterns.random

def update_board(X):
    # Check out the details at: https://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/
    # Compute number of neighbours,
    N = convolve2d(X, np.ones((3, 3)), mode='same', boundary='wrap') - X
    # Apply rules of the game
    X = (N == 3) | (X & (N == 2))
    return X

board = tf.placeholder(tf.int32, shape=shape, name='board')
board_update = tf.py_func(update_board, [board], [tf.int32])

with tf.Session() as session:
    initial_board_values = session.run(initial_board)
    X = session.run(initial_board)
    if len(pattern[0]):
        X = session.run(empty_board)
        X[2:2+len(pattern), 2:2+len(pattern[0])] = pattern
    def game_of_life(*args):
        global X
        X = session.run(board_update, feed_dict={board: X})[0]
        plot.set_array(X)
        return plot,
    fig = plt.figure()
    plot = plt.imshow(X, cmap='Greys',  interpolation='nearest')
    ani = animation.FuncAnimation(fig, game_of_life, interval=time_interval, blit=True)
    plt.show()