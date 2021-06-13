import tarfile
from pathlib import Path

from tqdm import tqdm

input_dir = Path("/project/sourcedata/Package_1189145/fmriresults01")

for zipped_file in tqdm(input_dir.glob("*baselineYear1Arm1*.tgz")):
    try:
        with tarfile.open(zipped_file) as tar:
            tar.extractall(path="/project/rawdata/")
    except:
        print(zipped_file)