import numpy as np
import control.matlab as ml
import matplotlib.pyplot as plt

class BodePlot:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.G = ml.tf(num, den)
    
    def calculate_margins(self):
        try:
            self.Gm, self.Pm, self.Wcg, self.Wcp = ml.margin(self.G)
            self.GM = 1 / abs(self.Gm) if not np.isnan(self.Wcg) else None
            self.PM = self.Pm if not np.isnan(self.Pm) else None
            self.stability = self.check_stability()
        except:
            self.Gm, self.Pm, self.Wcg, self.Wcp = None, None, None, None
            self.GM, self.PM, self.stability = None, None, None
    
    def check_stability(self):
        if np.isnan(self.Wcg) or np.isnan(self.Pm):
            return "Undefined"
        elif self.Gm > 1 and self.Pm > 0:
            return "Stable"
        else:
            return "Unstable"
    
    def display_info(self): 
        print("Given transfer function in S domain is", self.G)
        print("Gain crossover frequency:", round(self.Wcg, 2) if self.Wcg is not None else "Undefined")
        print("Phase crossover frequency:", round(self.Wcp, 2) if self.Wcp is not None else "Undefined")
        print("Gain margin:", round(self.GM, 2) if self.GM is not None else "Undefined")
        print("Phase margin:", round(self.PM, 2) if self.PM is not None else "Undefined")
        print("System stability:", self.stability)


def main():
    # Take input for numerator polynomial coefficients
    num_coefficients = input("Enter coefficients of the numerator polynomial separated by spaces: ")
    num = np.array(list(map(float, num_coefficients.split())))

    # Take input for denominator polynomial coefficients
    den_coefficients = input("Enter coefficients of the denominator polynomial separated by spaces: ")
    den = np.array(list(map(float, den_coefficients.split())))
    
    plotter = BodePlot(num, den)
    plotter.calculate_margins()
    plotter.display_info()

    # Plot Bode plot
    mag, phase, w = ml.bode(plotter.G)
    plt.show()

if __name__ == "__main__":
    main()
