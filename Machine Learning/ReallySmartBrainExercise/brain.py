from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()


prediction = ImagePrediction()
# download what model you want
# set model you want to use
prediction.setModelTypeAsSqueezeNet()
prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

# result count is how many predictions you want the model to give you
predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "house.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)