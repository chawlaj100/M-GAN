import os
import pickle
from PIL import Image
import cv2
import torch
import torch.utils.data as data
import torchvision.transforms as transforms

def img_load_and_transform(path, transform):
    img = cv2.imread(path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img_rgb)
    img = transform(img)
    return img
    
class ReadFromVec(data.Dataset):
    def __init__(self, path, img_transform=None):
        super(ReadFromVec, self).__init__()
        self.img_transform = img_transform

        self.data = self._load_dataset(path)

    def _load_dataset(self, path):
        get_file = open(path, 'rb')
        output = pickle.load(get_file)
        return output

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        datum = self.data[index]
        img = img_load_and_transform(datum['img'], self.img_transform)
        word_vec = datum['word_vec']
        len_desc = datum['len_desc']
        #selected = np.random.choice(word_vec.size(0))
        #word_vec = word_vec[selected, ...]
        #len_desc = len_desc[selected]
        return img, word_vec, len_desc