#!/usr/bin/env python
from foodwatch.pollocubaBot import PolloBot
import sys

bot = PolloBot()
bot.posttry(sys.argv[1])