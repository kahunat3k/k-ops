
import subprocess
import base64 
import os

from utils.git_hub import STGithub

# res = subprocess.run(['datamodel-codegen', '--input', './research/aws_s3.yml'],
#                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# print(res.stdout)

# for line in bytes.decode(res.stdout).split('/n'):

#     print(line)


class DynModel():

    def __init__(self, id_session: str, resource_name: str) -> None:

        self.git = STGithub()
        self.prefix_session = id_session
        self.prefix_name = resource_name
        self.repo_name = 'kahunat3k/k-ops/yaml'

    def load_schema(self) -> None:

        self.git.getfile(prefix=self.prefix_name)

        tf = open('./tmp/'+self.prefix_session+'_'+self.prefix_name+'.yml','+w')

        tf.write(bytes.decode(base64.b64decode(self.git.contents.content)))
        tf.flush()

    def gen_datamodel(self) -> None:

        class_model_name = self.prefix_session+'_'+self.prefix_name
        
        res = subprocess.run(['datamodel-codegen', '--input', 
                    './tmp/'+ class_model_name+'.yml' ],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        class_model = open('./model/'+class_model_name+'.py','+w')

        class_model.write(bytes.decode(res.stdout))

        class_model.flush()

        os.remove('./tmp/'+ class_model_name+'.yml')

        self.data_model = bytes.decode(res.stdout)

# # Init app
# if __name__ == '__main__':

#     ob = DynModel(id_session='9d93163b-df71-43c2-97d8-06035e7027cb', resource_name='s3')

#     ob.load_schema()

#     ob.gen_datamodel()

#     print(ob.data_model)
