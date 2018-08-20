# View Point Estimation

Classification of view points of  cars in order to sort listing images automatically according to their labels

# Dataset
5000 labelled images divided into classes with different perspectives - back, front, side left, side right, back left, back right, front left, front right and inside.

# Model
Custom VGGNet Model – 
  1. Instantiate the model with a 96 x 96 x 3  input volume
	2. Use sigmoid activation function for multi label classification
  3. RELU  activation (Rectified Linear Unit)
	4. Max Pooling
	5. 25% Dropout
  
# Implementation
  1. User uploads new listing
  2. Network assign probabilities to viewpoints
  3. Save Probability Information
  4. Move images to specific labels
 
# Results
  Training Accuracy – 89.48 % 
  Testing Accuracy -  88.14%





