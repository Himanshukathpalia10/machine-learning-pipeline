
import os


SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
API_KEY ="AZ2IWQAXNC5A47AE"#os.getenv('API_KEY',None)
ENDPOINT_SCHEMA_URL  ="https://psrc-kjwmg.ap-southeast-2.aws.confluent.cloud"#os.getenv('ENDPOINT_SCHEMA_URL',None)
API_SECRET_KEY = "tFkk5R3f9sgPN+EW4In8IxYDAFVf+ynQvAM0K2jWOFAzs3gy/mxUh3/zaUh9uAil"#os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER ="pkc-6ojv2.us-west4.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)
# SECURITY_PROTOCOL = #os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SCHEMA_REGISTRY_API_KEY ="HMDCXAUZYXGLBILT" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET ="QBshr5EXJEntP1BEeI+eXCanssczkhJX4LUnQz4h5KiM5kkkiCU8NLOlTyfekSUT" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

