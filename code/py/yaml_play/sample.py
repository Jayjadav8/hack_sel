import yaml

# Read data from YAML file and convert to dictionary
with open("data.yaml", "r") as file:
    data_dict = yaml.safe_load(file)

print(data_dict)
print(type(data_dict))