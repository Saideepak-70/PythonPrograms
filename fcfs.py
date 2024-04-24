def process(pid, arrival_time, burst_time):
  """
  Process object to store process information.
  """
  self.pid = pid
  self.arrival_time = arrival_time
  self.burst_time = burst_time
  self.completion_time = 0
  self.turnaround_time = 0
  self.waiting_time = 0

def fcfs(processes):
  """
  FCFS (First Come First Served) scheduling algorithm.
  """
  n = len(processes)
  completed = [False] * n
  current_time = 0
  waiting_time = [0] * n
  turnaround_time = [0] * n

  # Sort processes by arrival time
  processes.sort(key=lambda p: p.arrival_time)

  # Process jobs one by one
  for i in range(n):
    if not completed[i] and processes[i].arrival_time <= current_time:
      completed[i] = True
      processes[i].completion_time = current_time + processes[i].burst_time
      processes[i].turnaround_time = processes[i].completion_time - processes[i].arrival_time
      processes[i].waiting_time = processes[i].turnaround_time - processes[i].burst_time
      current_time += processes[i].burst_time

  # Calculate waiting and turnaround times
  for i in range(n):
    waiting_time[i] = processes[i].waiting_time
    turnaround_time[i] = processes[i].turnaround_time

  # Print results
  print("FCFS:")
  print("Process ID | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time")
  for i in range(n):
    print(f"{processes[i].pid} | {processes[i].arrival_time} | {processes[i].burst_time} | {processes[i].completion_time} | {processes[i].turnaround_time} | {processes[i].waiting_time}")

  return waiting_time, turnaround_time
