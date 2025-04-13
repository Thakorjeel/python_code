function runSpeedTest() {
  // Start the speed test and show a loading state
  document.getElementById('ping').textContent = 'Testing...';
  document.getElementById('download').textContent = 'Testing...';
  document.getElementById('upload').textContent = 'Testing...';

  // Simulate a speed test with random values (to mimic real values)
  // In a real-world scenario, you can replace this with actual testing logic (like fetching data from a server or using libraries)
  setTimeout(() => {
    const ping = Math.floor(Math.random() * 100) + 10;  // Random ping value between 10ms and 100ms
    const download = (Math.random() * 50 + 20).toFixed(2);  // Random download speed between 20Mbps and 70Mbps
    const upload = (Math.random() * 30 + 10).toFixed(2);  // Random upload speed between 10Mbps and 40Mbps

    // Update the results with the simulated values
    document.getElementById('ping').textContent = `${ping} ms`;
    document.getElementById('download').textContent = `${download} Mbps`;
    document.getElementById('upload').textContent = `${upload} Mbps`;
  }, 2000);  // Simulate a 2-second delay for the test
}

