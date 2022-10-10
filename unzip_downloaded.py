import tarfile
from pathlib import Path

from tqdm import tqdm

input_dir = Path("/project/sourcedata/Package_1195698/fmriresults01")

for zipped_file in tqdm(input_dir.glob("*baselineYear1Arm1*.tgz")):
    try:
        with tarfile.open(zipped_file) as tar:
            
            import os
            
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar, path="/project/rawdata/")
    except:
        print(zipped_file)