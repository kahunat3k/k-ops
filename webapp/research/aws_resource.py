import subprocess
from utils.git_hub import STGithub

res = subprocess.run(['datamodel-codegen','--input','./research/aws_s3.yml'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

print(res.stdout)

for line in bytes.decode(res.stdout).split('/n'):

    print(line)


class DynModel():

    def __init__(self) -> None:
        pass

    def load_schema(self, name:str) -> None:
        pass
    
    def gen_datamodel(self) -> None:
        pass

    def import_datamodel(self,name:str) -> None:
        pass

    def pull_datamodel(self, name:str) -> None:
        pass


