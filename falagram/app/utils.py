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

from pyrogram import Client
from os import mkdir, sep, getenv, getcwd, remove, listdir
from os.path import dirname, abspath, exists, join

def get_app():
    app = Client("my_account",
    api_id = getenv('FALAGRAM_API_ID'),
    api_hash = getenv('FALAGRAM_API_HASH'))
    return app
def get_root_path():
    current_module_path = abspath(dirname(__file__))
    return dirname(dirname(current_module_path))

def get_temp_path(file_name=None):
    temp_path = join(sep, get_root_path(), "temp")
    if not exists(temp_path):
        mkdir(temp_path)

    # if file_name is None, this function will return the temp folder path
    # else returns the path of the file passed as function arg.
    if file_name:
        return join(sep, temp_path, file_name)
    return temp_path


def get_output_path(file_name):
    output_path = getcwd()
    if file_name:
        return join(sep, output_path, file_name)
    return output_path

def delete_temporary_files():
    files = listdir(get_temp_path())
    for file in files:
        remove(get_temp_path(file))
