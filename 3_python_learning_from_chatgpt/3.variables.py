import logging

logging.basicConfig(
    filename="variables.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

test_cases = 10      # Integer
timeout = 2.5        # Float
browser = "Chrome"   # String
is_logged = False    # Boolean
browsers = ["Chrome", "Firefox", "Edge"]  # List
user = {"username": "admin", "role": "QA Lead"}  # Dictionary

print(f"Running {test_cases} test cases on {browser}")

def validate_page_load(time_taken):
    if time_taken > 5:
        logging.warning("application took more time to load page (%s sec)", time_taken)
    else:
        logging.info(f"application get loaded in time (%s sec) {time_taken}")

def login_to_app1(user,paswrd,browser):
    logging.info(f"launched app in {browser} browser")
    logging.info(f"entered username {user}",)
    logging.info(f"entered password {paswrd}", )
    logging.info("clicked on enter button")
    logging.info("dashboard page displayed")
    logging.info("login test passed successfully")
    global is_logged
    is_logged = True
    logging.info(f"flag is_logged set to {is_logged}")

def login_to_app2(user,paswrd,browser):
    logging.info(f"launched app in {browser} browser")
    logging.info(f"entered username {user}",)
    logging.error(f"entered blank password {paswrd}", )
    logging.error("clicked on enter button")
    logging.error("login test failed")
    global is_logged
    is_logged = False
    logging.info(f"flag is_logged set to {is_logged}")

validate_page_load(6)
login_to_app1('admin','admin123', 'chrome')
login_to_app2('admin','', 'chrome')