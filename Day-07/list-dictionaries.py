ec2_instances_info = [
    {
        "id": "instance-001",
        "type": "t2-micro"
    },
    {
        "id": "instance-002",
        "type": "t2-xlarge"
    },
    {
        "id": "instance-003",
        "type": "t3-medium" 
    }
]

print(ec2_instances_info[2]["type"])