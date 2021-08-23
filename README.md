# desktop_tools
Various tools I've written to facilitate using my personal desktop

desktop_tools.py is a Python class object I use to manage various Linux desktop settings;
right now, all it manages is detecting gnome and cinnamon, and setting sleep durations for
both.

A helper script, tied with a SystemD unit, manages determining what it should set according
to whether I'm supposed to be working or not, when the system resumes from sleep.
