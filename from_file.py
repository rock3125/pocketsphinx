#!/usr/bin/env python

import os
import sys

from pocketsphinx.pocketsphinx import *
from pocketsphinx import get_model_path

base_dir = os.path.dirname(__file__)

if __name__ == '__main__':

    if len(sys.argv) == 2:
        sound_file = sys.argv[1]

        # Create a decoder with certain model
        config = Decoder.default_config()
        config.set_string('-hmm', os.path.join(base_dir,'data/cmusphinx-en-us-5.2'))
        config.set_string('-lm', os.path.join(base_dir, 'data/en-70k-0.2.lm.bin'))
        config.set_string('-dict', os.path.join(get_model_path(), 'cmudict-en-us.dict'))
        # switch off noisy logging (very useful for debugging when it's not working)
        config.set_string('-logfn', '/dev/null')

        # Decode streaming data.
        decoder = Decoder(config)

        # input file must be 16KHz mono for this to work
        decoder.start_utt()
        stream = open(os.path.join(base_dir, sound_file), 'rb')
        while True:
            buf = stream.read(1024)
            if buf:
                decoder.process_raw(buf, False, False)
            else:
                break
        decoder.end_utt()

        # output decoded text for the entire file
        print(decoder.hyp().hypstr)

        # output segments with start frames (default frame rate = 100 fps) for each
        segment_list = []
        first_frame = -1
        for seg in decoder.seg():
            if first_frame == -1:
                first_frame = seg.start_frame
            orig_num = (seg.start_frame - first_frame)
            num = orig_num / 100
            mins = int(num / 60)
            secs = int(num % 60)
            time_str = '%s.%s:%s' % (mins, str(secs).zfill(2), str(orig_num % 100).zfill(2))
            segment_list.append(seg.word + "/" + time_str)
        print(segment_list)

    else:
        print("takes one parameter: /path/to/16KHz mono wav file.wav")
