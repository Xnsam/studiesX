import torch
import time

if not torch.backends.mps.is_available():
	print("MPS not available, Running only on a CPU")
	exit()

def benchmark(device_name, size=5000):
	device = torch.device(device_name)
	# create large random matrices
	a = torch.randn(size, size, device=device)
	b = torch.randn(size, size, device=device)

	# warm-up (initialise the device)
	torch.mm(a, b)
	if device_name == "mps":
		torch.mps.synchronize()
	
	start = time.time()
	for _ in range(10):
		c = torch.mm(a, b)
	if device_name == "mps":
		torch.mps.synchronize()
	end = time.time()

	print(f"time on {device_name.upper()}: {(end - start): .4f} seconds")

print(f"--- starting pytorch benchmark (5000 X 5000 matrix) ----")
benchmark("cpu")
benchmark("mps")

