from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from keras.datasets import mnist
from keras.utils import np_utils
from keras.callbacks import TensorBoard
import tensorflow as tf
import matplotlib.pyplot as plt

batch_size = 140
nb_classes = 10
nb_epoch = 100

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
Y_Train = np_utils.to_categorical(y_train, nb_classes)
Y_Test = np_utils.to_categorical(y_test, nb_classes)

# Logistic regression
model = Sequential()
model.add(Dense(output_dim=10, input_shape=(784,), init='normal', activation='tanh'))
model.compile(optimizer='RMSprop', loss='mean_squared_error', metrics=['accuracy'])
model.summary()

# Train
tensorboard = TensorBoard(log_dir="logsl4/{}",histogram_freq=0, write_graph=True, write_images=True)
history=model.fit(X_train, Y_Train, nb_epoch=nb_epoch, batch_size=batch_size,callbacks=[tensorboard])
# predicting the accuracy
score = model.evaluate(X_test, Y_Test, verbose=1)
print('Summary: Loss: %.2f, Accuracy: %.2f' % (score[0], score[1]))

plt.plot(history.history['loss'])
# plt.plot(history.history['test_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()