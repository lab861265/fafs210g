METADATA =\
{
	'name': 'FaceFusion',
	'description': 'Next generation face swapper and enhancer',
	'version': '2.1.0',
	'license': 'MIT',
	'author': 'Henry Ruhs',
	'url': 'https://facefusion.io'
}
METADATA['version'] = METADATA['version'] + ' Gold Edition'


def get(key : str) -> str:
	return METADATA[key]
