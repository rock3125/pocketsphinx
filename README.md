### Ubuntu 16.04/17.04 installation

First install the required apt dependencies
```
sudo apt install pocketsphinx swig libpulse-dev
```
and then continue with the pocketsphinx python wrapper
```
pip install --upgrade pocketsphinx
```

### Howto
Converting a text apra model to binary
`sphinx_lm_convert -i model.lm -o model.lm.bin`
