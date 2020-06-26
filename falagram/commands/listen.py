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
from ..app.utils import get_app, get_temp_path, delete_temporary_files
from ..app.validator import validate_message, validate_audiofile
from ..app.search import search_chat
from pygame import mixer  # Load the popular external library

@click.command()
@click.argument('chatname')
@click.option('--language', '-lang', type=click.STRING, default='pt', help='Language of the messages. [pt].')
def listen(chatname, language):
    delete_temporary_files()



    mixer.init()

    app = get_app()

    @app.on_message()
    def messages_stream(client, message):
        label = message.chat.first_name or message.chat.title
        if label is None: return
        if not chatname.lower() in label.lower(): return

        if not validate_message(message): return


        saved_file = save(message, lang=language)
        if validate_audiofile(saved_file):
            mixer.music.load(saved_file)
            mixer.music.play()
    app.run()
