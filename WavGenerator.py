
import os
import argparse
from speechkit import model_repository, configure_credentials, creds

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
      print('>>> no special voice provided')
      print('>>> using the default voice')
      model.voice = 'filipp'
   elif kwargs['voice'] != 'None' and kwargs['role'] == 'None':
      model.voice = kwargs['voice']
      if len(models[model.voice]) > 0:
         print('>>> no special role provided')
         print('>>> using the default role')
         model.role = 'neutral' if model.voice != 'naomi' else 'modern'
   else:
      if kwargs['role'] not in models[model.voice]:
         print('>>> role '+kwargs['role']+' does not exist for the voice '+model.voice)
         print('>>> using the default role for this voice')
         model.role = 'neutral' if model.voice != 'naomi' else 'modern'
      else:
         model.role = kwargs['role']

   result = model.synthesize(text, raw_format=False)
   result.export(output_filename, 'wav')
   print('>>> created file: '+output_filename)

def main():

   models_info = 'Model of voices and roles:\n'
   models_info += '\t- german  - lea       - female\n'
   models_info += '\t- english - john      - male\n'
   models_info += '\t- hebrew  - naomi     - female - modern\n'
   models_info += '\t                               - classic\n'
   models_info += '\t- kazakh  - amira     - female\n'
   models_info += '\t- kazakh  - madi      - male\n'
   models_info += '\t- russian - alena     - female - neutral\n'
   models_info += '\t                               - good\n'
   models_info += '\t- russian - filipp    - male\n'
   models_info += '\t- russian - ermil     - male   - neutral\n'
   models_info += '\t                               - good\n'
   models_info += '\t- russian - jane      - female - neutral\n'
   models_info += '\t                               - good\n'
   models_info += '\t                               - evil\n'
   models_info += '\t- russian - madirus   - female\n'
   models_info += '\t- russian - omazh     - male   - neutral\n'
   models_info += '\t                               - evil\n'
   models_info += '\t- russian - zahar     - male   - neutral\n'
   models_info += '\t                               - good\n'
   models_info += '\t- russian - dasha     - female\n'
   models_info += '\t- russian - julia     - female\n'
   models_info += '\t- russian - lera      - female\n'
   models_info += '\t- russian - marina    - female\n'
   models_info += '\t- russian - alexander - male\n'
   models_info += '\t- russian - kirill    - male\n'
   models_info += '\t- russian - anton     - male\n'
   models_info += '\t- uzbek   - nigora    - female\n'

   parser = argparse.ArgumentParser(description='Speech generation script based on Yandex SpeechKit')
   parser.add_argument('-input', type=str, default='text.txt', metavar='text', help='input text file')
   parser.add_argument('-output_dir', type=str, default='wavs', metavar='wav', help='output wav file')
   parser.add_argument('-voice', type=str, default='None', metavar='voice', help=models_info)
   parser.add_argument('-role', type=str, default='None', metavar='role', help=models_info)
   args = parser.parse_args()

   os.makedirs(args.output_dir, exist_ok=True)
   index = 1
   with open(args.input, 'r') as f:
      line = f.readline()
      wav_filename = os.path.join(args.output_dir, str(index)+'.wav')
      synthesize(line, wav_filename, voice=args.voice, role=args.role)
      index += 1

   return 0

if __name__ == '__main__':
   main()







