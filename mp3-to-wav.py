#import da lib pydub para manipular áudios
from pydub import AudioSegment

#definindo a função que converte o mp3 para wav
#a função recebe como parâmetro o path do mp3
#o path do output wav
#e o volume em decibéis
def convert(path_mp3, path_wav, volume):
  #criando variavel audio que recebe o arquivo mp3
  audio = AudioSegment.from_mp3(path_mp3)

  #definindo a taxa de amostragem para 16000
  audio = audio.set_frame_rate(16000)

  #definindo o volume a partir do número de decibéis
  audio = audio.apply_gain(volume)

  #exportando o arquivo convertido em wav para o path especificado
  audio.export(path_wav, format="wav")