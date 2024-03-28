import numpy as np
import matplotlib.pyplot as plt
import control
import base64
from io import BytesIO

class control_systems:
    def __init__(self, numerator_coeffs, denominator_coeffs):
        self.G = control.tf(numerator_coeffs, denominator_coeffs)


    # your respective code that returns output image and  steps (text format)
        # mention the author code details in the comments along with contact details
        # conversion of base64 is compulsory for any data

    def plot_bode(self):
        print("check 2")
        (num, den) = control.pade(0.25, 3)
        Gp = control.tf(num, den) * self.G

        mag, phase, omega = control.bode(Gp)
        w = np.logspace(-1.5, 1, 200)
        mag, phase, omega = control.bode(Gp, w)
        w = np.logspace(-1, 1)
        mag, phase, omega = control.bode(Gp, w)
        plt.tight_layout()

        wc = np.interp(-180.0, np.flipud(phase), np.flipud(omega))
        Kcu = np.interp(wc, omega, mag)

        print('Crossover freq = ', wc, ' rad/sec')
        print('Gain at crossover = ', Kcu)

        mag, phase, omega = control.bode(Gp, w)
        plt.tight_layout()

        ax1, ax2 = plt.gcf().axes

        plt.sca(ax1)
        plt.plot(plt.xlim(), [Kcu, Kcu], 'r--')
        plt.plot([wc, wc], plt.ylim(), 'r--')
        plt.title(f"Gain at Crossover = {0:.3g}".format(Kcu))

        plt.sca(ax2)
        plt.plot(plt.xlim(), [-180, -180], 'r--')
        plt.plot([wc, wc], plt.ylim(), 'r--')
        plt.title(f"Crossover Frequency = {0:.3g} rad/sec".format(wc))

        # Save the plot image to a BytesIO buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()  # Close the plot to free up resources

        # Convert the image buffer to a base64-encoded string
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return image_data
    plt.show()