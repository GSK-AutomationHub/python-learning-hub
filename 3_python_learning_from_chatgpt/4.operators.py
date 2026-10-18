# Test case execution count
executed_tests = 5
total_tests = 10

# Calculate pending tests
pending_tests = total_tests - executed_tests

print(f"Tests Executed: {executed_tests}")
print(f"Pending Tests: {pending_tests}")

# Assertion check
if executed_tests == total_tests:
    print("All tests executed!")
else:
    print("Some tests are still pending.")
