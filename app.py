import streamlit as st
import cv2
import numpy as np
from PIL import Image

import torch
# Load the YOLO model
model = torch.load('your_yolo_model.pt')
