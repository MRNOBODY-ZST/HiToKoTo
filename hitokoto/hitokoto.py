import requests
import json
from mcdreforged.api.decorator import *
from mcdreforged.api.types import PluginServerInterface,CommandSource,Info
from mcdreforged.api.rtext import *
from mcdreforged.api.command import Literal


hitokoto_url = "https://v1.hitokoto.cn"


@new_thread("HiToKoTo - Say")
def say_hitokoto(src:CommandSource):
    hitokoto_sentence = requests.get(hitokoto_url).text
    hitokoto_sentence = json.loads(hitokoto_sentence)
    hitokoto_sentence = hitokoto_sentence["hitokoto"]
    src.reply(RText("今日一言：",color=RColor.gold)+hitokoto_sentence)


@new_thread("HiToKoTo - Help")
def help_message(src: CommandSource):
    src.reply(RText("!!hitokoto 显示一言",color=RColor.green))
    src.reply(RText("!!hitokoto help 显示帮助信息",color=RColor.green))


def register_command(server:PluginServerInterface):
    server.register_command(
            Literal('!!hitokoto').runs(lambda src:say_hitokoto(src))
                .then(
                Literal({"help"})
                    .runs(lambda src:help_message(src))
            )
    )


def on_load(server: PluginServerInterface,old):
    register_command(server)


def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    hitokoto_sentence = requests.get(hitokoto_url).text
    hitokoto_sentence = json.loads(hitokoto_sentence)
    hitokoto_sentence = hitokoto_sentence["hitokoto"]
    server.tell(player=player,text=hitokoto_sentence)