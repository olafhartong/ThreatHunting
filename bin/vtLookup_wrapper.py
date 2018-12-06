#!/usr/bin/python
# Point the external lookup to this script.
# Replace real_script with the name/location of your script
# This was found on Splunk forums.

import os, sys
for envvar in ("PYTHONPATH", "LD_LIBRARY_PATH"):
    if envvar in os.environ:
        del os.environ[envvar]
python_executable = "/opt/splunk/bin/python"
real_script = "/opt/splunk/etc/apps/ThreatHunting/bin/vtLookup.py"
os.execv(python_executable, [ python_executable, real_script ] + sys.argv[1:])
