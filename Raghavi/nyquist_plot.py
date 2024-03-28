import control as ct
import matplotlib.pyplot as plt
import random
import numpy as np
import matplotlib.patches as patches

class NyquistPlot:
    def __init__(self, numerator, denomenator):
        self.numerator = numerator
        self.denomenator = denomenator
        self.transfer_function = ct.tf(self.numerator, self.denomenator)
        self.stability_margins = ct.stability_margins(self.transfer_function)

    def random_color(self):
        return (random.random(), random.random(), random.random())

    def contour_plot(self):
        contour = ct.nyquist_plot(self.transfer_function, return_contour=True,
                                  color=self.random_color(), arrows=2, arrow_size=10,
                                  start_marker='o', start_marker_size=10, linewidth=4)
        for arrow in plt.gca().findobj(patches.FancyArrowPatch):
            color = "black"
            arrow.set_color(color)
            arrow.set_zorder(30)
        return contour

    def print_stability_info(self):
        print(f"Stability Margins: {self.stability_margins}")
        gm = self.stability_margins[0]
        pm = self.stability_margins[1]
        if gm > 1 and pm > 0:
            print("System is stable (Gain Margin > 1 and Phase Margin > 0)")
        else:
            print("System is unstable")

    def add_plot_elements(self):
        plt.xlabel('Real axis', fontsize=14)
        plt.ylabel('Imaginary axis', fontsize=14)
        plt.title('NYQUIST PLOT', fontsize=16)
        plt.axhline(0, color='black', linewidth=2)
        plt.axvline(0, color='black', linewidth=2)
        plt.text(0.95, 0.95, r'$0 < \omega < \infty$', fontsize=12, ha='right', va='top', weight='bold',
                 transform=plt.gca().transAxes)
        plt.text(0.95, 0.9, r'$-\infty < \omega < 0$', fontsize=12, ha='right', va='top', weight='bold',
                 transform=plt.gca().transAxes)
        plt.text(0.05, 0.95, f'Transfer Function: {self.transfer_function}', fontsize=12, ha='left', va='top',
                 transform=plt.gca().transAxes)
        plt.plot(-1, 0, marker='o', markersize=8, color='blue')
        plt.text(-1, 0, '(-1, 0)', fontsize=10, ha='left', va='bottom')

    def plot_frequency_response(self):
        omega = np.logspace(-2, 2, 100)
        frequency_response = ct.freqresp(self.transfer_function, omega)
        print("Frequency Response:")
        print(frequency_response)
        return frequency_response[1]

    def count_encirclements(self, contour):
        num_encirclements = 0
        for i in range(len(contour) - 1):
            if contour[i] < -1 and contour[i + 1] > -1:
                num_encirclements += 1
            elif contour[i] > -1 and contour[i + 1] < -1:
                num_encirclements -= 1
        return num_encirclements

    def main(self):
        # Set up the figure
        self.contour = self.contour_plot()
        self.print_stability_info()
        self.add_plot_elements
        plt.show()