 # Extraction des donnees
         ![img1](../ProjetSAE1.05/PieChart01.png)
 ![img2](../ProjetSAE1.05/PieChart02.png)
 ![img3](../ProjetSAE1.05/PieChart03.png)
 #How to use the Tcp_dump_file_extraction:


Warning: This program can only extract informations from a tcp dump file, you can't use it for another type of file

==================================================================================================================

Before to run make sure that the programme and the tcp dump file are located on the same folder.
You must also rename your file "Dumpfile" ( it should have the .txt enxtension).
The programm is a python file, you can interpret it with a IDE or with your local python environement like
conda or anaconda. 
After you run it, the programm will make some time to extract all the data depending on the tcp-dump-file's size (~10mn if your file is higher than 25mo)

=================================================================================================================

After the programm is done you will get some files:
-------------------------------------------------

* Markdown file : You can delete it, it was just for making the html file
* HTML file : The graphics are exported in a html file
* CSV_file : The information are exported in csv file with 4 tables:
			? In the first table you have all the informations from the header of the frames ( Time,IPSRC,IPDST,SEQ,ACK,WIN.....)
			? In the second table all the routes (IPSRC==IPDST)
			? In the third table all the flags
			? In the fourth you have a combination of the routes and flags
---------------------------------------------------

To make appear the graphic you can do it manually or use the Macro file which accompanies the programm:

Open the macro_file in the folder macro and the csv file, enable the developper mode ( go to file --> more --> options --> ruaban --> check the developper mode)

Then go to macro and run the macro or use this shortcut : Ctrl+Shift+M

If you have this following error: "Becausse to your security...." Please go to the macro setting on the both file and make sure than the Enable all macro is checked,
try to reopen the file after that.

With this macro you'll have The 3 graphics of the TCP_dump_file

Here are some info on the acronym of the tcp flags:
Acronym 	Name 	Meaning
SYN 	Synchronization 	Used to create a TCP connection
ACK 	Acknowledgment 	Used to acknowledge the reception of data or synchronization packets
PSH 	Push 	Instruct the network stacks to bypass buffering
URG 	Urgent 	Indicates out-of-band data that must be processed by the network stacks before normal data
FIN 	Finish 	Gracefully terminate the TCP connection
RST 	Reset 	Immediately terminate the connection and drop any in-transit data

Thanks for reading