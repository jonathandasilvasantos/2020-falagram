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

import click
import pickle
import time
import subprocess
from ..app.utils import  get_temp_path, delete_temporary_files
from ..app.validator import validate_message, validate_audiofile
from os import listdir
from os import system

class UserDTO:
    def __init__(self, author_name, author_id):
        self.id = author_id
        self.name = author_name

class MessageDTO:
    def __init__(self, message):
        self.text = message['text']
        self.from_user = UserDTO(message['author_name'], message['author_id'])



@click.command()
@click.option('--language', '-lang', type=click.STRING, default='pt', help='Language of the messages. [pt].')
@click.option('--plim/--no-plim', default=False)
@click.option('--looping/--no-looping', default=False)
def echo(language, plim, looping):
    print("speak aloud")
    
    while True:
        time.sleep(1)
        files = listdir(get_temp_path())
        
        messages = []
        # filter files
        for file in sorted(files):
            if ".msg" in file:

                try:
                    with open(get_temp_path(file),'rb') as infile:
                        data = pickle.load(infile)
                        messages.append(MessageDTO(data))
                        time.sleep(1)
                        system("rm " + get_temp_path(file))

                except Exception as e:
                    print(e)
                

        last_author = ""
        for message in messages:
            if not validate_message(message): continue
            if plim: subprocess.check_call(["afplay", "/Users/bender/falagram/message.mp3"])

            output = message.from_user.name + " disse: "
            if message.from_user.name == last_author:
                output = ""
            last_author = message.from_user.name
            output = output + message.text
            p =subprocess.Popen(['say', output], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.wait()
            



        if not looping:
            break