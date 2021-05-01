import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
import tensorflow
tensorflow.compat.v1.disable_eager_execution()
from tensorflow.keras.datasets import mnist

#Téléchargement du dataset (X est l'image y un charactéristique, ici le chiffre écrit de 0 à 9)
(trainX, trainy), (testX, testy) = mnist.load_data()

print('Training data shapes: X=%s, y=%s' % (trainX.shape, trainy.shape))
print('Testing data shapes: X=%s, y=%s' % (testX.shape, testy.shape))

#Affichage de 5 échantillons du dataset d'entrainement
for j in range(5):
    i = np.random.randint(0, 10000)
    plt.subplot(550 + 1 + j)
    plt.imshow(trainX[i], cmap='gray')
    plt.title(trainy[i])
plt.show()

#Mise en forme des dataframes avec pandas
#Conversion de toutes les valeurs des 2 datasets en float32 
train_data = trainX.astype('float32')/255
test_data = testX.astype('float32')/255


train_data = np.reshape(train_data, (60000, 28, 28, 1))
test_data = np.reshape(test_data, (10000, 28, 28, 1))

#affichage des dimensions du dataset
#print (train_data.shape, test_data.shape)  #pour mnist : (60000, 28, 28, 1) (10000, 28, 28, 1)



"""
VARIABLES
"""

nbrVariables=10 #si >2 pas de plot  || Il s'agit du nombre de variables de l'espace latent 
nbrEpochs=1  #nombre d'entrainements réalisés l'erreur décroit logarithmiquement (c'est presque inutile au dela de 10)


"""
"""

#Création du réseau de neuronne de l'encodeur

input_data = tensorflow.keras.layers.Input(shape=(28, 28, 1))

encoder = tensorflow.keras.layers.Conv2D(64, (5,5), activation='relu')(input_data)
encoder = tensorflow.keras.layers.MaxPooling2D((2,2))(encoder)

encoder = tensorflow.keras.layers.Conv2D(64, (3,3), activation='relu')(encoder)
encoder = tensorflow.keras.layers.MaxPooling2D((2,2))(encoder)

encoder = tensorflow.keras.layers.Conv2D(32, (3,3), activation='relu')(encoder)
encoder = tensorflow.keras.layers.MaxPooling2D((2,2))(encoder)

encoder = tensorflow.keras.layers.Flatten()(encoder)
encoder = tensorflow.keras.layers.Dense(16)(encoder)

def sample_latent_features(distribution):
    distribution_mean, distribution_variance = distribution
    batch_size = tensorflow.shape(distribution_variance)[0]
    random = tensorflow.keras.backend.random_normal(shape=(batch_size, tensorflow.shape(distribution_variance)[1]))
    return distribution_mean + tensorflow.exp(0.5 * distribution_variance) * random


distribution_mean = tensorflow.keras.layers.Dense(nbrVariables, name='mean')(encoder)
distribution_variance = tensorflow.keras.layers.Dense(nbrVariables, name='log_variance')(encoder)
latent_encoding = tensorflow.keras.layers.Lambda(sample_latent_features)([distribution_mean, distribution_variance])

encoder_model = tensorflow.keras.Model(input_data, latent_encoding)
encoder_model.summary()

#Création du réseau de neuronne du décodeur


decoder_input = tensorflow.keras.layers.Input(shape=(nbrVariables))
decoder = tensorflow.keras.layers.Dense(64)(decoder_input)
decoder = tensorflow.keras.layers.Reshape((1, 1, 64))(decoder)
decoder = tensorflow.keras.layers.Conv2DTranspose(64, (3,3), activation='relu')(decoder)

decoder = tensorflow.keras.layers.Conv2DTranspose(64, (3,3), activation='relu')(decoder)
decoder = tensorflow.keras.layers.UpSampling2D((2,2))(decoder)

decoder = tensorflow.keras.layers.Conv2DTranspose(64, (3,3), activation='relu')(decoder)
decoder = tensorflow.keras.layers.UpSampling2D((2,2))(decoder)

decoder_output = tensorflow.keras.layers.Conv2DTranspose(1, (5,5), activation='relu')(decoder)

decoder_model = tensorflow.keras.Model(decoder_input, decoder_output)
decoder_model.summary()

encoded = encoder_model(input_data)
decoded = decoder_model(encoded)
autoencoder = tensorflow.keras.models.Model(input_data, decoded)



def get_loss(distribution_mean, distribution_variance):
    
    def get_reconstruction_loss(y_true, y_pred):
        reconstruction_loss = tensorflow.keras.losses.mse(y_true, y_pred)
        reconstruction_loss_batch = tensorflow.reduce_mean(reconstruction_loss)
        return reconstruction_loss_batch*28*28
    
    def get_kl_loss(distribution_mean, distribution_variance):
        kl_loss = 1 + distribution_variance - tensorflow.square(distribution_mean) - tensorflow.exp(distribution_variance)
        kl_loss_batch = tensorflow.reduce_mean(kl_loss)
        return kl_loss_batch*(-0.5)
    
    def total_loss(y_true, y_pred):
        reconstruction_loss_batch = get_reconstruction_loss(y_true, y_pred)
        kl_loss_batch = get_kl_loss(distribution_mean, distribution_variance)
        return reconstruction_loss_batch + kl_loss_batch
    
    return total_loss



autoencoder.compile(loss=get_loss(distribution_mean, distribution_variance), optimizer='adam')
autoencoder.summary()

#tensorflow.config.run_functions_eagerly(True)#experimental_

autoencoder.fit(train_data, train_data, epochs=nbrEpochs, batch_size=64, validation_data=(test_data, test_data))


#Affichage du résultat (avant/après)

offset=400
print ("Images en Entrée")
# Images Réelles 
for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.imshow(test_data[i+offset,:,:, -1], cmap='gray')
plt.show()

# Images Reconstruites
print ("Images Reconstruites par le VAE")
for i in range(9):
    plt.subplot(330 + 1 + i)
    output = autoencoder.predict(np.array([test_data[i+offset]]))
    op_image = np.reshape(output[0]*255, (28, 28))
    plt.imshow(op_image, cmap='gray')
plt.show()

#Si le nombre de variables ==2 on peut afficher une carte de l'espace latent 
if nbrVariables==2:
    generator_model = decoder_model
    x_values = np.linspace(-3, 3, 30)
    y_values = np.linspace(-3, 3, 30)
    figure = np.zeros((28 * 30, 28 * 30))
    for ix, x in enumerate(x_values):
        for iy, y in enumerate(y_values):
            latent_point = np.array([[x, y]])
            generated_image = generator_model.predict(latent_point)[0]
            figure[ix*28:(ix+1)*28, iy*28:(iy+1)*28,] = generated_image[:,:,-1]
    
    plt.figure(figsize=(15, 15))
    plt.imshow(figure, cmap='gray', extent=[3,-3,3,-3])
    plt.show()

elif nbrVariables==10:
  generator_model = decoder_model
  for i in range(10):
    plt.subplot(5,2,1 + i)
    list=[0,0,0,0,0,0,0,0,0,0]
    list[i]=10
    latent_point=np.array([list])
    generated_image = generator_model.predict(latent_point)[0]
    plt.imshow(generated_image[:,:,-1], cmap='gray')
    plt.title(str(list))
    list[i]=0
  plt.show()
