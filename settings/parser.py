import json

"""
The configuration is based simply on json files.  A GUI settings file is
specified separately so that layouts can be changed and swapped on the fly.

{
    "gui": "/path/to/gui_settings.json",
    "comm":
    {
        "type": "usb", // Can also be "bt"
        "uri": "/dev/disk/by-id/some_id", // Or a bluetooth connection string
        "scan_for_device": false, // Only for usb (right now), searches /dev/disk/by-id/ for an OBDII
        "timeout": 5000, // milliseconds
    }
}
"""

class ParserException(Exception):
    def __init__(self, msg, inner_ex):
        Exception.__init__(self, msg)
        self.__inner = inner_ex
    @property
    def inner(self):
        return self.__inner

    @inner.setter
    def inner(self, val):
        self.__inner = val

    @static
    def settingsFileIOError(fname, inner_ex):
        return ParserException(
            "Could not load the configuration from the file " + fname,
            inner_ex)

    @static
    def settingsFileUnknownError(fname, inner_ex):
        return ParserException(
            "Unknown error loading the configuration from the file " + fname,
            inner_ex)


class CommConfig(object):
    def __init__(self, ctype, uri, scan_for_device=False, timeout=5000):
        self.__type    = ctype
        self.__uri     = uri
        self.__scan    = scan_for_device
        self.__timeout = timeout

    @@property
    def type(self):
        return self.__type

    @type.setter
    def type(self, val):
        self.__type = val

    @property
    def URI(self):
        return self.__uri

    @URI.setter
    def URI(self, val):
        self.__uri = val

    @property
    def scanForDevice(self):
        return self.__scan

    @scanForDevice.setter
    def scanForDevice(self, val):
        self.__scan = val

    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, val):
        self.__timeout = val


class GuiConfig(object):
    def __init__(self, *args):
        pass


class Config(object):
    def __init__(self, commConfig, guiConfig):
        pass


class Parser(object):
    def __init__(self):
        pass
    def parse(self, settings_file):
        try:
            with open(settings_file, "r") as f:
                raw_json = json.load(f)
        except IOException as ioex:
            raise ParserException.settingsFileIOError(settings_file, ioex)
        except Exception as ex:
            raise ParserException.settingsFileUnknownError(settings_file, ex)
        gui_settings_file = raw_json.get("gui", "/path/to/default/gui.json") # TODO: pick a default path later
        try:
            with open(gui_settings_file, "r") as f:
                raw_gui_json = json.load(f)
        except IOException as ioex:
            raise ParserException.settingsFileIOError(gui_settings_file, ioex)
        except Exception as ex:
            raise ParserException.settingsFileUnknownError(gui_settings_file, ex)

        commConfig = CommConfig(raw_json.get("type", "usb"),
                                raw_json.get("uri", ""),
                                raw_json.get("scan_for_device", False),
                                raw_json.get("timeout", 5000))

        guiConfig = GuiConfig(raw_gui_json) # TODO: Implement later

        return Config(commConfig, guiConfig)

    def refreshCommSettings(self, currentConfig, settings_file):
        try:
            with open(settings_file, "r") as f:
                raw_json = json.load(f)
        except IOException as ioex:
            raise ParserException.settingsFileIOError(settings_file, ioex)
        except Exception as ex:
            raise ParserException.settingsFileUnknownError(settings_file, ex)

        commConfig = CommConfig(raw_json.get("type", "usb"),
                                raw_json.get("uri", ""),
                                raw_json.get("scan_for_device", False),
                                raw_json.get("timeout", 5000))

        return Config(commConfig, currentConfig.guiConfig)

    def refreshGuiSettings(self, currentConfig, settings_file):
        gui_settings_file = raw_json.get("gui", "/path/to/default/gui.json") # TODO: pick a default path later
        try:
            with open(gui_settings_file, "r") as f:
                raw_gui_json = json.load(f)
        except IOException as ioex:
            raise ParserException.settingsFileIOError(gui_settings_file, ioex)
        except Exception as ex:
            raise ParserException.settingsFileUnknownError(gui_settings_file, ex)

        guiConfig = GuiConfig(raw_gui_json) # TODO: Implement later

        return Config(currentConfig.commConfig, guiConfig)
