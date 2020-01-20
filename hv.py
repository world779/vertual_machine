class HV:
  def __init__(self, hv_number, cpu, memory):
    self.hv_number = hv_number
    self.cpu = cpu
    self.memory = memory
    self.max_cpu = cpu
    self.max_memory = self.memory
    self.cpu_usage = 0

  def check_allocate(self, vm):
    return vm.cpu <= self.cpu and vm.memory <= self.memory
  
  def allocate(self, vm):
    if self.check_allocate(vm):
      self.cpu = self.cpu - vm.cpu
      self.memory = self.memory - vm.memory
      self.cpu_usage = self.get_cpu_usage()
  
  def get_cpu_usage(self):
    return 1 - self.cpu/self.max_cpu

