""" Shortest Job First (Non Pre-emtive) """

from pprint import pprint

class SJF:
  def __init__(self):
    self.number_of_process = 0
    self.processes = []
    self.complete_processes = []
    self.start_time = 0
    self.end_time = 0
  
  def start(self):
    self.processes = self.get_process_list()
    
    self.start_process()
    
    self.print_result()

  def get_turn_around_time(self, index):
    return self.processes[index]['ct'] - self.processes[index]['at']

  def get_wait_time(self, index):
    return self.processes[index]['tat'] - self.processes[index]['bt']
  
  def get_response_time(self, index):
    return self.start_time - self.processes[index]['at']
  
  
  def start_process(self):
    for i in range(len(self.processes)):
      current_process_index = self.get_selectable_process()
      
      self.start_time = max(self.end_time, self.processes[current_process_index]['at'])
      self.end_time = self.start_time + self.processes[current_process_index]['bt']
      
      self.processes[current_process_index]['ct'] = self.end_time
      self.processes[current_process_index]['tat'] = self.get_turn_around_time(current_process_index)
      self.processes[current_process_index]['wt'] = self.get_wait_time(current_process_index)
      self.processes[current_process_index]['rt'] = self.get_response_time(current_process_index)
      
      process = self.processes.pop(current_process_index)
      self.complete_processes.append(process)
      
    self.complete_processes.sort(key=lambda x: x['id'])
      
  def get_selectable_process(self):
    selectable_processes_burst_time = []
    min_burst_time = float("inf")
    
    for index, process in enumerate(self.processes):
      if process['at'] > self.end_time: continue
      
      if process['bt'] < min_burst_time:
        selectable_processes_burst_time = [index]
        min_burst_time = process['bt']
      elif process['bt'] == min_burst_time:
        selectable_processes_burst_time.append(index)
        
    if not len(selectable_processes_burst_time):
      return self.get_min_arrival_time(list(range(len(self.processes))))
    
    return self.get_min_arrival_time(selectable_processes_burst_time)
        
  def get_min_arrival_time(self, arr):
    min_arrival_index = arr[0] 
    min_arrival_time = float("inf")
    
    for index in arr:
      if self.processes[index]['at'] < min_arrival_time:
        min_arrival_time = self.processes[index]['at']
        min_arrival_index = index
    
    return min_arrival_index

  def get_process_list(self):
    processes = []
    try:
      self.number_of_process = int(input("Number of processes = "))
      
      print("""
      ==========================
      || Process ===> P       ||
      || Arrival Time ===> AT ||   
      || Bust Time ===> BT    ||         
      ==========================
      """)
      
      print("P    AT BT")
      
      for i in range(self.number_of_process):
        process_id = i+1
        current_process_data = input(f"P{process_id} = ").split()
        processes.append({
          "id": process_id,
          "at": int(current_process_data[0]),
          "bt": int(current_process_data[1]),        
        })
        
      return processes
              
    except Exception as e:
      print("Process number must be a number")
  
  def print_result(self):
    print("P\t AT\t BT\t CT\t TAT\t WT\t RT")
    for _, data in enumerate(self.complete_processes):
      print(f"P{data['id']}\t {data['at']}\t {data['bt']}\t {data['ct']}\t {data['tat']}\t {data['wt']}\t {data['rt']}")
    
    print("""
    =====================================
    Process ===> P
    Arrival Time ===> AT
    Bust Time ===> BT
    Complete Time ===> CT
    Turn Around Time ===> TAT
    Wait Time ===> WT
    Response Time ===> RT
    =====================================
    """)


sjf1 = SJF()
sjf1.start()