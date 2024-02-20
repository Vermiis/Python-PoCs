import subprocess

#subprocess.call(["calc"], shell=True)

#out=subprocess.check_call(["cmd", "/c", "whoami"])

out=subprocess.check_output(["cmd", "/c", "whoami"])
print("ourtput {}".format(out.decode()))