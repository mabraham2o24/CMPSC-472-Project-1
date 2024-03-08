# **Multi-Process/Threads Manager with IPC and Parallel Text File Processing**

# ***Description of the project***
+ I did this project in python. It creates an operating system environment with features like managing processes, threads, inter-process communication (IPC), and parallel text file processing. Users can create, terminate, suspend, and resume processes and threads, while also sending messages between them. The project focuses on hands-on learning of system resource utilization, communication protocols, and parallel computing concepts, providing insights into operating system functionalities and performance metrics. It serves as a practical tool for understanding process management, communication, and text processing in a simulated environment. For the sake of this project for 2 of the 3 features I implemented some test cases myself to test out the code while for the managing threads feature I have the user choose from the multiple options. 
  
# ***Structure of the code with diagram and some descriptions regarding structure***
+ ***Main Program:***
  + Tests out features 2 and 3 - Inter-Process Communication (IPC) Mechanisms and Parallel Text File Processing
  + It prints out the menu for the users to choose options from.
  + Based on the user's choice it will call the appropriate functions.

+ ***Process Manager:***
  + The Process Manager is responsible for managing processes and threads within the system.
  + It maintains a list of processes and provides methods to create, terminate, suspend, resume, and display processes and threads.

+ ***Process Class:***
  + Each process in the system is represented by an instance of the Process Class.
  + It contains attributes such as a unique Process ID and a list of associated threads.
  + The Process Class provides methods to manage threads within the process, such as creating and terminating threads.
    
+ ***Thread Class:***
  + Individual threads within each process are represented by instances of the Thread Class.
  + Each thread has attributes such as a unique Thread ID and a status indicating whether it is running, suspended, or terminated.
  + The Thread Class provides methods to manipulate the status of threads, such as suspending or resuming them.
    
![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/105bd2eb-5233-4a04-9b7b-03eda41e68df)

----------------------------------------------------

# ***Instructions on how to use the program***
+ Download the zip file from github. Once it is downloaded you should find it in your downloads.
  ![Screenshot 2024-03-08 015741](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/56d6d595-8608-48c4-a402-8c69a57e16f6)

+ Right click on the zipped file and hit "extract all."
+ ![Screenshot 2024-03-08 011251](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/0911d459-4531-4186-8197-39003d37158f)
  
+ Hit "extract" and it will extract all the files within the zipped file into a folder in the same location under the same name.
+ ![Screenshot 2024-03-08 011408](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/7f7101ac-5fc9-47ed-91fc-ea98250fc755)
+ ![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/15368a0a-2e85-4bd9-8ae3-cc413c2a0de6)
  
+ Once the folder has been unzipped, open the folder. You will see another folder inside of it. This is the folder we have to go into to run the program.
+ ![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/9ddede00-b940-414f-8253-63a7f4f8f976)
  
+ Right click on the folder and click on the command called "Copy as Path." This copies the path of the folder which we need in a few to run the program.
+ ![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/ef1ff55e-d036-4002-b2c0-cc3bd555e9b4)
  
+ Now open up the command prompt/terminal of your computer.
+ Type in the command "cd" and then paste the path we just copied. It will look something like this:
+ ![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/d5fc128d-be69-45f7-9b9d-5f8a77b5acdd).
  
+ Hit enter and now you are in the folder(directory). To confirm you are in the folder your terminal line should look like this:
+ ![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/8205c1dd-1494-4886-b9f8-7b3498dce57f)
  
+ Now, run the command "python 472Project1.py". This is the name of our python file and will run the program.
+ ![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/2460dcef-4dcc-4683-b381-7c85e6b1b532)
  
+ Choosing option 1 will prompt you to another menu where you can choose different options such as creating a thread, killing a thread, creating a process, etc.
+ ![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/6dabb026-a9d9-401e-8c1d-388cbd6bcf59)
  
+ You can exit the thread manager menu by entering '8' which will take you back to the main menu.
+ If you choose option 2 it will run some of the test cases I have in place to test out the IPC function using some short and long messages.
+ ![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/94e63c2e-69e2-4b81-b97a-21a63a837319)
  
+ If you choose option 3 then it will read through a text file(data.txt) and uppercase all the letters, count the frequences, etc.
+ ![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/b545c373-fc7f-4386-94a3-b71edf13b988)
  
+ Last but not least if you hit option 4 that will just exit you from the program. 

----------------------------------------------------

# ***Validity of the implemented functionalities.***
+ To validate the code I looked at different resources out there to see if I am approaching this right. I also went through the code line by line and tried to catch any issues. I strcutured the code as organized as possible by create different classes, functions, etc. for the different features and what each feature has to do. This way if I had an error it was easier to catch exactly where the error is coming from throughout the process. Keeping an organized code structures helps to iterate through the functions and code in the case we had to check anything over again. Also it is easier to see how the process is being carried out. Below I did include screenshots of the most important classes and functions. If more is needed you can find it in the py file attatched to this github. 
  
+ ***Code Structure: Classes, functions, etc.***
+ ![Screenshot 2024-03-08 013402](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/6fcb9bc3-1325-459e-8f1a-e5aba4525a42)
+ ![Screenshot 2024-03-08 013414](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/cd59b413-51b9-44e1-9728-40cf8505af59)
+ ![Screenshot 2024-03-08 013433](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/5e3bab59-611f-4639-91a1-c6b5c3b1cc04)
+ ![Screenshot 2024-03-08 013442](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/bdcf32a3-1048-4e05-9ed1-6858ea8db751)
+ ![Screenshot 2024-03-08 013457](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/49c7f502-446c-45a8-b884-15e2fa5b61bc)

+ ***Testing the Code:***
+ ![Screenshot 2024-03-08 013708](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/8f03a851-3845-4ca9-8ab3-1b21a08ab340)
  
+ This screenshot below is just some of the tests I have written and commented out to test out the thread managing(option 1).
+ ![image](https://github.com/mabraham2o24/CMPSC-472-Project-1/assets/143213640/2994285a-e7e5-4ff8-a8f8-63c428835682)

-----------------------------------------------------

# ***Findings, Complications, etc.***
+ Through the implementation of features like multi-process and thread management, inter-process communication, and text file processing, I gained a better understanding how all of those functions/features work. By measuring execution times, resource utilization, and scalability with increasing file sizes, I was able to visualize the performance of different components of the system, such as process/thread management and file processing. Calculating the time helped me track the performance of IPC mechanisms like shared memory and message passing by evaluating their efficiency with short and long messages. I saw how the times for the shorter messages were a bit shorter than the longer meassages likely because shorter messages can have less overhead while the longer ones could need more time and resources. 

+ I did not have serious loads of complications but one major one I had was when I was trying to do all of this in the C language. The way I was trying to do was by creating a cpp file and h file for each function(feature) and then calling it in a main.cpp file. When I was trying to do this the functions were not getting called correctly because of the way I created the files. I got confused with the multiple files and it was hard to keep track of everything. This is why I switched to python. It was a bit harder to implement all the functions but I did it by doing a bit research and trying to follow the same principles I would if I were to do it in C.

---------------------------------------------------

+ # ***Resources***
+ ***Threading, Operating Systems, etc.***
  + https://www.geeksforgeeks.org/multithreading-in-operating-system/
  + https://www.geeksforgeeks.org/multi-threading-models-in-process-management/
  + https://www.geeksforgeeks.org/difference-between-multi-tasking-and-multi-threading/
  + https://realpython.com/intro-to-python-threading/
  + https://docs.python.org/3/library/multiprocessing.html
  + https://www.geeksforgeeks.org/multiprocessing-python-set-1/
  + https://www.geeksforgeeks.org/multiprocessing-python-set-2/
    
+ ***Parallel Text File Processing***
  + https://www.kdnuggets.com/2022/07/parallel-processing-large-file-python.html
  + https://www.geeksforgeeks.org/change-case-of-all-characters-in-a-txt-file-using-python/

+ ***IPC***
  + https://www.geeksforgeeks.org/inter-process-communication-ipc/

