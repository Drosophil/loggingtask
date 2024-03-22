from mylog import logger

""" do something here """

for i in range(1,10):
    if i % 2 == 0:
        logger.warning(f"The number is 2N: {i} NOLOG")
    if i % 3 == 0:
        logger.error(f"The number is 3N: {i}")
