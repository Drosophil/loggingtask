from mylog import logger

""" do something else here """

for i in range(1,10):
    if i % 7 == 0:
        logger.critical(f"Oh, no! The number is 7N: {i}")