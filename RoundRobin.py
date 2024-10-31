class RoundRobin:
  def __init__(self):
    self.number_of_process = 0
    self.time_quanta = 1
    self.ready_queue = []
    self.processes = []
    self.complete_processes = []
    self.current_time = 0

  
  def start(self):
    self.processes = self.get_process_list()
    
    self.start_process()
    
    self.print_result()
    
  def start_process(self):
    while True:
      if not len(self.ready_queue):
        selected_process = self.get_selected_process()
        self.ready_queue.append(selected_process)
      
      current_process = self.ready_queue.pop(0)
      
      # self.processes[]
      
      
      # min_arrival_index = self.get_min_arrival_time()
      
      # self.ready_queue += min_arrival_index
      
      """ find the list of process lies into that time stemp """

      """ push that process into the ready queue """

      """ pop that first process from the ready queue """
      
      """ update that process data based on it's id """

      """ update current time """

      """ if process is empty then break """
      
  def get_selected_process(self):
    pass
  
  def get_min_arrival_time(self):
    min_arrival_time = []
    
    for index in self.processes:
      if self.processes[index]['at'] > self.current_time: continue
      
      min_arrival_time.append(index)
      
    min_arrival_time.sort()
    
    return min_arrival_time  
  
  def get_process_list(self):
    processes = []
    
    try:
      self.number_of_process = int(input("Number of processes = "))
      self.time_quanta = int(input("Time quanta = "))
      
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


if __name__ == '__main__':
  round_robin = RoundRobin()
  round_robin.start()