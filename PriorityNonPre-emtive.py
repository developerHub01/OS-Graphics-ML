from pprint import pprint

class PriorityNonPre_emtive: 
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
  
  def start_process(self):
    for _ in range(len(self.processes)):
      current_process_index = self.get_selectable_process()
      
      self.start_time = max(self.processes[current_process_index]['at'], self.end_time)
      self.end_time = self.start_time + self.processes[current_process_index]['bt']
      
      self.processes[current_process_index]['ct'] = self.end_time
      self.processes[current_process_index]['tat'] = self.get_turn_around_time(current_process_index)
      self.processes[current_process_index]['wt'] = self.get_wait_time(current_process_index)
      self.processes[current_process_index]['rt'] = self.get_response_time(current_process_index)
      
      process = self.processes.pop(current_process_index)
      self.complete_processes.append(process)
      
    self.complete_processes.sort(key=lambda x: x['id'])
      
   
  def get_turn_around_time(self, index):
    return self.processes[index]['ct'] - self.processes[index]['at']

  def get_wait_time(self, index):
    return self.processes[index]['tat'] - self.processes[index]['bt']
  
  def get_response_time(self, index):
    return self.start_time - self.processes[index]['at']
  
  
  def get_selectable_process(self):
    selectable_prioritie_index = []
    min_priority = float("inf")
    
    for index in range(len(self.processes)):
      if self.processes[index]['at'] > self.end_time: continue
      
      if self.processes[index]['pt'] < min_priority:
        min_priority = self.processes[index]['pt']
        selectable_prioritie_index = [index]
      elif self.processes[index]['pt'] == min_priority:
        selectable_prioritie_index.append(index)
    
    if not len(selectable_prioritie_index):
      return self.get_min_arrival_time(range(len(self.processes)))
    
    return self.get_min_arrival_time(selectable_prioritie_index)
  
  def get_min_arrival_time(self, arr):
    min_arrival_index = arr[0]
    min_arrival_time = float("inf")

    for index in arr:
      if self.processes[index]['at'] < min_arrival_time:
        min_arrival_index = index
        min_arrival_time = self.processes[index]['at']
  
    return min_arrival_index
  
  def get_process_list(self):
    processes = []
    
    try:
      self.number_of_process = int(input("Number of processes = "))
      
      print("""
      ===========================
      || Process ===> P        ||
      || Arrival Time ===> AT  ||   
      || Bust Time ===> BT     ||
      || Priority ===> PT      ||         
      ===========================
      """)
      
      print("P    AT BT PT")
      for i in range(self.number_of_process):
        process_id = i+1
        current_process_data = input(f"P{process_id} = ").split()
        processes.append({
          "id": process_id,
          "at": int(current_process_data[0]),
          "bt": int(current_process_data[1]),        
          "pt": int(current_process_data[2]),
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
    Priority ===> PT
    Complete Time ===> CT
    Turn Around Time ===> TAT
    Wait Time ===> WT
    Response Time ===> RT
    =====================================
    """)

  

pnp1 = PriorityNonPre_emtive()
pnp1.start()