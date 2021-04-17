#   Falagram is a software that allow userts to listen the telegram chats.
#    Copyright (C) 2020 - Jonathan S. Santos
#
#    Falagram is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Falagram is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Falagram.  If not, see <https://www.gnu.org/licenses/>.
from os import system
from ..app.utils import get_temp_path
from .personality import change_voice


def save(message, lang, samplerate=22000, n_channels=2, file_extension=".mp3"):
    textfile_path = get_temp_path('speech.txt')
    aifffile_path = get_temp_path('speech.aiff')
    audiofile_path = get_temp_path('speech' + file_extension)
    text_file = open(textfile_path, "w")
    text_file.write(message.text)
    text_file.close()
    system("say -f "+ textfile_path + " -o " + aifffile_path)
    system("rm "+ audiofile_path)
    system("rm "+ textfile_path)
    system("ffmpeg -i " + aifffile_path + " " + audiofile_path + " -loglevel quiet")
    try:
        changed_voice_file = change_voice(audiofile_path, message.from_user.id, message.message_id, message.from_user.id)
        return changed_voice_file
    except:
        print("Error to handle with last audiofile")
        return None
