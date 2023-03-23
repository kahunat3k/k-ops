
from importlib import import_module

from PIL import Image


# diagram.py
from diagrams import Diagram, Cluster
from diagrams.aws.storage import S3
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53, APIGateway

import json

from diagram.aws import s3

class GraphView():

    def __init__(self) -> None:
        pass

    def make_diagram(self, cloud: str, resources: list, data_json: dict):

        graph_attr = {
            "fontsize": "12",
            "bgcolor": "transparent",
            "pad":"3.0",
            "ranksep": "1"
            }

        
        node_attr = {
            "fontsize": "12",
             "pad":"1.75"
            }

        
        with Diagram("SREOps",show=True, filename=f"{cloud}", outformat="png", direction="LR",graph_attr=graph_attr,node_attr=node_attr):

            with Cluster(f"{data_json[0]['main']['environments']}"):
                
                dns = Route53(
                label=f"{data_json[0]['main']['product']}-{data_json[0]['main']['environments'].lower()}.smartfit.cloud")

                elb = ELB(label=f"elb")

                with Cluster(f"{data_json[0]['main']['product']}"):
                    
                    apigw = APIGateway("apigw")

                    aws_resources = []

                    for item in resources:

                        aws_resources.append(
                            eval(f"{item.lower()}.{item.lower()}_resource('{item.lower()}')"))


            dns >> elb >> apigw >> aws_resources
