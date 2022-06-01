import psutil

path = "/dev/sda"
DiskRuum = psutil.disk_usage(path)
Vmemory = psutil.virtual_memory()
print("Vaba RAMi on", Vmemory[4])
print("Kokku RAMi on", Vmemory[0])
print(DiskRuum)