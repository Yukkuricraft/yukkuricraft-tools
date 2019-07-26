import os
import re
import sys
import datetime

config = {
    '6h': 4 * 7, // one week
    '1w': 4 * 4, // 4 months
    '6m': 4, // 2 years
}

def parseConfField(config_field):
    num = `config_field`[0]
    // to delta epoch
