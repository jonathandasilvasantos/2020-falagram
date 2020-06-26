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
import sox
from ..app.utils import get_temp_path
from random import randint, random, seed

def change_voice(audiofile_path, user_id, message_id, samplerate=22000, n_channels=2, file_extension=".mp3"):

    tfm = sox.Transformer()
    tfm.pitch(randint(-3, 3))
    tfm.overdrive(randint(0, 10))
    tfm.flanger(randint(0, 4))
    tfm.phaser(random())
    tfm.bass(randint(-10,10))
    tfm.treble(randint(-10,10))
    tfm.norm()
    tfm.convert(samplerate=samplerate, n_channels=n_channels)

    output_path = get_temp_path(str(message_id) + file_extension)
    tfm.build(audiofile_path, output_path)
    return output_path
