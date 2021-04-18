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
from ..provider.speech import save
from ..provider.composer import compose
from ..commands.listen import save_message
from ..app.utils import get_app, get_temp_path, get_output_path, delete_temporary_files
from ..app.validator import validate_message, validate_audiofile
from ..app.search import search_chat
from os import listdir
import os

@click.command()
@click.argument('chatname')
@click.option('--chatid', '-id', default=0, help='ID of Chat. You don\'t now the ID? Run: falagram chats')
@click.option('--limit', '-l', default=25, required=False, help='Numer of messages [25].')
@click.option('--language', '-lang', type=click.STRING, default='pt', help='Language of the messages. [pt].')
@click.option('--outputfilename', '-o', type=click.STRING, default='result.mp3', help='Name of the output file. [result.mp3]')
@click.option('--replay/--no-replay', default=False)
def history(chatname, chatid, limit, language, outputfilename, replay):
    delete_temporary_files()
    app = get_app()
    with app:
        if chatid == 0:
            if len(chatname) == 0:
                print("You must pass a chat name or chat ID!")
                exit(1)
            else:
                chatid = search_chat(app, chatname)
                if chatid is None:
                    print("Chat not found :()")
                    exit(1)



        messages = []
        for index, message in enumerate(app.iter_history(chat_id=chatid)):
            if len(messages) >= limit:
                break

            print("Fetching messages... ( " + str(index+1) + "/" + str(limit) + " )")
            messages.append(message)

    messages.reverse()
    audio_files = []
    
    if replay:
        for message in messages:
            save_message(message)
        return

    for index, message in enumerate(messages):
        print("Text-to-Speech proccess... ( " + str(index+1) + "/" + str(len(messages)) + " )")
        if not validate_message(message): continue
        saved_file = save(message, lang=language)
        if saved_file: audio_files.append(saved_file)

    if len(audio_files) > 0:
        print("Composing the final track")
        result = compose(audio_files, get_output_path(outputfilename))

        print("Removing temporary files...")
        delete_temporary_files()

        if validate_audiofile(result):
            print("Done! Created the final track at: ! + result")
        else:
            print("Error :()")
