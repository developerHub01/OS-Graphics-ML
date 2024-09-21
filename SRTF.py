""" Shorting Remaining Time First (Pre-emtive) """

from pprint import pprint

class SRJF:
  def __init__(self):
    self.number_of_process = 0
    self.processes = []
    self.complete_processes = []
    self.current_time = 0

  
  def start(self):
    self.processes = self.get_process_list()
    
    self.start_process()
    
    self.print_result()
  
  def start_process(self):
    while True: 
      current_process_index = self.get_selectable_process()

      if current_process_index == -1:
        self.current_time += 1
        continue
      
      print("current_process_index: ", current_process_index)
      
      if 'first_response_time' not in self.processes[current_process_index]:
        self.processes[current_process_index]['first_response_time'] = self.current_time
         
      self.processes[current_process_index]['changeable_bt'] -= 1
      self.processes[current_process_index]['ct'] = self.current_time + 1
      self.processes[current_process_index]['tat'] = self.get_turn_around_time(current_process_index)
      self.processes[current_process_index]['wt'] = self.get_wait_time(current_process_index)
      self.processes[current_process_index]['rt'] = self.get_response_time(current_process_index)

      self.current_time += 1
      
      """ check if that process is completed then move it inot complete_processes list """
      if not self.processes[current_process_index]['changeable_bt']:
        process = self.processes.pop(current_process_index)
        self.complete_processes.append(process)
        
      if not len(self.processes): break
      
    self.complete_processes.sort(key=lambda x: x['id'])

  
  def get_selectable_process(self):
    selectable_min_bust_list = []
    min_bust_time = float("inf")
    
    for index, details in enumerate(self.processes):
      """ checking that is there any process till that time which are not completed """
      if (not details['changeable_bt']) or (details['at'] > self.current_time): continue
      
      if details['changeable_bt'] < min_bust_time:
        selectable_min_bust_list = [index]
        min_bust_time = details['changeable_bt']
      elif details['changeable_bt'] == min_bust_time:
        selectable_min_bust_list.append(index)
    
    if not len(selectable_min_bust_list):
      return -1
    
    return self.get_min_arrival_time(selectable_min_bust_list)

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
          "changeable_bt": int(current_process_data[1]),
        })
        
      return processes
      
    except Exception as e:
      print("Process number must be a number")

  def get_turn_around_time(self, index):
    return self.processes[index]['ct'] - self.processes[index]['at']

  def get_wait_time(self, index):
    return self.processes[index]['tat'] - self.processes[index]['bt']
  
  def get_response_time(self, index):
    return self.processes[index]['first_response_time'] - self.processes[index]['at']
  

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

  
srjf1 = SRJF()
srjf1.start()