# ThreatHunting | A Splunk app mapped to MITRE ATT&CK to guide your threat hunts

[![license](https://img.shields.io/github/license/olafhartong/ThreatHunting.svg?style=flat-square)](https://github.com/olafhartong/ThreatHunting/blob/master/license.md)
![Maintenance](https://img.shields.io/maintenance/yes/2018.svg?style=flat-square)
[![GitHub last commit](https://img.shields.io/github/last-commit/olafhartong/ThreatHunting.svg?style=flat-square)](https://github.com/olafhartong/ThreatHunting/commit/master)

This is a Splunk application containing several dashboards and over 100 reports that will facilitate intital hunting indicators to investigate.

**Note:**
This application is not a magic bullet, it will require tuning and real investigative work to be truly effective in your environment.
Try to become best friends with your system administrators. They will be able to explain a lot of the initially discovered indicators.

Big credit goes out to [MITRE](https://attack.mitre.org) for creating the ATT&CK framework!

Pull requests / issue tickets and new additions will be greatly appreciated!

## Mitre ATT&CK

A current ATT&CK navigator export of mapped searches will be added soon.

### Prerequisites

Install the following apps to your SearchHead:

- [Punchcard Visualization](https://splunkbase.splunk.com/app/3129/)
- [Force Directed Visualization](https://splunkbase.splunk.com/app/3767/)
- [Sankey Diagram Visualization](https://splunkbase.splunk.com/app/3112/)
- [Lookup File Editor](https://splunkbase.splunk.com/app/1724/)

## Required actions after deployment

- Make sure the threathunting index is present on your indexers
- Edit the macro's to suit your environment (leaving it to * is not recommended, it will take a lot more resources)  > https://YOURSPLUNK/en-US/manager/ThreatHunting/admin/macros
- The app is shipped without whitelist lookup files, you'll need to create them yourself. This is so you won't accidentally overwrite them on an upgrade of the app.
