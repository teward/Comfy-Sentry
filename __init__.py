import json
import os.path

import sentry_sdk

from ._util.log import log

__version__ = '1.0.0'
__author__ = 'Thomas Ward <teward@thomas-ward.net>'
__copyright__ = 'Copyright 2024'
__license__ = "GPL-3.0"


THIS_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(THIS_DIR, 'sentry_config.json')) as f:
        sentry = json.load(f)
    log("Sentry integration active.", color="CYAN")
except FileNotFoundError:
    log("No sentry_config.json file found, please create it from sentry_config.example.json and "
        f"make sure that file is present in {THIS_DIR}, then relaunch ComfyUI.", color="BRIGHT_RED", style="BOLD")
    raise RuntimeError("Missing sentry_config.json file")

# noinspection HttpUrlsUsage
sentry_sdk.init(
    f"{'https://' if sentry['https'] is True else 'http://'}{sentry['key']}@{sentry['host']}/{sentry['project']}",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for Tracing.
    # We recommend adjusting this value in production.
    enable_tracing=sentry['enable_tracing'],
    traces_sample_rate=sentry['sample_rate']
)

NODE_CLASS_MAPPINGS = {}

__all__ = ['NODE_CLASS_MAPPINGS']