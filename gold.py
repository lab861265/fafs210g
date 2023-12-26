from typing import Dict, Tuple
import os
import subprocess
import argparse

subprocess.call([ 'pip', 'install' , 'inquirer', '-q' ])

import inquirer

features : Dict[str, str] = \
{
	'theme': 'gold_edition/theme.patch',
	'ghost_swappers': 'gold_edition/ghost_swappers.patch',
	'target_download': 'gold_edition/target_download.patch',
	'hls_webcam_mode': 'gold_edition/hls_webcam_mode.patch'
}

parser = argparse.ArgumentParser()
parser.add_argument('-y', action='store_true')
args = parser.parse_args()

if args.y:
	answers =\
	{
		'features': list(features.keys())
	}
else:
	questions =\
	[
		inquirer.Checkbox('features', message = 'select features to install', choices = features.keys())
	]
	answers = inquirer.prompt(questions)

for feature in answers['features']:
	patch_file = features[feature]
	if os.path.exists(patch_file):
		try:
			subprocess.run([ 'git', 'apply', patch_file, '--whitespace', 'nowarn' ])
			print('Feature "' + feature + '" installed successfully.')
		except Exception:
			print('Something went wrong!')
	else:
		print('Patch file ' + patch_file + ' could not be found.')
