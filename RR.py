import time
def round_robin(processes, quantum):
   n = len(processes)
   remaining_burst_time = [0] * n
   response_time = [0] * n
   turnaround_time = 0
   total_waiting_time = 0
   total_response_time = 0
   entry_times = [0] * n
   for i in range(n):
       remaining_burst_time[i] = int(processes[i][1])
   print(f"Schdeuling algorithm: RR")
   print(f"Total {n} tasks are read from \"input.txt\". Press \"enter\" to start...")
   print("===================================================================")
   input()
   print(f"<system time 0> process 1 is running")
   t = 0
   while True:
       done = True
       for i in range(n):
           if remaining_burst_time[i] > 0:
               done = False
               if remaining_burst_time[i] > quantum:
                   if response_time[i] == 0:
                       response_time[i] = t - int(processes[i][0])
                   for _ in range(quantum):
                       t += 1
                       print(f"<system time {t}> process {i+1} is running")
                       time.sleep(1)
                   remaining_burst_time[i] -= quantum
                   if entry_times[i] == 0:
                       entry_times[i] = t
               else:
                   if response_time[i] == 0:
                       response_time[i] = t - int(processes[i][0])
                   for _ in range(remaining_burst_time[i]):
                       t += 1
                       print(f"<system time {t}> process {i+1} is running")
                       time.sleep(1)
                   total_waiting_time += t - int(processes[i][0]) - response_time[i]
                   remaining_burst_time[i] = 0
                   print(f"<system time {t}> process {i+1} is finished.......")
       if done:
           break
   avg_response_time = sum(response_time) / n
   avg_waiting_time = total_waiting_time / n
   turnaround_time = avg_waiting_time + sum(int(process[1]) for process in processes) / n
   print(f"<system time {t}> All processes finished..............")
   print(f"Average Waiting Time: {avg_waiting_time:.2f}")
   print(f"Average Response Time: {avg_response_time:.2f}")
   print(f"Average Turnaround Time: {turnaround_time:.2f}")
if __name__ == "__main__":
   processes = []
   with open("input.txt", 'r') as file:
       for line in file:
           processes.append(line.split())
   round_robin(processes, 4)  # Quantum for Round Robin,we can change it