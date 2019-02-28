#!/usr/bin/env python3.4

from asterisk.agi import *
import argparse
import re

# Package needs to be fixed: https://github.com/jinglemansweep/PyLMS/issues/15
from pylms.server import Server
from pylms.player import Player


class VerifyMacaddressAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", values[0].lower()):
            sys.stderr.write("Invalid MAC")
            exit(-1)
        else:
            setattr(namespace, self.dest, values)


agi = AGI()

parser = argparse.ArgumentParser(description='Process LMS commands.')
parser.add_argument('player', type=str, nargs=1, help="MAC adress of player", action=VerifyMacaddressAction)
parser.add_argument('command', type=str, nargs=1, default="mode",
                    choices=['mode', 'start', 'stop', 'toggle', 'pause', 'unpause'],
                    help='Command to execute on LMS player')

args = parser.parse_args()

sc = Server(hostname="lms.wi.kettenbach-it.de", port=9090)
sc.connect()
sq = sc.get_player(args.player[0])  # type: Player

if sq is None:
    sys.stderr.write("Player not found")
    exit(-1)

if args.command[0] == "mode":
    #agi.set_variable("LMSSTATUS", str(sq.get_mode()))
    # agi_set_varaible is broken: https://github.com/rdegges/pyst2/issues/19
    print("SET VARIABLE LMSSTATUS " + sq.get_mode())

if args.command[0] == "stop":
    sq.stop()

if args.command[0] == "start":
    sq.play()

if args.command[0] == "toggle":
    sq.toggle()

if args.command[0] == "pause":
    sq.pause()

if args.command[0] == "unpause":
    sq.unpause()
