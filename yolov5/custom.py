from yolov5.models.common import *
from yolov5.utils.torch_utils import select_device

def load(weights, device='cpu'):
    device = select_device(device)
    model = AutoShape(DetectMultiBackend(weights, device=device, fuse=True), verbose=False)
    return model