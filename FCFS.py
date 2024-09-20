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
  "name: "P1",
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
    self.start_time = 0
    self.end_time = 0
  
  def get_process_list(self):
    processes = []
    try:
      self.number_of_process = int(input("Number of processes = "))
      
      for i in range(self.number_of_process):
        process_name = f"P{i+1}"
        current_process_data = input(f"{process_name} = ").split()
        processes.append({
          "name": process_name,
          "at": int(current_process_data[0]),
          "bt": int(current_process_data[1]),
          "is_complete": False,
        })
        
      return processes
    
    except Exception as e:
      print("Process number must be a number")

  def get_priority_index(self):
    min_at = float("inf")
    min_index = -1
    for index, details in enumerate(self.processes):
      """ checking that is there any process till that time which are not completed """
      if details['is_complete'] or details['at'] > self.end_time: continue
      if details['at'] < min_at: 
        min_at = details['at']
        min_index = index
    return min_index
  
  def get_turn_around_time(self, index): 
    return self.processes[index]['ct'] - self.processes[index]['at']

  def get_wait_time(self, index): 
    return self.processes[index]['tat'] - self.processes[index]['bt'] 

  def get_response_time(self, index): 
    return self.start_time - self.processes[index]['at'] 

  def start_process(self):
    for i in range(self.number_of_process):
      current_process_index = self.get_priority_index()
      
      self.start_time = max(self.end_time, self.processes[current_process_index]["at"])
      self.end_time = self.start_time + self.processes[current_process_index]['bt']
      
      self.processes[current_process_index]["ct"] = self.end_time
      
      self.processes[current_process_index]["tat"] = self.get_turn_around_time(current_process_index)
      
      self.processes[current_process_index]["wt"] = self.get_wait_time(current_process_index)
      
      self.processes[current_process_index]["rt"] = self.get_response_time(current_process_index)
      
      self.processes[current_process_index]["is_complete"] = True
      

  def return_process_data(self):
    data = self.processes
    for index, details in enumerate(data):
      data[index].pop("is_complete") 
    return data

  def start(self):
    self.processes = self.get_process_list()
    
    self.start_process() 
    
    return self.return_process_data()
  
  def print_result(self):
    print("P\t AT\t BT\t CT\t TAT\t WT\t RT")
    for _, data in enumerate(self.processes):
      print(f"{data['name']}\t {data['at']}\t {data['bt']}\t {data['ct']}\t {data['tat']}\t {data['wt']}\t {data['rt']}")
    
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
fcfs1.print_result()