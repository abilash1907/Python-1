Eimport re
import operator
import csv
def error_count(filename):
	e={}
	with open(filename, 'r') as f:
		for line in f.readlines():
			line=line.strip()
			if re.search(r"ticky: ERROR ([\w ]*)", line) is not None: 
				words=re.findall(r"ticky: ERROR ([\w ]*)", line)
				for i in words:
					if i in e.keys():
						e[i]+=1
					else:
						e[i]=1
		f.close()
	return dict(sorted(e.items(),key=operator.itemgetter(1),reverse=True))
def user_count(filename):
	count_info={}
	count_error={}
	user=[]
	l=[]
	with open("d.txt", 'r') as f:
		for line in f.readlines():
			line=line.strip()
			
			if re.search(r"ticky: INFO: ([\w ]*) ", line) is not None:
				for i in re.findall(r"\(([\w]*)\)",line):
					if i in count_info.keys():
						count_info[i]+=1
					else:
						count_info[i]=1
			elif re.search(r"ticky: ERROR: ([\w ]*) ", line) is not None:
				for i in re.findall(r"\(([\w]*)\)",line):
					if i in count_info.keys():
						count_error[i]+=1
					else:
						count_error[i]=1
		f.close()

	print("ERRORs:")
	print(count_error)
	print("INFO:")
	print(count_info)
def main():
	filename="d.txt"
	s=error_count(filename)
	print(s)
	with open("error.csv", "w") as f1:
		f1.write("%s,%s\n"%("Error","Count"))
		for key in s.keys():
        		f1.write("%s,%d\n"%(key,s[key]))
		f1.close()
	keys=["User","INFO","ERROR"]
	user_count(filename)
main()






