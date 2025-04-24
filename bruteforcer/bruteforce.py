import argparse
import requests
import logging
from datetime import datetime

def setup_logger():
    # Configure the logger
    logging.basicConfig(
        filename='login_attempts.log',
        level=logging.INFO,
        format='%(asctime)s - IP: %(ip)s -Username: %(username)s - Status: %(status)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
def parse_args():
    parser = argparse.ArgumentParser(description='Login script')
    parser.add_argument('--url', required=True, help='Target URL')
    parser.add_argument('--username', required=True, help='admin')
    parser.add_argument('--password', required=True, help='password')
    parser.add_argument('--wordlist', type=str, required=True, help='/attack/wordlist.txt')
    parser.add_argument('--ip', required=False, default='N/A', help='127.0.0.1')
    
    return parser.parse_args()

def log_attempt(ip, username, status):
    logging.info('', extra={'ip': ip, 'username': username, 'status': status})

def main():
    setup_logger()
    args = parse_args()
    
    # Define the POST data
    data = {
        'username': args.username,
        'password': args.password
        }
    
    try:
        # Send the POST request
        response = requests.post(args.url, data=data)
        
        # Check the response status code
        if response.status_code == 200:
            print('Login successful')
            log_attempt(args.ip, args.username, 'SUCCESS')
        else:
            print('Login failed')
            log_attempt(args.ip, args.username, 'FAILURE')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        log_attempt(args.ip, args.username, f'ERROR: {e}')

if __name__ == '__main__':
    main()
