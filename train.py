from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("drive/My Drive/Colab Notebooks/car1")
model_trainer.trainModel(num_objects=13, num_experiments=200, enhance_data=True, batch_size=32, show_network_summary=True)
