from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


############## Input data##############

with open('/home/maya/public/PDP_Assignment1/input96.txt', 'r') as f:
    fx = np.fromstring(f.read(), sep=' ')

x = range(0,int(fx[0])) # x vector
fx = fx[1:]             # f vector



############## Derivative ##############

with open('/home/maya/public/PDP_Assignment1/output96_1_ref.txt', 'r') as f:
    dfx = np.fromstring(f.read(), sep=' ')

with open('output.txt', 'r') as f:
    my_dfx = np.fromstring(f.read(), sep=' ')


############## PLOTS ##############

# Create a new figure and axis object
fig, ax = plt.subplots()

# Plot the data on the axis
ax.plot(x, fx, 'r-', label='Data')
ax.plot(x, dfx, 'b-', label='Correct Derivative')
ax.plot(x, my_dfx, 'g*', label='My Derivative')



# Settings
plt.rcParams.update({'font.size': 14})
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

ax.legend()
ax.grid(True)

ax.set_title('A1')

# Show the plot
plt.savefig('plot.png')




############## Error estimation ##############

error = my_dfx-dfx
print("Max error = ", max(error))