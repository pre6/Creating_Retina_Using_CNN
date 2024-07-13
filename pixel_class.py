import numpy as np

class Pixel:
    def __init__(self, wavelength):
        self.wavelength = wavelength

    

    @property
    def rod(self):
        return 150 * np.exp(-((self.wavelength - 500) ** 2) / (2 * 60 ** 2)) / (60 * np.sqrt(2 * np.pi))

    @property
    def s_cone(self):
        return 150 * np.exp(-((self.wavelength - 424) ** 2) / (2 * 60 ** 2)) / (60 * np.sqrt(2 * np.pi))

    @property
    def m_cone(self):
        return 150 * np.exp(-((self.wavelength - 523) ** 2) / (2 * 60 ** 2)) / (60 * np.sqrt(2 * np.pi))

    @property
    def l_cone(self):
        return 150 * np.exp(-((self.wavelength - 563) ** 2) / (2 * 60 ** 2)) / (60 * np.sqrt(2 * np.pi))
