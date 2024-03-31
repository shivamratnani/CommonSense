import answers
import boto3
import questions
import requests
from bs4 import BeautifulSoup


def scrapeData():
    url = 'https://quizlet.com/899330417/computersciencequestionsdataset-flash-cards/?i=4majqt&x=1jqt'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

    with open('filename.txt', 'w') as file:
        # Iterate over each question and answer
        for question, answer in zip(questions, answers):
            # Write the question and answer to the file, followed by three newlines
            file.write(f"{question},{answer}\n\n\n")

def getData(dataset):
    # Get the data from dataset.txt
    with open(dataset, 'r') as file:
        data = file.read().split('\n')
    if data == ['']:
        print("Unable to get data.")
    return data


def uploadData(data):
    # Upload the data to S3

    # Initialize S3 client
    s3 = boto3.client('s3')

    # Upload the data to S3
    #s3.put_object(Bucket='your-s3-bucket-name', Key='dataset.txt', Body='\n'.join(data))

    return None

def downloadData():
    # Download the data from S3

    # Initialize S3 client
    s3 = boto3.client('s3')

    # Download the data from S3
    #response = s3.get_object(Bucket='your-s3-bucket-name', Key='dataset.txt')
    #data = response['Body'].read().decode('utf-8').split('\n')

    return None