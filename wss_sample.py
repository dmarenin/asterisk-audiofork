import sys
from websocket_server import WebsocketServer


def new_client(self, client, server):
    pass

def client_left(self, client, server):
    pass

def message_received(self, client, server, message):
    if message[:3]==b'SIP':
        client['channel'] = message.decode()
        client['frames'] = []
        client['last_offset_read'] = 0

        server.client_channels[client['channel']] = client

        return

    if not client.get('channel') is None:
        client['frames'].append(message)

        #print(message)

        #f = open('audio.raw', 'ab')
        #f.write(message)
        #f.close()
		
		
ws_server = WebsocketServer(WS_PORT, HOST)

ws_server.client_channels = {}

ws_server.set_fn_client_left(self.client_left)
ws_server.set_fn_message_received(self.message_received)
ws_server.set_fn_new_client(self.new_client)

ws_server.run_forever()

