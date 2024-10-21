import certstream
import json
import os

def callback(message, context):
    if message['message_type'] == "certificate_update":
        for cert in message['data']['leaf_cert']['all_domains']:
            # Hapus wildcard jika ada
            if cert.startswith('*.'):
                cert = cert[2:]
            # Tulis domain ke file
            with open('domains.txt', 'a') as f:
                f.write(cert + '\n')

def main():
    # Hapus file lama jika ada
    if os.path.exists('domains.txt'):
        os.remove('domains.txt')
    
    # Start certstream
    certstream.listen_for_events(callback, url='wss://certstream.calidog.io/')

if __name__ == "__main__":
    main()
