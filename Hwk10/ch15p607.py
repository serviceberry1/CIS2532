# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:52:13 2020

@author: anony1
"""
# =============================================================================
from sklearn.datasets import load_digits
digits = load_digits()
import matplotlib.pyplot as plt
figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))
# for item in zip(axes.ravel(), digits.images, digits.target):
#     axes, image, target = item
#     axes.imshow(image, cmap=plt.cm.Blues_r)
#     axes.set_xticks([])
#     axes.set_yticks([])
#     axes.set_title(target)
# plt.tight_layout()
# 
# =============================================================================
# axes = plt.subplot()
# image = plt.imshow(digits.images[22], cmap=plt.cm.gray_r)
# xticks = axes.set_xticks([])
# yticks = axes.set_yticks([])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, random_state=11)

X_train.shape

