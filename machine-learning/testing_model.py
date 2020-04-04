import cv2
import numpy as np
import glob


from hu_moments_generation import hu_moments_of_file
from label_converters import int_to_label

def load_and_test_svm():
    svm = cv2.ml.SVM_load('./generated-files/svm_shapes_model.yml')
    files = glob.glob('./shapes/testing/*')
    for f in files:
        hu_moments = hu_moments_of_file(f)
        sample = np.array([hu_moments], dtype=np.float32)
        testResponse = svm.predict(sample)[1]
        print(f + ' -> ' + int_to_label(testResponse))
