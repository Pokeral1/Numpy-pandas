import numpy as np
prices = np.array([120, 450, 89, 300, 175, 520, 95])
prices= prices*0.9
print(prices[prices>150])