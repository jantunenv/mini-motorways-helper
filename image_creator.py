import numpy as np
import pyautogui
import time
from PIL import Image

def create_heat_map(fps=10, length=5):

	data = []
	dt_previous = time.time()
	start_t = dt_previous
	while(True):
		dt = time.time()
		if(dt - start_t > length):
			break

		if(dt - 1.0/fps >= dt_previous):
			screens = pyautogui.screenshot()
			frame = np.array(screens)
			data.append(frame)

	mean_frame = np.zeros(data[0].shape, dtype=int)
	for frame in data:
		mean_frame = np.add(mean_frame, frame)

	mean_frame = mean_frame/len(data)

	mean_frame = mean_frame.astype(np.uint8)

	img = Image.fromarray(mean_frame, 'RGB')
	return(img)

def main():
	img = create_heat_map()
	img.show()

if (__name__ == "__main__"):
	main()
