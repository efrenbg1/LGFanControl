## LG Gram Automatic Fan Control

#### Why?
> New LG Grams with 13th gen CPUs are hot. Nothing we can change there.
> 
> When connected to the AC, even normal browsing will keep the cooling fan ON most of the time which can be quite annoying. LG provides four modes for cooling, but changing between them all the time is just a pain in the ass...

#### What does it do?
> To solve it I've created a Python script which reads the temperature every 15 seconds and switches between Normal and Silent mode automatically.

#### How it works?
> To read the CPU package temperature I use `LibreHardwareMonitorLib.dll`
>
> To change between cooling modes we need two DLLs:
> 1. `WMIConn.dll`: provides the communication to WMI
> 1. `WindowsControl.dll`: contains the interesting functions to change the cooling mode (and much more things!)
>
> Both DLLs are located under the directory `C:\Program Files (x86)\LG Software\LG Smart Assistant`
>
> To visualize the available functions you can use (is free): https://www.jetbrains.com/es-es/decompiler/
>
> The program must run as ADMIN, to have it run on startup you can use Task Scheduler in Windows. An example of the task can be found in the file `WindowsTask.xml`. You can import it directly into the Task Scheduler

Many thanks @Falcosc for the idea on how to change the modes from powershell: https://www.reddit.com/r/LGgram/comments/vgy9l1/2021_gram_does_anyone_know_how_to_set_the_battery/?utm_source=share&utm_medium=web2x&context=3