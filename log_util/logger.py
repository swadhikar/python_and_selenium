"""Create log and give it to the user to make use of logging through variable log"""
import logging
import sys

log = logging.getLogger("python_practise")

# Set logging level to the lowest
log.setLevel(logging.DEBUG)

# Set the formatting to console output capture
default_formatter = logging.Formatter('%(asctime)-15s: %(levelname)-5s - %(message)s')
__stream_handle = logging.StreamHandler(sys.stdout)
__stream_handle.setLevel(logging.DEBUG)
__stream_handle.setFormatter(default_formatter)
log.addHandler(__stream_handle)
