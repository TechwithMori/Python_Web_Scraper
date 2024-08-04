from selenium import webdriver
from selenium.webdriver.common.by import By
import pika

def scrape_data():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    driver.get('https://example.com')
    data = driver.find_element(By.XPATH, '//*[@id="data"]').text
    driver.quit()

    return data

def send_to_queue(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='data_queue')
    channel.basic_publish(exchange='', routing_key='data_queue', body=message)
    connection.close()

if __name__ == '__main__':
    data = scrape_data()
    send_to_queue(data)
