print("[+] Hello and welcome to deep, in the man cave...")
print("What is your name?")
name = input()
print(" Good we will be checking your log report for suspicious activities, welcome " +name)

def analyze_log(filename):
	keywords = {
		"FAILED": 0, "DENIED": 0, "ERROR": 0, "WARNING": 0,"SSH": 0,"ROOT":0
	}
	total_lines = 0

	with open(filename, "r") as file:
		for line in file:
			total_lines += 1
			line = line.upper()
			
			for keyword in keywords:
				if keyword in line:
					keywords[keyword] += 1
	print(f"Total lines processed: {total_lines}")
	
	for keyword, count in sorted(keywords.items(), key=lambda x: x[1], reverse=True):
		print(f"{keyword:<10} : {count}")
	
analyze_log("Linux_2k.log")
