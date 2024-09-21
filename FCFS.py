""" First come first serve (Non Pre-emtive) """

""" 
P1 0 2
P2 1 2
P3 5 3
P4 6 4
"""

""" 
process data queue details
===================
{
  "id: "P1",
  "at": int(current_process_data[0]),
  "bt": int(current_process_data[1]),
  "ct": None,
  "tat": None,
  "wt": None,
  "rt": None,
  "is_complete": False,
}
"""

from pprint import pprint

class FCFS: 
  def __init__(self):
    self.number_of_process = 0
    self.processes = []
    self.complete_procesees = []
    self.start_time = 0
    self.end_time = 0
  
  def get_process_list(self):
    processes = []
    try:
      self.number_of_process = int(input("Number of processes = "))
      
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

  def get_selectable_process(self):
    selectable_process_index = 0
    min_arrival_time = float("inf")

    for index, details in enumerate(self.processes):
      if details['at'] < min_arrival_time: 
        min_arrival_time = details['at']
        selectable_process_index = index
    
    return selectable_process_index
        
    
  
  def get_turn_around_time(self, index): 
    return self.processes[index]['ct'] - self.processes[index]['at']

  def get_wait_time(self, index): 
    return self.processes[index]['tat'] - self.processes[index]['bt'] 

  def get_response_time(self, index): 
    return self.start_time - self.processes[index]['at'] 

  def start_process(self):
    for _ in range(len(self.processes)):
      current_process_index = self.get_selectable_process()
      
      self.start_time = max(self.end_time, self.processes[current_process_index]["at"])
      self.end_time = self.start_time + self.processes[current_process_index]['bt']
      
      self.processes[current_process_index]["ct"] = self.end_time
      
      self.processes[current_process_index]["tat"] = self.get_turn_around_time(current_process_index)
      
      self.processes[current_process_index]["wt"] = self.get_wait_time(current_process_index)
      
      self.processes[current_process_index]["rt"] = self.get_response_time(current_process_index)
      
      process = self.processes.pop(current_process_index)
      self.complete_procesees.append(process)
      
    self.complete_procesees.sort(key=lambda x: x['id'])


  def start(self):
    self.processes = self.get_process_list()
    
    self.start_process() 
    
    self.print_result()
  
  def print_result(self):
    print("P\t AT\t BT\t CT\t TAT\t WT\t RT")
    for _, data in enumerate(self.complete_procesees):
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
  
fcfs1 = FCFS()
fcfs1.start()