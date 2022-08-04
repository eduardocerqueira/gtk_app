import gi
from datetime import datetime

gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')

from gi.repository import Gtk
from gi.repository import Notify

_GTK_APP_TITLE = "GTK Python App"


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=_GTK_APP_TITLE, window_position=Gtk.WindowPosition.CENTER_ALWAYS)
        Gtk.Window.set_default_size(self, 640, 480)
        Notify.init(_GTK_APP_TITLE)

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button = Gtk.Button(label="Click Here")
        self.button.set_halign(Gtk.Align.CENTER)
        self.button.set_valign(Gtk.Align.CENTER)
        self.button.connect("clicked", self.send_notification)
        self.box.pack_start(self.button, True, True, 0)



    def send_notification(self, widget):
        n = Notify.Notification.new(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), _GTK_APP_TITLE, "*")
        n.show()


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
