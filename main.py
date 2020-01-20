import csv
from hv import HV
from vm import VM
from allhvs import ALLHVS
    
if __name__ == "__main__":
  hvs = ALLHVS()
  while True:
    hvs.get_command()
    # print(c_v, m_v)
    # vm = VM(c_v, m_v)
    