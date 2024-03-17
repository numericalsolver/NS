import control as ct
import matplotlib.pyplot as plt
numerator=[]
denomenator=[]
# numerator= [1]#(input("enter the value of the numerator:"))
# denomenator= [1,2,1]#(input("enter the value of the denomenator:"))
numerator=(input("enter the value of the numerator:"))
print(numerator)
denomenator=(input("enter the value of the denomenator:"))
print(denomenator)
transfer_function=ct.tf(numerator,denomenator)
print(transfer_function)
plt.xlabel('Real axis',fontsize=14)
plt.ylabel('Imaginary axis',fontsize=14)
plt.title('NYQUIST PLOT',fontsize=16)
plt.axhline(0, color='black',linewidth=2)
plt.axvline(0, color='black',linewidth=2)
contour=ct.nyquist_plot(transfer_function,return_contour=True,arrows =2 ,arrow_size=10,start_marker='o',start_marker_size=10,linewidth=4)
plt.show()