import pulumi
import pulumi_aws as aws

ami_id = "ami-022ce79dc9cabea0c"
key_name = "vockey"

sec_group = aws.ec2.SecurityGroup("web-secgrp",
    description="Permitir acceso SSH y HTTP",
    ingress=[
        {"protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"]},
        {"protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"]}
    ],
    egress=[
        {"protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]}
    ]
)

server = aws.ec2.Instance("cloud9-vm",
    instance_type="t2.micro",
    ami=ami_id,
    key_name=key_name,
    vpc_security_group_ids=[sec_group.id],
    root_block_device={
        "volume_size": 20,
        "volume_type": "gp2"
    },
    tags={"Name": "Investigacion_Grupo1"}
)

pulumi.export("public_ip", server.public_ip)
pulumi.export("public_dns", server.public_dns)
