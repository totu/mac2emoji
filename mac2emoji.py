# -*- coding: utf-8 -*-
import sys
import re


class hex2emoji(object):
    """Class is used to transform hex values to emoji"""
    def __init__(self, start=128000):
        """In init you can set start point for the emoji.

        Args:
            start (int):    Number from which emoji is created using chr().
        """
        self.start = start

    def _hex2emoji(self, hexa):
        """This method is used to transform hex value to emoji

        Args:
            hexa (string):  Hex value (00 - FF).

        Returns char of initialized starting number + hex value.
        """
        num = int("0x%s" % hexa, 16)
        return chr(self.start + num) + " "

    def convert(self, mac):
        """This method is used to detect and convert MAC addresses.

        Args:
            mac (string):   String which may contain MAC address.

        Returns given string with MAC address' hex values changed to emoji.
        """

        regex = re.compile(r'(?:[0-9a-fA-F]:?){12}')
        mac_vals = re.findall(regex, mac)
        if len(mac_vals) > 0:
            if len(mac_vals[0]) is 17:
                mac_vals = mac_vals[0].split(":")
                hexas = [self._hex2emoji(hexa) for hexa in mac_vals]
                for i in range(len(mac_vals)):
                    mac = re.sub(mac_vals[i], hexas[i], mac)
        return mac


if __name__ == "__main__":
    """This makes CLI execution possible.

    By default this file is used by piping in stdout which
    is written out after running it through the convert method.
    """
    h2e = hex2emoji()
    for line in sys.stdin:
        converted = h2e.convert(line)
        sys.stdout.write(converted)
