import pandas as pd
import matplotlib.pyplot as plt
import random
import skimage
from skimage import io
df_celeb = pd.read_csv('test3.csv')

def show_sample_image(nb=3, df=df_celeb, verbose=True):
    f, ax = plt.subplots(1, nb, figsize=(10,5))
    for i in range(nb):
        idx = random.randint(0, df.shape[0]-1)
        img_id = df.loc[idx].image_id
        img_uri = 'img_align_celeba/' + img_id
        img = skimage.io.imread(img_uri)  
        if verbose:
            label = img_id
            for col in df.columns:
                if df.loc[idx][col]==1:
                    label = label + '\n' + col  
            if nb > 1:
                ax[i].imshow(img)
                ax[i].set_title(label)
            else:
                ax.imshow(img) 
                ax.set_title(label)
        
    return img, list(df.loc[idx][1:df.shape[1]])
  
sample_img, sample_img_meta = show_sample_image()