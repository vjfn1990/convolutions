import cv2
import numpy
A = cv2.imread('original.jpg')
A = numpy.float32(A)
B = cv2.imread('mask.jpg')
color = [255, 127, 127]
color = [color[2], color[1], color[0]]
color = numpy.float32(color)
color[0] = color[0] / 255.0
color[1] = color[1] / 255.0
color[2] = color[2] / 255.0
for i in range(1280):
	for j in range(1920):
		if B[i,j,0] > 127:
			A[i,j,0] = A[i,j,0] / 255.0
			if color[0] > 0.5:
				A[i,j,0] = (1.0 - (1.0 - 2.0 * (color[0] - 0.5)) * (1.0 - A[i,j,0]));
			else:
				A[i,j,0] = ((2.0 * color[0]) * A[i,j,0]);
			A[i,j,0] = A[i,j,0] * 255.0
			A[i,j,1] = A[i,j,1] / 255.0
			if color[1] > 0.5:
				A[i,j,1] = (1.0 - (1.0 - 2.0 * (color[1] - 0.5)) * (1.0 - A[i,j,1]));
			else:
				A[i,j,1] = ((2.0 * color[1]) * A[i,j,1]);
			A[i,j,1] = A[i,j,1] * 255.0
			A[i,j,2] = A[i,j,2] / 255.0
			if color[2] > 0.5:
				A[i,j,2] = (1.0 - (1.0 - 2.0 * (color[2] - 0.5)) * (1.0 - A[i,j,2]));
			else:
				A[i,j,2] = ((2.0 * color[2]) * A[i,j,2]);
			A[i,j,2] = A[i,j,2] * 255.0
A = numpy.uint8(A)
cv2.imwrite('modified.jpg', A);

