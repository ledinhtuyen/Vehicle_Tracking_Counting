from yolov5.models.common import *
from yolov5.utils.torch_utils import select_device

def load(weights, device='cpu', half=False, verbose=True):
    device = select_device(device)
    model = AutoShape(DetectMultiBackend(weights, device=device, fuse=True, fp16=half), verbose=verbose)
    return model