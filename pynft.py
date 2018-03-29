import os
import glob
import pandas
import csv

def get_stat_from_file(file_name):
	try:
		df = pandas.read_csv(file_name, delimiter="\t")
		cpus = df['%CPU'].apply(lambda x: float(x[:-1]))
		mems = df['RSS'].apply(lambda x: float(x[:-1]))
		return {"cpu_max":cpus.max(), "cpu_avg":cpus.sum()/cpus.shape[0], "mem_max": mems.max(), "mem_avg": mems.sum()/mems.shape[0]}
	except:
		return {"error": "Something went wrong"}

if __name__ == "__main__":
	current_dir = os.getcwd()
	files_pattern = "/*.csv"
	files = glob.glob(current_dir+files_pattern)
	for file_name in files:
		stats =	get_stat_from_file(file_name)
		if not "error" in stats.keys():
			print "For file: {}".format(file_name)
			print "CPU max: {} \nCPU avg: {}\nMEMORY max: {} \nMEMORY avg: {}\n".format(stats["cpu_max"], stats["cpu_avg"], stats["mem_max"], stats["mem_avg"])

