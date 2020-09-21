import aiml
import os

#create the kernel
kernel = aiml.Kernel()

# if os.path.isfile("bot_brain.brn") :
# 	kernel.bootstrap(brainFile = "bot_brain.brn")
# else :
kernel.bootstrap(learnFiles = "aiml_ref/std-startup.xml", commands = "load bibo")
kernel.setPredicate("bibo_flag", "empty")
# kernel.bootstrap(learnFiles = "aiml_ref/std-startup.xml", commands = "load all")
# kernel.saveBrain("bot_brain.brn")

device=["robot"]
command=["turn on"]

# ready
while True:
	print(kernel.respond(input("text me >>")))
	r_device = kernel.getPredicate("bibo_device")
	r_command = kernel.getPredicate("bibo_command")
	r_flag = kernel.getPredicate("bibo_flag")
	if r_flag == "queued":
		device.append(r_device)
		command.append(r_command)
		kernel.setPredicate("bibo_flag", "empty")
		print("from python ",r_device, "with command ", r_command)

# print(kernel.respond(input("text me >>")))
# print(kernel.getPredicate("name"))

