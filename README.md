# WavGenerator
Speech generation from text based on Yandex SpeechKit.


## Installation guide:

- install 'pipenv'

`pip install pipenv`
- open the project directory:

`cd WavGenerator`
- create lock file:

`pipenv lock`
- install dependencies:

`pipenv install`

## User guide:

- WavGenerator.py uses argparse. For information about CL args use -h.
- Text for speech generation should be written in one file (default: text.txt) and used as -input flag from CL.
- Wav files would be generated in output_dir (default: wav/) that is set by -output_dir flag from CL.
- Every string in -input would be generated as separate files. Names of these files are set as the number of string in the -input file.

## NOTE: 
It is needed a Yandex Cloud API-key for the script running.
Use your own one or connect with script provider for the key obtaining.
