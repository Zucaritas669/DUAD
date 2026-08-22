import pytest
from datetime import datetime

print("=" * 50)
print("AUTOMATED TESTING")
print("=" * 50)
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

result = pytest.main([
    "tests/",
    "-v"
])

print()
print("=" * 50)

if result == 0:
    print("All the test passed")
else:
    print("Some tests did not pass")
print("=" * 50)

