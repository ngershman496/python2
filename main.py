from multiprocessing.connection import wait
import psutil
from psutil._common import bytes2human
import os

def show_disks():
	temp = "%s\\ %12s %12s %12s %8d%% %12s %12s\\"
	temp1 = "%s %12s %12s %12s %9s %12s %13s"
	print(temp1 % ("Name", "Total", "Used", "Free", "Percent", "System", "Mount"))
	for part in psutil.disk_partitions(all=False):
		
		if os.name == 'nt':
			if 'cdrom' in part.opts or part.fstype == '':
				continue
			usage = psutil.disk_usage(part.mountpoint)
			print(temp % (part.device, bytes2human(usage.total), bytes2human(usage.used),
			  bytes2human(usage.free), int(usage.percent), part.fstype, part.mountpoint))

def get_memory():
	mem = psutil.virtual_memory()
	temp = "%s %12s %10s %10s"
	temp1 = "%s %13s %10s %10s"
	print(temp % ("Total", "Avaliable", "Used", "Free"))
	print(temp1 % (bytes2human(mem.total), bytes2human(mem.available), bytes2human(mem.used), bytes2human(mem.free)))

def partition():
	print("need to do")


if __name__ == '__main__':
	print("Disks:")
	show_disks()
	print()
	print("Memory:")
	get_memory()