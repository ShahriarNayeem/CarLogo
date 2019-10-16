from imageai.Prediction.Custom import CustomImagePrediction
from PIL import Image
import matplotlib.pyplot as plt
import os
import cv2
import glob
import numpy as np

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "model_ex-090_acc-0.933160.h5"))
prediction.setJsonPath(os.path.join(execution_path, "model_class.json"))
prediction.loadModel(num_objects=13)

# for single image
# predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "test_image/22.jpg"), result_count=5)
#
# for eachPrediction, eachProbability in zip(predictions, probabilities):
#     print(eachPrediction , " : " , eachProbability)
# end

# for multiple image
all_images_array = []
for filename in glob.glob('E:/Python Code/CarLogo/venv/test_image/*.jpg'):
    im = Image.open(filename)
    all_images_array.append(im)
i = 0
results_array = prediction.predictMultipleImages(all_images_array, result_count_per_image=1, input_type='array')

for each_result in results_array:
    predictions, percentage_probabilities = each_result["predictions"], each_result["percentage_probabilities"]
    for index in range(len(predictions)):
        print(predictions[index], " : ", percentage_probabilities[index])
    print("-----------------------")
    plt.imshow(np.asarray(all_images_array[i]))
    plt.show()
    i = i + 1
