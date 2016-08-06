#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import argparse
import sys
import signal

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code" +str(rc))
    # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Topic: ", msg.topic+'\nMessage: '+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('-H', '--host', dest='tgtHost', type=str, help='specify target host')
        parser.add_argument('-f', '--filename', dest='tgtfile', type=str, help='specify file name to write data to') 
        
        options = parser.parse_args()
        tgtHost = options.tgtHost
        tgtfile = options.tgtfile
        if (tgtHost == None) or (tgtfile == None):
            print parser.print_help()
            exit(0)
        else:
            try:
                orig_stdout = sys.stdout
                f = open(tgtfile, 'wb') 
                sys.stdout = f
                client.connect(tgtHost, 1883, 60)
                client.loop_forever()
            except KeyboardInterrupt:
                sys.stdout = orig_stdout
                f.close()
                client.disconnect()
                print("[+] Interrupt recieved, closing request to %s" % tgtHost)

if __name__ =='__main__':
        main()

