#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os
class GaussianScaler:
    def __init__(self, eps=1e-8):
        self.eps = eps
        self.mean_val = None
        self.std_val = None

    def fit(self, data):
        self.mean_val = np.mean(data)
        self.std_val = np.std(data)

    def transform(self, data):
        if self.mean_val is None or self.std_val is None:
            raise ValueError("Scaler has not been fitted.")
        standardized_data = (data - self.mean_val) / (self.std_val + self.eps)
        return standardized_data

    def inverse_transform(self, standardized_data):
        if self.mean_val is None or self.std_val is None:
            raise ValueError("Scaler has not been fitted.")
        original_data = (standardized_data * (self.std_val + self.eps)) + self.mean_val
        return original_data

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)

    def save(self, filepath: str, compress: bool = True):
        """保存标准化器参数"""
        if self.mean_val is None or self.std_val is None:
            raise RuntimeError("请先调用 fit() 或 fit_transform()")
        

        data = {
            'mean_val': float(self.mean_val),
            'std_val': float(self.std_val),
            'eps': float(self.eps),
            'scaler_type': 'GaussianScaler'
        }
        
        save_func = np.savez_compressed if compress else np.savez
        save_func(filepath, **data)
        
        print(f"GaussianScaler 已保存至: {filepath}")

    @classmethod
    def load(cls, filepath: str):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"文件不存在: {filepath}")
        
        data = np.load(filepath, allow_pickle=True)
        instance = cls(eps=float(data['eps']))
        instance.mean_val = float(data['mean_val'])
        instance.std_val = float(data['std_val'])
        return instance