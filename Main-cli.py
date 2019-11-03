import math
import os
import time
import json
import errno

print("This program tests the Internet Speed")
try:
    import speedtest
    s = speedtest.Speedtest()
except ImportError as e:
    exit()
memorypreallocation = input("Disable memory preallocation? (press enter= no/ press Y = yes) >> ").upper()
print("Set the values:")
times = math.inf
timeout = int(input("How many seconds between every test: >> "))
kindoftestdown = 1
kindoftestup = 1
testping = 1
timessofar = 1
try:
    os.makedirs("Logs")
    print("Folder created!!")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
if timeout == 0:
    timeout = 1
    print("TIMEOUT MUST BE 1 SECOND AT LEAST...")
dirname = os.path.dirname(__file__)
filename= os.path.join(dirname, "Logs/CLI_" + time.strftime("%Y-%m-%d_%H-%M-%S")+".txt")
while timessofar <= times:
    f = open(filename, "a")
    if timessofar == 1:
        print("DO NOT CLOSE THE WINDOW OR THE TEST WILL HALT!")
        print("Connecting to the closest server...")
        serverdata = (s.get_best_server())
        f.write(json.dumps(serverdata))
        print("USING SERVER:" )
        for x, y in serverdata.items():
            print(x, ": ", y)
        print (serverdata)
        print('TEST RUN AT: ', time.strftime("%c") + " with serial " + str(times) + str(kindoftestup) + str(kindoftestdown) + str(testping) + str(timeout))
        f.write("\n" + "TEST RUN AT: " + time.strftime("%c") + "with serial" + str(times) + str(kindoftestup) + str(kindoftestdown) + str(testping) + str(timeout))
    else:
        print("Waiting", timeout, " seconds...")
        time.sleep(timeout)
    print("\n------------------------------------------------------------------------------------------------")
    print("TEST NUMBER", timessofar, "/", times, ":", kindoftestdown, kindoftestup, testping, timeout, times, "at time", time.strftime("%c") )
    f.write("\n" + "\n-----------------------------------------------------------" + "\nTEST NUMBER " + str(
        timessofar) + "/" + str(times) + ": " + str(kindoftestdown) + str(kindoftestup) + str(testping) + str(
        timeout) + str(times) + " at time " + time.strftime("%c"))
    print("Testing download speed...(", timessofar, ")/(", times, ")")
    download = s.download()
    download = download / 1024
    download = round(download)
    print("Download Speed (", timessofar, "): ", download, "KB/s. ", download / 1024, "MB/s")
    f.write("\nDownload Speed ("+ str(timessofar)+ "): "+ str(download) + "KB/s. "+ str(download / 1024)+ "MB/s")
    print("Testing ping...(", timessofar, ")")
    ping = s.lat_lon
    print("Ping:" , ping)
    f.write("\nPing:" + str(ping))
    print("Testing upload speed...(", timessofar, ")")
    if memorypreallocation == "Y":
         upload = s.upload(pre_allocate=False)
    elif memorypreallocation != "Y":
        upload = s.upload()
    upload = upload / 1024
    upload = round(upload)
    print("Upload Speed (", timessofar, "): ", upload, "KB/s. ", upload / 1024, "MB/s")
    f.write("\nUpload Speed (" + str(timessofar) + "): " + str(upload) + "KB/s. " + str(upload / 1024) + "MB/s")
    print("TEST FINISHED...")
    timessofar = timessofar + 1
    f.close()
if times == 0:
    print("No tests will be executed...")
else:
    print("Schelude completed. Check " + filename)
input()

