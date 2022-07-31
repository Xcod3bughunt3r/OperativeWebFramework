#!/usr/bin/env python
# The MIT License (MIT).
# Copyright (c) 2022 ALIF-FUSOBAR.
# -*- coding: utf-8 -*-
# description:Search log file from website name

import os,sys

class export_module(object):
	def __init__(self):
		self.export_name = ""     # File Output Name
		self.export_array = []    # exported data 
		self.total_report = False # int numbers of data
		self.module_name = ""     # Current module name (e.g: WHOIS)
		self.extension = "html"       # Output file extension

	def set_export(self,file):
		self.export_name = file

	def set_report(self,value):
		self.export_array = value

	def set_total(self,total_report):
		self.total_report = total_report

	def set_name(self,module_name):
		self.module_name = module_name

	def parse_title(self):
		export_name = self.module_name
		if ":" in export_name:
			export_name= export_name.replace(':', '')
		if '(' in export_name:
			export_name = export_name.replace('(','')
			export_name = export_name.replace(')','')
		export_name = export_name.strip()
		if " " in export_name:
			export_name = export_name.replace(' ', '-')
		self.module_name = export_name

	def begin_file(self):
		self.export_name = "export/" + self.export_name
		# first line of document (if needed).
		file_open = open(self.export_name,"a+")
		html_begin_string = "<!DOCTYPE html><html><head><title>Operative framework - Report</title><style>footer{bottom: 0;margin-top: 10px;font-size: 10px;background: #c15c5c;width: 900px;margin-left: auto;margin-right: auto;color: white;}html{margin:0}body{margin:0;width: 900px;margin-left: auto;margin-right: auto;padding:0}#logo{border-bottom:1px solid black;background-repeat:no-repeat;height:50px;background-image:url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA5wAAAB1CAYAAAAiEe4GAAAACXBIWXMAAAsTAAALEwEAmpwYAAA7XmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMwNjcgNzkuMTU3NzQ3LCAyMDE1LzAzLzMwLTIzOjQwOjQyICAgICAgICAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIKICAgICAgICAgICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIj4KICAgICAgICAgPHhtcDpDcmVhdG9yVG9vbD5BZG9iZSBQaG90b3Nob3AgQ0MgMjAxNSAoTWFjaW50b3NoKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAxNi0wNi0xOVQxNTozMDozMCswMjowMDwveG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDE3LTAxLTE2VDEyOjM2OjMyKzAxOjAwPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcDpNZXRhZGF0YURhdGU+MjAxNy0wMS0xNlQxMjozNjozMiswMTowMDwveG1wOk1ldGFkYXRhRGF0ZT4KICAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9wbmc8L2RjOmZvcm1hdD4KICAgICAgICAgPHBob3Rvc2hvcDpDb2xvck1vZGU+MzwvcGhvdG9zaG9wOkNvbG9yTW9kZT4KICAgICAgICAgPHBob3Rvc2hvcDpUZXh0TGF5ZXJzPgogICAgICAgICAgICA8cmRmOkJhZz4KICAgICAgICAgICAgICAgPHJkZjpsaSByZGY6cGFyc2VUeXBlPSJSZXNvdXJjZSI+CiAgICAgICAgICAgICAgICAgIDxwaG90b3Nob3A6TGF5ZXJOYW1lPiAgIE9QRVJBVElWRSAgICAgRlJBTUVXT1JLIDwvcGhvdG9zaG9wOkxheWVyTmFtZT4KICAgICAgICAgICAgICAgICAgPHBob3Rvc2hvcDpMYXllclRleHQ+ICAgT1BFUkFUSVZFICAgICBGUkFNRVdPUksgPC9waG90b3Nob3A6TGF5ZXJUZXh0PgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6QmFnPgogICAgICAgICA8L3Bob3Rvc2hvcDpUZXh0TGF5ZXJzPgogICAgICAgICA8eG1wTU06SW5zdGFuY2VJRD54bXAuaWlkOjBlNjIxY2Y0LTlkY2QtNDE3Ni05OGNjLTFhMzMyMjI0Y2YzNjwveG1wTU06SW5zdGFuY2VJRD4KICAgICAgICAgPHhtcE1NOkRvY3VtZW50SUQ+YWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOjZjMTRjYzBkLTFjNmUtMTE3YS04MmNmLWEzOTRkZTUyMWFlZjwveG1wTU06RG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD54bXAuZGlkOmY1ZDIzYzkxLWFkYTYtNGRhMS1iNzgwLWRhMGUzM2U3MzdkYjwveG1wTU06T3JpZ2luYWxEb2N1bWVudElEPgogICAgICAgICA8eG1wTU06SGlzdG9yeT4KICAgICAgICAgICAgPHJkZjpTZXE+CiAgICAgICAgICAgICAgIDxyZGY6bGkgcmRmOnBhcnNlVHlwZT0iUmVzb3VyY2UiPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6YWN0aW9uPmNyZWF0ZWQ8L3N0RXZ0OmFjdGlvbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0Omluc3RhbmNlSUQ+eG1wLmlpZDpmNWQyM2M5MS1hZGE2LTRkYTEtYjc4MC1kYTBlMzNlNzM3ZGI8L3N0RXZ0Omluc3RhbmNlSUQ+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDp3aGVuPjIwMTYtMDYtMTlUMTU6MzA6MzArMDI6MDA8L3N0RXZ0OndoZW4+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpzb2Z0d2FyZUFnZW50PkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE1IChNYWNpbnRvc2gpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgICAgPHJkZjpsaSByZGY6cGFyc2VUeXBlPSJSZXNvdXJjZSI+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDphY3Rpb24+c2F2ZWQ8L3N0RXZ0OmFjdGlvbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0Omluc3RhbmNlSUQ+eG1wLmlpZDowZTYyMWNmNC05ZGNkLTQxNzYtOThjYy0xYTMzMjIyNGNmMzY8L3N0RXZ0Omluc3RhbmNlSUQ+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDp3aGVuPjIwMTctMDEtMTZUMTI6MzY6MzIrMDE6MDA8L3N0RXZ0OndoZW4+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpzb2Z0d2FyZUFnZW50PkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE1IChNYWNpbnRvc2gpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjY1NTM1PC9leGlmOkNvbG9yU3BhY2U+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj45MjQ8L2V4aWY6UGl4ZWxYRGltZW5zaW9uPgogICAgICAgICA8ZXhpZjpQaXhlbFlEaW1lbnNpb24+MTE3PC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz5lXG9aAAAAIGNIUk0AAG11AABzoAAA/N0AAINkAABw6AAA7GgAADA+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');background-size:250px}table{font-family:arial,sans-serif;border-collapse:collapse;width:100%;box-shadow:2px 2px 4px #000;border-bottom:2px solid #b2b2b2}td,th{font-size:12px;border:1px solid #ddd;text-align:left;padding:8px}tr{background-color:#ddd}.head{background-color:#fff!important}.space{height:0;border:3px dashed #fff;background:#c55e5e}</style></head><body><div id='logo'></div>"
		file_open.write(html_begin_string)
		file_open.close()
		return True

	def end_file(self):
		# end line of document (if needed).
		file_open = open(self.export_name,"a+")
		string_end = '<footer>(c) operative framework - https://github.com/graniet/operative-framework</footer></body></html>'
		file_open.write(string_end)
		file_open.close()
		return True

	def core_file(self):
		# Core of export process
		if len(self.export_array) > 0:
			current = 0
			string_core = ""
			html_core_string = '<table><tr class="head"><th>'+str(self.module_name)+' ('+str(len(self.export_array))+')</th></tr>'
			file_open = open(self.export_name,"a+")
			for element in self.export_array:
				current = current + 1
				string_core =  string_core + '<tr><td>'+str(element)+'</td></tr>'
			string_core = string_core + '</table><div class="space"></div>'
			file_open.write(html_core_string + string_core)
			file_open.close()
		return True