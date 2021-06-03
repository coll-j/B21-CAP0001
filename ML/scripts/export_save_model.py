import tensorflow as tf

# The export path contains the name and the version of the model
# tf.keras.backend.set_learning_phase(0)  # Ignore dropout at inference
model = tf.keras.models.load_model('../binary_repo_83_41.h5')
export_path = '../hs_classifier/1'

# Fetch the Keras session and save the model
# The signature definition is defined by the input and output tensors
# And stored with the default serving key
tf.saved_model.save(model, export_path)