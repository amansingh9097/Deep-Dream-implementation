import cv2
import os

dream_name = "paris2"
dream_path = "dream/{}".format(dream_name)

#windows codec:
# fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Linux codec:
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

out = cv2.VideoWriter('{}.avi'.format(dream_name), fourcc, 10, (800,450))
for i in range(9999999999999999999):
	if os.path.isfile('dream/{}/img_{}.jpg'.format(dream_name, i+1)):
		print('{} already exists, continuing along...'.format(i+1))

	else:
		dream_length = i
		break

for i in range(dream_length):
	img_path = os.path.join(dream_path, "img_{}.jpg".format(i))
	print(img_path)
	frame = cv2.imread(img_path)
	out.write(frame)

out.release()