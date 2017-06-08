#!/usr/bin/env python

import os

from pocketsphinx.pocketsphinx import *
from pocketsphinx import get_model_path

base_dir = os.path.dirname(__file__)

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(base_dir,'data/cmusphinx-en-us-5.2'))
config.set_string('-lm', os.path.join(base_dir, 'data/en-70k-0.2.lm.bin'))
config.set_string('-dict', os.path.join(get_model_path(), 'cmudict-en-us.dict'))
# switch off noisy logging (very useful for debugging when it's not working)
config.set_string('-logfn', '/dev/null')

# config.set_string('-inmic', 'yes')

# Decode streaming data.
decoder = Decoder(config)

# input file must be 16KHz mono for this to work
decoder.start_utt()
stream = open(os.path.join(base_dir, 'data/r_nixon_short.wav'), 'rb')
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
        break
decoder.end_utt()

hypothesis = decoder.hyp()
# logmath = decoder.get_logmath()
print('Best hypothesis: ' + hypothesis.hypstr) # , " model score: ", hypothesis.best_score, " confidence: ", logmath.exp(hypothesis.prob))

# output segments
for seg in decoder.seg():
    print(seg.word + " [" + str(seg.start_frame) + "-" + str(seg.end_frame) + "]")
