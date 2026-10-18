import logging


def log_events(filename):
    return logging.basicConfig(
        filename=f'{filename}.log',
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s")


def test_run(filename, test_name,result):
    log_events(filename)
    logging.info("Test Execution started .....")
    try:
        if result == 'passed':
           logging.info(f"{test_name} is Passed")
        elif result == 'failed':
           logging.info(f"{test_name} is Failed")
    except:
        logging.error("Test Execution terminated due to error .....")
    logging.info("Test Execution completed .....")