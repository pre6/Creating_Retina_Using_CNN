from PIL import Image
import numpy as np
import colorsys

class ImageConverter:
    
    def __init__(self, image_path):
        # ImageConverter(path of file)
        self.image_path = image_path
        # coverts it to RBG
        self.image = Image.open(image_path).convert("RGB")
    
    @staticmethod
    def rgb_to_wavelength(r, g, b):
        # Normalize RGB values to the range [0, 1]
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        
        # Convert RGB to HSV
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        
        # Convert hue to degrees
        h_deg = h * 360
        
        # Map hue to wavelength
        if 0 <= h_deg < 60:
            wavelength = 620 - (h_deg / 60) * (620 - 590)
        elif 60 <= h_deg < 120:
            wavelength = 590 - ((h_deg - 60) / 60) * (590 - 495)
        elif 120 <= h_deg < 180:
            wavelength = 495 - ((h_deg - 120) / 60) * (495 - 480)
        elif 180 <= h_deg < 240:
            wavelength = 480 - ((h_deg - 180) / 60) * (480 - 450)
        elif 240 <= h_deg < 300:
            wavelength = 450 - ((h_deg - 240) / 60) * (450 - 400)
        else:
            wavelength = 400 + ((h_deg - 300) / 60) * (620 - 400)
        
        return wavelength

    @staticmethod
    def rgb_to_brightness(r, g, b):
        # Convert RGB to HSV to get the brightness (value) component
        h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
        return v * 255

    
    def image_to_wavelengths(self):
        # Get image dimensions
        width, height = self.image.size
        
        # Create an array to hold the wavelength values
        wavelength_array = np.zeros((height, width))
        
        # Process each pixel
        for y in range(height):
            for x in range(width):
                r, g, b = self.image.getpixel((x, y))
                wavelength = self.rgb_to_wavelength(r, g, b)
                wavelength_array[y, x] = wavelength
        
        return wavelength_array



    def image_to_brightness(self):
        # Get image dimensions
        width, height = self.image.size
        
        # Create an array to hold the wavelength values
        wavelength_array_b = np.zeros((height, width))
        
        # Process each pixel
        for y in range(height):
            for x in range(width):
                r, g, b = self.image.getpixel((x, y))
                brightness = self.rgb_to_brightness(r, g, b)
                wavelength_array_b[y, x] = brightness
        
        return wavelength_array_b
  