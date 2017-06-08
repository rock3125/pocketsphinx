### Ubuntu 16.04/17.04 installation

First install the required apt dependencies
```
sudo apt install pocketsphinx swig libpulse-dev
```
setup your Python 3.5/3.6 environment and install the dependencies.
```
pip install -r requirements.txt
```

### Howto
Converting a text apra model to binary
`sphinx_lm_convert -i model.lm -o model.lm.bin`
