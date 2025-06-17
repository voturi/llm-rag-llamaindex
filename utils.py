import os
import yaml

def get_apikey():
    """
    Reads API key from a configuration file.

    This function opens a configuration file named "apikeys.yml", reads the API key for OpenAI

    Returns:
    api_key (str): The OpenAI API key.
    """
    
    # Construct the full path to the configuration file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "apikeys.yml")

    with open(file_path, 'r') as yamlfile:
         yaml_file = yaml.safe_load(yamlfile)
         API_KEY = yaml_file['openai']['api_key']
         return API_KEY


         
    return API_KEY

if __name__ == "__main__":
    print("API_KEY", get_apikey())