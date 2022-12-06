from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    service_name: str
    graylog_address: str
    graylog_port: int
    amqp_connection_string: str

    class Config:
        env_prefix = ""
        case_sensitive = False
        fields = {
            'service_name': {
                'env': 'SERVICE_NAME',
            },
            'graylog_address': {
                'env': 'GRAYLOG_ADDRESS',
            },
            'graylog_port': {
                'env': 'GRAYLOG_PORT'
            },
            'amqp_connection_string': {
                'env': 'AMQP_CS'
            }
        }


app_config = AppSettings()
