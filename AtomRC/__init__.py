# -*- coding: utf-8 -*-

# Copyright 2023 InfernalAtom
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""AtomRC is a remote control
"""


import os
import socket
import time
import tkinter as tk
import numpy as np
import cv2
import requests
import re

try:
    from PIL import ImageGrab
except ImportError:
    PIL = None

    

s = socket.socket()
