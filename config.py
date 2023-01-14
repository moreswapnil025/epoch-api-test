import os
from pathlib import Path

base_uri = 'https://helloacm.com/api/unix-timestamp-converter/?cached'
invalid_base_uri = 'https://helloacm.com/api/unix-timestamp/?cached&s=2020-01-01 16:31:20'
testdata_path = Path.cwd().joinpath('resources','testdata.json')