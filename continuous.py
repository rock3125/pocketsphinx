#!/usr/bin/env python

import os
from pocketsphinx import LiveSpeech, get_model_path

# use this little utility to continuously convert speech from the mic
# to text

base_dir = os.path.dirname(__file__)

if __name__ == '__main__':

    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        hmm=os.path.join(base_dir, os.path.join(base_dir,'data/cmusphinx-en-us-5.2')),
        lm=os.path.join(base_dir, 'data/en-70k-0.2.lm.bin'),
        dic=os.path.join(get_model_path(), 'cmudict-en-us.dict')
    )

    print("start talking, I'm listening.  Say \"stop\" to stop this program.")
    for phrase in LiveSpeech():
        phrase_str = str(phrase)
        print(phrase_str)
        if phrase_str == "stop" or phrase_str == "stop it":
            break
