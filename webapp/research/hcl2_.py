import hcl2
from yaml import load

from utils.git_hub import STGithub
from utils.operations import ToolBox

git_hub = STGithub()
toolbox = ToolBox()

git_hub.getitemcontent('tfbase','kahunat3k/k-ops')

def main():

    with open('./checkout/staging.tfvars','r') as file_tf:

        dict_data = hcl2.load(file_tf)

        print(dict_data)

if __name__ == "__main__":

    main()