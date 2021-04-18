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
from os.path import exists
from ..app.utils import get_app, get_temp_path, delete_temporary_files
from ..app.validator import validate_message, validate_audiofile
from ..app.search import search_chat

def save_message(message):
    if not validate_message(message): return

    #saved_file = save(message, lang=language)
    messagefilename = str(round(time.time() * 1000)) + ".msg"
    messagefilepath = get_temp_path(messagefilename)
    while exists(messagefilepath):
        messagefilename = str(round(time.time() * 1000)+1) + ".msg"
        messagefilepath = get_temp_path(messagefilename)
    try:
        name = "anonymous"
        if message.from_user:
            if message.from_user.first_name:
                name = message.from_user.first_name
            if message.from_user.last_name:
                name = name + " " + message.from_user.last_name                    
                
        data = dict()
        data['author_id'] = message.from_user.id
        data['author_name'] = name
        data['text'] = message.text
        with open(messagefilepath,'wb') as outfile:
            pickle.dump(data, outfile)
            print("saved: " + messagefilename)
    except Exception as e:
        print(e)
    

@click.command()
@click.argument('chatname')
@click.option('--language', '-lang', type=click.STRING, default='pt', help='Language of the messages. [pt].')
def listen(chatname, language):
    delete_temporary_files()



    app = get_app()

    @app.on_message()
    def messages_stream(client, message):
        label = message.chat.first_name or message.chat.title
        if label is None: return
        if not chatname.lower() in label.lower(): return
        
        save_message(message)

        
    app.run()
