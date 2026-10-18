import logging

# Configure logging to write to a file
logging.basicConfig(
    filename='test_execution.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

def execute_test():
    logging.info("Test Started......")
    logging.info("Launching application......")
    logging.info("Checking login functionality...")
    logging.info("Verifying dashboard loading...")
    logging.info("Test completed......")

def check_page_load(time_taken):
    if time_taken > 5:
        logging.warning("Page took longer than expected to load (%s sec)", time_taken)
    else:
        logging.info("Page loaded in %s seconds", time_taken)

def validate_login_button(button_found):
    if not button_found:
        logging.error("Login button not found! Test Failed.")
    else:
        logging.info("Login button is present.")


# Run the test execution function
execute_test()

# Example where a warning is logged
check_page_load(6)

# Simulating missing login button
validate_login_button(False)

print("Test execution log saved to 'test_execution.log'.")