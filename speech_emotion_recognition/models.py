import os
import joblib
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import (
    Dense,
    Conv1D,
    Flatten,
    Dropout,
    Activation,
    MaxPooling1D,
)
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def cnn_model(X, y):
    """
    This function trains the neural network.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    x_traincnn = np.expand_dims(X_train, axis=2)
    x_testcnn = np.expand_dims(X_test, axis=2)

    model = Sequential()
    model.add(Conv1D(64, 5, padding="same", input_shape=(40, 1)))
    model.add(Activation("relu"))
    model.add(Conv1D(128, 5, padding="same"))
    model.add(Activation("relu"))
    model.add(Dropout(0.1))
    model.add(MaxPooling1D(pool_size=(8)))
    model.add(
        Conv1D(
            128,
            5,
            padding="same",
        )
    )
    model.add(Activation("relu"))
    model.add(
        Conv1D(
            128,
            5,
            padding="same",
        )
    )
    model.add(Activation("relu"))
    model.add(Flatten())
    model.add(Dense(8))
    model.add(Activation("softmax"))

    # rmsprop = RMSprop(lr=0.00001, decay=1e-6)

    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer="rmsprop",
        metrics=["accuracy"],
    )

    cnn_history = model.fit(
        x_traincnn,
        y_train,
        batch_size=16,
        epochs=50,
        validation_data=(x_testcnn, y_test),
    )

    # Plot model loss
    plt.plot(cnn_history.history["loss"])
    plt.plot(cnn_history.history["val_loss"])
    plt.title("CNN model loss")
    plt.ylabel("loss")
    plt.xlabel("epoch")
    plt.legend(["train", "test"])
    plt.savefig("speech_emotion_recognition/images/cnn_loss.png")
    plt.close()

    # Plot model accuracy
    plt.plot(cnn_history.history["accuracy"])
    plt.plot(cnn_history.history["val_accuracy"])
    plt.title("CNN model accuracy")
    plt.ylabel("acc")
    plt.xlabel("epoch")
    plt.legend(["train", "test"])
    plt.savefig("speech_emotion_recognition/images/cnn_accuracy.png")

    predictions = model.predict_classes(x_testcnn)
    new_y_test = y_test.astype(int)
    matrix = confusion_matrix(new_y_test, predictions)

    print(classification_report(new_y_test, predictions))
    print(matrix)

    model_name = "cnn_model.h5"

    if not os.path.isdir("speech_emotion_recognition/models"):
        os.makedirs("speech_emotion_recognition/models")

    model_path = os.path.join("speech_emotion_recognition/models", model_name)
    model.save(model_path)
    print("Saved trained model at %s " % model_path)


if __name__ == "__main__":
    print("Training started")
    X = joblib.load("speech_emotion_recognition/features/X.joblib")
    y = joblib.load("speech_emotion_recognition/features/y.joblib")
    cnn_model(X=X, y=y)
    print("Model finished.")