import json
import yaml
import datetime
import base64

class ToolBox():

    def __init__(self) -> None:
        
        pass

    def byaml_2_dict(self, content:bytes) ->dict:

        return yaml.safe_load(bytes.decode(base64.b64decode(content)))

    def yaml_2_dict(self, content:str)->dict:

        return yaml.safe_load(content)




