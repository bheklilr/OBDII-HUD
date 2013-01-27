"""
OBD2 Module
"""

class Command(object):
    def __init__(self, cmd, description=""):
        self.__cmd = ""
        self.command = cmd
        self.__name = self.__class__.__name__
        self.__desc = description

    @property
    def command(self):
        return self.__cmd

    @command.setter
    def command(self, cmd):
        if isinstance(cmd, Command):
            self.__cmd = cmd.command
        elif isinstance(cmd, str):
            self.__cmd = cmd

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__desc

    @description.setter
    def description(self, val):
        self.__desc = val


class OBD2(object):
    def __init__(self, **kwargs):
        pass

    def connect(self, **kwargs):
        pass

    def disconnect(self, **kwargs):
        pass

    def sendCommand(self, cmd):
        pass

    def read(self):
        pass

    def deviceName(self):
        pass

