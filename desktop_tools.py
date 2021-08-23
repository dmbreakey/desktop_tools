import psutil
from os import system

class desktop:
    def __init__(self):
        self.desktops = {
            'gnome':
                { 'process': 'gnome-session',
                  'gsettings-power-leaf': 'org.gnome.settings-daemon.plugins.power',
                  'gsettings-power-key': 'sleep-inactive-ac-timeout' },
            'cinnamon':
                { 'process': 'cinnamon-session',
                  'gsettings-power-leaf': 'org.cinnamon.settings-daemon.plugins.power',
                  'gsettings-power-key': 'sleep-inactive-ac-timeout' }
            }
        self.user_name = 'david'
        self.desktop = self.identify()
        self.dbus_address = None
        if self.desktop:
            self.desktop_pids = self.findPidByName(self.desktops[self.desktop]['process'])
            self.desktop_environment = self.desktop_pids[0].environ()
            if 'DBUS_SESSION_BUS_ADDRESS' in self.desktop_environment:
                self.dbus_address = self.desktop_environment['DBUS_SESSION_BUS_ADDRESS']
        else:
            self.desktop_environment = None
            self.desktop_pids = None
        return

    def identify(self):
        for desktop in self.desktops:
            if self.findPidByName(self.desktops[desktop]['process']) != None:
                return desktop
        return None

    def findPidByName(self, process_name):
        '''
        Get a list of all PIDs for all processes containing
        the given name.
        '''
        process_name = process_name.lower()
        processObjects = [ process for process in psutil.process_iter() if process_name in process.name().lower() ]
        if len(processObjects) > 0:
            return processObjects
        else:
            return None

    def setSleep(self, duration=600):
        if self.dbus_address:
            if self.desktop:
                node = self.desktops[self.desktop]
                system(f"gsettings set {node['gsettings-power-leaf']} {node['gsettings-power-key']} {duration}")
