This project provides easier programs to learn OpenMP using C and C++. <br> <br> 
It uses gcc as the underlying C compiler. <br> <br>
Following commands can be used to compile and run an openmp program. <br>
&emsp; gcc -fopenmp program_name.c <br>
&emsp; ./a.out <br> <br>
Following command is required to compile the sobel filter file. <br>
&emsp; g++ 12_sobel_filter.cpp -fopenmp `pkg-config --cflags --libs opencv4` <br> <br>
To change number of threads, use the following command in terminal. <br> 
&emsp; export OMP_NUM_THREADS=count <br> 
&emsp; where, "count" is the number of threads you want to use in the program. 
