import csv
from hv import HV
from vm import VM

class ALLHVS:

  def __init__(self, filename='hv_list.csv'):
    self.hv_dict = {}
    with open(filename) as f:
      reader = list(csv.reader(f))
    for i, hv_info in enumerate(reader, 1):
      c_h, m_h = int(hv_info[0]), int(hv_info[1])
      hv = HV(i, c_h, m_h)
      self.hv_dict[i] = hv

  def get_command(self):
    input_list = input().split()
    if input_list[0] == "create":
      c_v, m_v = int(input_list[1]), int(input_list[2])
      vm = VM(c_v, m_v)
      self.create(vm)
    elif input_list[0] == "delete":
      pass
    else:
      pass
  
  def create(self, vm):
    hv_list = self.hv_dict.items()
    order_hv_list = sorted(hv_list, key=lambda x:x[1].cpu_usage)
    for _, hv in order_hv_list:
      if hv.check_allocate(vm):
        print("OK")
        print("allocate to HV{}".format(hv.hv_number))
        hv.allocate(vm)
        break
    else:
      print("NG")