# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:11:25 2022

@author: DELL
"""
import logging
import numpy as np
from torch.utils.data import Dataset

class RealDataset(Dataset){
   def __init__(self,config, mode = 'train'):
       super._init_()
       self.config = config
       self.mode = mode
       self.load_dataset = self.config['dataset']
   
   def __len__(self):
       self.rolling_window.shape[0]
   
   def __getitem__(self, index):
       input = target = self.rolling_windows[index,:,:]
       sample = ["input" = input, "target" = target]
       return sample
   
   def __loaddataset__ (self,dataset):
       data_dir = self.config('data_dir')
       self.data = np.load(data_dir + dataset + ".npz")
        if self.mode == 'train':
        data = self.data['train']
        else:
        data = self.data['test']
       
       self.rolling_windows = np.lib.stride_tricks.sliding_window_view(data, self.config["l_win"], axis=0, writeable=True).transpose(0, 2, 1)
       