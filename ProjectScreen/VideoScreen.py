import subprocess as subp
from os.path import join
  
log_dir = 'C:\\Users\\JavaCode\\Documents\\python\\ProjectScreen\\' # путь куда положить файл с записью
CORE_DIR = 'C:\\Users\\JavaCode\\Documents\\python\\ProjectScreen\\' # путь где лежит ffmpeg.exe
video_file = join(log_dir, 'video_' + '.flv')
FFMPEG_BIN = join(CORE_DIR, 'ffmpeg\\bin\\ffmpeg.exe')
  
command = [
    FFMPEG_BIN,
    '-y',
    '-loglevel', 'error',
    '-f', 'gdigrab',
    '-framerate', '12',
    '-i', 'desktop',
    '-s', '960x540',
    '-pix_fmt', 'yuv420p',
    '-c:v', 'libx264',
    '-profile:v', 'main',
    '-fs', '50M',
    video_file
]
ffmpeg = subp.Popen(command, stdin=subp.PIPE, stdout=subp.PIPE, stderr=subp.PIPE)
