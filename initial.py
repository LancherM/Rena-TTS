import logging

from vits import commons, utils

numba_logger = logging.getLogger('numba')
numba_logger.setLevel(logging.WARNING)

import librosa
import matplotlib.pyplot as plt

import os
import json
import math
import torch
import soundfile as sf
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader

import vits.commons
import vits.utils
from vits.data_utils import TextAudioLoader, TextAudioCollate, TextAudioSpeakerLoader, TextAudioSpeakerCollate
from vits.models import SynthesizerTrn
from vits.text.cleaners import japanese_phrase_cleaners, japanese_tokenization_cleaners
from vits.text import cleaned_text_to_sequence


def get_text(text, hps):
    text_norm = cleaned_text_to_sequence(text)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm
# hps_ms = utils.get_hparams_from_file("./configs/vctk_base.json")

# net_g_ms = SynthesizerTrn(
#     len(symbols),
#     hps_ms.data.filter_length // 2 + 1,
#     hps_ms.train.segment_size // hps.data.hop_length,
#     n_speakers=hps_ms.data.n_speakers,
#     **hps_ms.model)

def init(symbols, json_dir):
    hps = utils.get_hparams_from_file(json_dir)
    net_g = SynthesizerTrn(
        len(symbols),
        hps.data.filter_length // 2 + 1,
        hps.train.segment_size // hps.data.hop_length,
        **hps.model)
    _ = net_g.eval()
    return net_g, hps

def load_model(model_dir, net_g):
    _ = utils.load_checkpoint(model_dir, net_g, None)


def jtts(text, net_g, hps, dir, length=1):
    stn_tst = get_text(japanese_tokenization_cleaners(text), hps)
    with torch.no_grad():
        x_tst = stn_tst.unsqueeze(0)
        x_tst_lengths = torch.LongTensor([stn_tst.size(0)])
        audio = net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=length)[0][0,0].data.float().numpy()
    sf.write(dir+'/'+text[:10] if len(text) > 10 else text, audio, hps.data.sampling_rate)
