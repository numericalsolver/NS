import control as ct
import matplotlib.pyplot as plt
import random
import numpy as np
import matplotlib.patches as patches
# numerator= [1]#(input("enter the value of the numerator:"))
# denomenator= [1,2,1]#(input("enter the value of the denomenator:"))
numerator=[1,-2]
denomenator=[1,2,1]
transfer_function=ct.tf(numerator,denomenator)
print(transfer_function)
plt.xlabel('Real axis',fontsize=14)
plt.ylabel('Imaginary axis',fontsize=14)
plt.title('NYQUIST PLOT',fontsize=16)
plt.axhline(0, color='black',linewidth=2)
plt.axvline(0, color='black',linewidth=2)

def random_color():
    return (random.random(), random.random(), random.random())

contour=ct.nyquist_plot(transfer_function,return_contour=True ,color=random_color(),arrows =2 ,arrow_size=10,start_marker='o',start_marker_size=10,linewidth=4)
for arrow in plt.gca().findobj(patches.FancyArrowPatch):
    color ="black"
    arrow.set_color(color)
    arrow.set_zorder(30)

stability_margins = ct.stability_margins(transfer_function)
print("Stability Margins:", stability_margins)
gm = stability_margins[0] 
pm = stability_margins[1] 
if gm > 1 and pm > 0:
    print("System is stable (Gain Margin > 1 and Phase Margin > 0)")
else:
    print("System is unstable")
   

plt.text(0.95, 0.95, r'$0 < \omega < \infty$', fontsize=12, ha='right', va='top',weight='bold', transform=plt.gca().transAxes)
plt.text(0.95, 0.9, r'$-\infty < \omega < 0$', fontsize=12, ha='right', va='top',weight='bold', transform=plt.gca().transAxes)
plt.text(0.05, 0.95, f'Transfer Function: {transfer_function}', fontsize=12, ha='left', va='top', transform=plt.gca().transAxes)


plt.plot(-1, 0, marker='o', markersize=8, color='blue')
plt.text(-1, 0, '(-1, 0)', fontsize=10, ha='left', va='bottom')

omega = np.logspace(-2, 2, 100)
frequency_response = ct.freqresp(transfer_function, omega)
print("Frequency Response:")
print(frequency_response)
contour = frequency_response[1]  
def count_encirclements(contour):
     num_encirclements = 0
     for i in range(len(contour) - 1):
         if contour[i] < -1 and contour[i + 1] > -1:
             num_encirclements += 1
         elif contour[i] > -1 and contour[i + 1] < -1:
             num_encirclements -= 1
     return num_encirclements # Call the function to count encirclements
num_encirclements = count_encirclements(contour)
print(f"Number of encirclements of the critical point (-1,0) in the Nyquist plot: {num_encirclements}")
plt.show()
