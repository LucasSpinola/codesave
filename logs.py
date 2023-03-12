import logging


def guardar_log():
  logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='./logs/comp.log',
    filemode='a'
  )
