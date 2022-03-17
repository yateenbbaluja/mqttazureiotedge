import uuid
import sys
from termcolor import colored
from azure.data.tables import TableServiceClient


class saveData:
    def __init__(self):
        self.table_client = None
        self.conn_str = ""
        self.table_service_client = TableServiceClient.from_connection_string(conn_str=self.conn_str)
        self.appid = u"MQTTPoc"
        self.productname = u"HomeAutomation"
        # self.logger = logging.getLogger('azure')
        # self.logger.setLevel(logging.DEBUG)
        # self.handler = logging.StreamHandler(stream=sys.stdout)
        # self.logger.addHandler(self.handler)

    def save_into_table(self, data):
        final_data = self.make_data(data)
        self.send_data_azure_table(final_data)

    def send_data_azure_table(self, data_to_send):
        try:
            self.table_client = self.table_service_client.get_table_client(table_name=data_to_send[1])
            entity = self.table_client.create_entity(entity=data_to_send[0])
            print(colored("Data saved into azure tables:- " + str(entity), "magenta",attrs=['bold']))
        except:
            e = sys.exc_info()[0]
            print(colored("Exception got while saving data to azure tables-:" + str(e), "red",attrs=['bold']))

    def make_data(self, data):
        test = {
            u'PartitionKey': self.appid,
            u'RowKey': str(uuid.uuid4()),
            'EdgeID': data["EdgeID"],
            'DeviceID': data["DeviceID"],
            'Temperature': data["Data"]["Temperature"],
            'Humidity': data["Data"]["Humidity"],
            'Timestamp': data["Timestamp"]
        }
        if data["EdgeID"] == "1891832b-cbca-43ba-9c6b-192660b316a6":
            return [test, "edgetesting"]
        if data["EdgeID"] == "9c2f0f03-5778-4d6b-a6e9-42fa473752e4":
            return [test, "edgetesting"]
