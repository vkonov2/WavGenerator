
import os
import argparse
from speechkit import model_repository, configure_credentials, creds
from tqdm import tqdm

configure_credentials(
   yandex_credentials=creds.YandexCredentials(
      api_key=''
   )
)

def synthesize(text, output_filename, **kwargs):
   model = model_repository.synthesis_model()

   models = {
   'lea':[],
   'john':[],
   'naomi':['modern', 'classic'],
   'amira':[],
   'madi':[],
   'alena':['neutral','good'],
   'filipp':[],
   'ermil':['neutral','good'],
   'jane':['neutral','good','evil'],
   'madirus':[],
   'omazh':['neutral','evil'],
   'zahar':['neutral','good'],
   'dasha':[],
   'julia':[],
   'lera':[],
   'marina':[],
   'alexander':[],
   'kirill':[],
   'anton':[],
   'nigora':[]}

   if kwargs['voice'] == 'None':
      if kwargs['show']:
         print('>>> no special voice provided')
         print('>>> using the default voice')
      model.voice = 'filipp'
   elif kwargs['voice'] != 'None' and kwargs['role'] == 'None':
      model.voice = kwargs['voice']
      if len(models[model.voice]) > 0:
         if kwargs['show']:
            print('>>> no special role provided')
            print('>>> using the default role')
         model.role = 'neutral' if model.voice != 'naomi' else 'modern'
   else:
      if kwargs['role'] not in models[model.voice]:
         if kwargs['show']:
            print('>>> role '+kwargs['role']+' does not exist for the voice '+model.voice)
            print('>>> using the default role for this voice')
         model.role = 'neutral' if model.voice != 'naomi' else 'modern'
      else:
         model.role = kwargs['role']
   model.speed = kwargs['speed']
   model.volume = kwargs['volume']
   model.pitch_shift = kwargs['pitch']

   result = model.synthesize(text, raw_format=False)
   result.export(output_filename, 'wav')
   if kwargs['show']:
      print('>>> created file: '+output_filename)

def main():

   parser = argparse.ArgumentParser(description='Speech generation script based on Yandex SpeechKit')
   parser.add_argument('-input', type=str, default='text.txt', metavar='text.txt', help='input text file')
   parser.add_argument('-dir', type=str, default='wavs', metavar='wav', help='output wav file')
   parser.add_argument('-warnings', type=bool, default=False, metavar='False', help='show all warnings')
   parser.add_argument('-voice', type=str, default='None', metavar='alena', help='see list of available models in README')
   parser.add_argument('-role', type=str, default='None', metavar='good', help='see list of available roles in README')
   parser.add_argument('-speed', type=float, default=1.0, metavar='1.0', help='change speed of speech')
   parser.add_argument('-volume', type=int, default=-19, metavar='-19', help='regulate normalization level. Volume changes in a range [-145;0), default value is -19.')
   parser.add_argument('-pitch', type=float, default=0., metavar='0.0', help='increase (or decrease) speakers pitch, measured in Hz. Valid values are in range [-1000;1000], default value is 0.')
   args = parser.parse_args()

   os.makedirs(args.dir, exist_ok=True)
   with open(args.input, 'r') as f:
      lines = f.readlines()
      
   for index in tqdm(range(len(lines))): 
      wav_filename = os.path.join(args.dir, str(index+1)+'.wav')
      synthesize(lines[index], wav_filename, show=args.warnings, speed=args.speed, voice=args.voice, role=args.role, volume=args.volume, pitch=args.pitch)

   return 0

if __name__ == '__main__':
   main()







