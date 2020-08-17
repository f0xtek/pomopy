import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')

from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Notify


class Notifier(GObject.Object):
    def __init__(self):
        super(Notifier, self).__init__()
        Notify.init("Pomopy")

    @staticmethod
    def send_notification(title, text, file_path_to_icon=""):
        n = Notify.Notification.new(title, text, file_path_to_icon)
        n.set_timeout(10000)
        n.set_urgency(1)
        n.show()


def notify(message):
    print(message)
    # Might not be running GTK!
    if Gtk.MAJOR_VERSION is not None:
        notifier = Notifier()
        notifier.send_notification("Pomopy", message)
