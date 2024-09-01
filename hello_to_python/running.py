#!/usr/bin/env python3

import os

stage = os.environ.get('STAGE', 'dev').upper()

output = f"We're running in {stage}"

if stage.startswith('PROD'):
    output = "DANGER!!! - " + output

print(output)