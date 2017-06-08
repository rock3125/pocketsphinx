### Ubuntu 16.04/17.04 installation

First install the required apt dependencies
```
sudo apt install pocketsphinx swig libpulse-dev
```
and then continue with the pocketsphinx python wrapper
```
pip install --upgrade pocketsphinx
```

Download latest LM and HMM from
```
https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/US%20English/
```
The HMM is the `cmusphinx-en-us-5.2.tar.gz` file (which needs to be extracted to use)
The LM is the `en-70k-0.2.lm.gz` file.

Converting a text apra model to binary
`sphinx_lm_convert -i model.lm -o model.lm.bin`
