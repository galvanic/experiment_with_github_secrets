
import yaml
from pprint import pprint as pretty_print

with open('credentials.yaml', 'r') as ifile:
    CREDENTIALS = yaml.load(ifile, Loader=yaml.FullLoader)

pretty_print(CREDENTIALS)
