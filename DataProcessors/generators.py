

def generator(X_data, y_data, batch_size):

  samples_per_epoch = X_data.shape[0]
  number_of_batches = samples_per_epoch/batch_size
  counter=0

  while 1:

    X_batch = np.array(X_data[batch_size*counter:batch_size*(counter+1)]).astype('float32')
    y_batch = np.array(y_data[batch_size*counter:batch_size*(counter+1)]).astype('float32')
    counter += 1
    yield X_batch,y_batch

    #restart counter to yeild data in the next epoch as well
    if counter >= number_of_batches:
        counter = 0


def keras_gen():
    # https://stackoverflow.com/questions/46493419/use-a-generator-for-keras-model-fit-generator
    from keras.datasets import mnist
    from keras.models import Sequential
    from keras.layers.core import Dense, Dropout, Activation, Flatten, Reshape
    from keras.layers.convolutional import Convolution1D, Convolution2D, MaxPooling2D
    from keras.utils import np_utils


     model = Sequential()
     model.add(Dense(12, activation='relu', input_dim=dataFrame.shape[1]))
     model.add(Dense(1, activation='sigmoid'))


     model.compile(loss='binary_crossentropy', optimizer='adadelta', metrics=['accuracy'])

     #Train the model using generator vs using the full batch
     batch_size = 8

     model.fit_generator(generator(dataFrameTrain,expectedFrameTrain,batch_size), epochs=3,steps_per_epoch = dataFrame.shape[0]/batch_size, validation_data=generator(dataFrameTest,expectedFrameTest,batch_size*2),validation_steps=dataFrame.shape[0]/batch_size*2)

     #without generator
     #model.fit(x = np.array(dataFrame), y = np.array(expected), batch_size = batch_size, epochs = 3)


def tensorflow_gen():
    # https://stackoverflow.com/questions/48769142/tensorflow-how-to-use-dataset-from-generator-in-estimator
    shapes = ((SIZE,), (SIZE,))
    dataset = tf.data.Dataset.from_generator(generator=_generator,
                                             output_types=(tf.float32, tf.float32),
                                             output_shapes=shapes)
    x_col = tf.feature_column.numeric_column(key='x', shape=(SIZE,))
    es = tf.estimator.LinearRegressor(feature_columns=[x_col],
                                  label_dimension=10)