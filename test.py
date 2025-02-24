# # -*- coding: utf-8 -*-
#
# # some general info
# # --------------------------------------------------------------------------
# # cd /home/manitowoc/build-testGuiMqtt-Desktop-Debug/ && ./testGuiMqtt
# # ./squishrunner --testsuite "/home/manitowoc/suite_testSuiteTesting" --local
# # tags are mqttPublish for test_case 2 and other mqtt publish (has to remove --debugLog if i use tags
# # /home/manitowoc/squish-for-qt-7.2.1/bin/squishrunner --debugLog --testsuite /home/manitowoc/suite_testSuiteTesting --testcase /home/manitowoc/suite_testSuiteTesting/tst_testStuff/
# # /home/manitowoc/squish-for-qt-7.2.1/bin/squishrunner --testsuite /home/manitowoc/suite_testSuiteTesting --tags engine
# # to write the test you need to change INVALID TO OK for the specific one you are looking at + change the number to the value you desire 
# # /home/manitowoc/squish-for-qt-7.2.1/bin/squishrunner --testsuite /home/manitowoc/suite_testSuiteTesting --tags @publishing for bdd test
# # --random to do it in different order
#
# # sudo lsof -iTCP:8080 -sTCP:LISTEN to get pid you can use it to kill the process if needed
# # make sure you turn on verbose as well
#
# # for html thing that can be reported on use /home/manitowoc/squish-for-qt-7.2.1/bin/squishrunner --testsuite /home/manitowoc/suite_testSuiteTesting --tags @publishing --reportgen html,/home/manitowoc/suite_testSuiteTesting/results
# # this will create the report that team and dave can use to check for processses

# https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html < for environment purposes
#https://blog.mbedded.ninja/programming/operating-systems/linux/how-to-use-socketcan-with-the-command-line-in-linux/
# # --------------------------------------------------------------------------
#
# # import qMapDatabase
# import ctypes
# from ctypes import *
# import os
# from threading import Thread
# from time import sleep
# import subprocess
#
#
# def mqtt_server():
#     huh2 = ctypes.cdll.LoadLibrary("/home/manitowoc/testGuiMqtt3/libhello.so")
#     interesting = str(huh2.hello())
#     test.log(str(interesting))
#     print(huh2)
#     # print(ctypes.cast(interesting, ctypes.py_object).value)
#     test.log(str(huh2.hello()))
#     happy = c_int(huh2.hello())
#     print(happy)
#     # test.log(happy)
#     test.log("aaaaa")
#     subprocess.call("python3 /home/manitowoc/testGuiMqtt3/test.py", shell=True)
#     test.log("aaaaa")
#     subprocess.call("cd /home/manitowoc/build-testGuiMqtt-Desktop-Debug/ && ./testGuiMqtt", shell=True)
#     test.log("hmmm")
#     # snooze(10);
#
#
# def main():
#     thread = Thread(target=mqtt_server)
#     thread.start()
#     thread.join()
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/Engine/Transmission/Temp -m 3.00")
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/Config/RiggingCode_Startup -m 3")
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/Lights/IsOn/Boom -m false")
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/Boom/A2B -m true")
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/Outrigger/Beam/p045/Percent -m 3.00")
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/Engine/Transmission/AWD/IsActive -m true")
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/RCL/Hook/Load/ActualTons~p2 -m 2")
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/Boom/TipHeight -m 9")
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/Boom/Angle~p2 -m 7")
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/RCL/Hook/Radius~p2 -m 2")
#     # huh2 =  ctypes.cdll.LoadLibrary("/home/manitowoc/testGuiMqtt3/libhello.so")
#     # interesting = str(huh2.hello())
#     # test.log(str(interesting))
#     # print(huh2)
#     # #print(ctypes.cast(interesting, ctypes.py_object).value)
#     # test.log(str(huh2.hello()))
#     # happy = c_int(huh2.hello())
#     # print(happy)
#     # #test.log(happy)
#     # test.log("aaaaa")
#     # subprocess.call("python3 /home/manitowoc/testGuiMqtt3/test.py", shell=True)
#     # test.log("aaaaa")
#     # subprocess.call("cd /home/manitowoc/build-testGuiMqtt-Desktop-Debug/ && ./testGuiMqtt", shell=True)
#     # test.log("hmmm")
#     # snooze(10);
#     # os.system("mosquitto_pub -h 10.100.30.130 -t craneInfo/Config/RiggingCode_Startup -m 3")
#     # subprocess.call("mosquitto_pub -h 10.100.30.130 -t craneInfo/Lights/IsOn/Boom -m false", shell=True)
#     # subprocess.call("mosquitto_pub -h 10.100.30.130 -t craneInfo/Boom/A2B -m true", shell=True)
#     # subprocess.call("mosquitto_pub -h 10.100.30.130 -t craneInfo/Engine/Transmission/Temp -m 3.00", shell=True)
#     # subprocess.call("mosquitto_pub -h 10.100.30.130 -t craneInfo/Outrigger/Beam/p045/Percent -m 3.00", shell=True)
#     # subprocess.call("mosquitto_pub -h 10.100.30.130 -t craneInfo/Engine/Transmission/AWD/IsActive -m true", shell=True)
#     # subprocess.call("mosquitto_pub -h 10.100.30.130 -t craneInfo/RCL/Hook/Load/ActualTons~p2 -m 66.14", shell=True)
#     # subprocess.call("mosquitto_pub -h 10.100.30.130 -t craneInfo/Boom/TipHeight -m 9", shell=True)
#     # subprocess.call("mosquitto_pub -h 10.100.30.130 -t craneInfo/Boom/Angle~p2 -m 7", shell=True)
#     # subprocess.call("mosquitto_pub -h 10.100.30.130 -t craneInfo/RCL/Hook/Radius~p2 -m 2", shell=True)
#     test.log("aaaaa")
# # print("hello world");
#
# # [
# #   {
# #     "componentText": "8400",
# #     "conditionText": "44",
# #     "deviceText": "3",
# #     "indexText": "141",
# #     "isDeletable": "false"
# #   },
# #   {
# #     "componentText": "8008",
# #     "conditionText": "44",
# #     "deviceText": "3",
# #     "indexText": "144",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "8904",
# #     "conditionText": "110",
# #     "deviceText": "3",
# #     "indexText": "144",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "8905",
# #     "conditionText": "110",
# #     "deviceText": "3",
# #     "indexText": "144",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7093",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "129",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7092",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "129",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7053",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "131",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7026",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "132",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7033",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "132",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7034",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "132",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7077",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "129",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7025",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "130",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7078",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "130",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7079",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "130",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7013",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "131",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7015",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "131",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7068",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "131",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7066",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "131",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "7099",
# #     "conditionText": "2",
# #     "deviceText": "3",
# #     "indexText": "131",
# #     "isDeletable": "true"
# #   },
# #   {
# #     "componentText": "8001",
# #     "conditionText": "51",
# #     "deviceText": "3",
# #     "indexText": "145",
# #     "isDeletable": "false"
# #   },
# #   {
# #     "componentText": "80013",
# #     "conditionText": "513",
# #     "deviceText": "33",
# #     "indexText": "1435",
# #     "isDeletable": "false"
# #   }
# # ]
# #
# # print("entering the testing stuff")
# # #huh = ctypes.cdll.LoadLibrary("/home/manitowoc/testGuiMqtt3/testing.so")
# # #huh = ctypes.CDLL("/home/manitowoc/testGuiMqtt3/testing.so")
# # # huh = ctypes.CDLL("/home/manitowoc/testGuiMqtt3/libhello.so")
# # # huh2 =  ctypes.cdll.LoadLibrary("/home/manitowoc/testGuiMqtt3/libhello.so")
# # # print(huh2)
# # # huh.hello();
# # # //huh2.hello()
# #
# # #subprocess.run("python3 /home/manitowoc/testGuiMqtt3/test.py")
# # print("aaaaa")
# # return_code = subprocess.call("python3 /home/manitowoc/testGuiMqtt3/test.py", shell=True)
# # print("aaaaa")
# # #huh.abc();
# # #huh.hello();
# # #huh2.hello()
# # #print(qMapDatabase)
