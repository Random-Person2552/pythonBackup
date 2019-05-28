import matplotlib.pyplot as plt

# Column 2 from data table
A_input_chars = [1, 2, 3, 4]
B_input_chars = [1, 2, 3, 4, 5, 6, 7, 8]

# Column 3 and 4 from data table
# Replace list elements with your times
A_time = [0.0068,0.0136,0.195,2.029] 
B_time = [0.0257,0.0385,0.0216,0.0353,0.0721,0.202,0.633,1.938]

fig, ax = plt.subplots(1,1)
# plot(x_list, y_list, "color and style")
ax.plot(A_input_chars, A_time, 'ro-', label='Algorithm A') # red dots
ax.plot(B_input_chars, B_time, 'bo-',label='Algorithm B') # blue dots

# Label and show
ax.set_xlabel ("Length of input in characters")
ax.set_ylabel("Worst case execution time")
ax.set_title("Execution time vs. input length")
ax.legend(loc='center left')
ax.margins(.1)
fig.set_facecolor('white')
fig.show()