import tensorflow.keras as keras
from train_england import build_model, OUTPUT_UNITS, NUM_UNITS, LOSS, LEARNING_RATE

def load_test_data():
    # This function should load your test data and return it
    # Replace this with your actual code to load test data
    pass

def test_model():
    # Load the test data
    test_data, test_labels = load_test_data()

    # Build the model
    model = build_model(OUTPUT_UNITS, NUM_UNITS, LOSS, LEARNING_RATE)

    # Load the trained weights
    model.load_weights('model.h5')

    # Evaluate the model
    test_loss, test_accuracy = model.evaluate(test_data, test_labels, verbose=2)
    print('\nTest accuracy:', test_accuracy)

if __name__ == "__main__":
    test_model()