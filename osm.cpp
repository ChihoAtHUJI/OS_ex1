//
// Created by Chiho Song on 21/03/2021.
//

#include <iostream>
#include "osm.h"
#include <sys/time.h>

void empty(){}

double osm_operation_time(unsigned int iterations){
    if (iterations == 0){
        return -1;
    }
    unsigned int x = 0;
    double retVal;
    struct timeval start, end;
    gettimeofday(&start, NULL);
    for (unsigned int i = 0; i < iterations; i+=5){
        x = x + 1;
        x = x + 1;
        x = x + 1;
        x = x + 1;
        x = x + 1;
    }
    gettimeofday(&end, NULL);
    retVal = (double)((end.tv_sec-start.tv_sec)*1000000 +(end.tv_usec-start.tv_usec))/(iterations);
    // need to multiply 1000 to change unit into nanosecond
    return retVal*1000;
}

double osm_function_time(unsigned int iterations){
    if (iterations == 0){
        return -1;
    }
    double retVal;
    struct timeval start, end;
    gettimeofday(&start, NULL);
    for (unsigned int i = 0; i < iterations; i+=5){
        empty();
        empty();
        empty();
        empty();
        empty();
    }
    gettimeofday(&end, NULL);
    retVal = (double)((end.tv_sec-start.tv_sec)*1000000 + (end.tv_usec-start.tv_usec))/(iterations);
    return retVal*1000;
}

double osm_syscall_time(unsigned int iterations){
    if (iterations == 0){
        return -1;
    }
    double retVal;
    struct timeval start, end;
    gettimeofday(&start, NULL);
    for (unsigned int i = 0; i < iterations; i+=5){
        OSM_NULLSYSCALL;
        OSM_NULLSYSCALL;
        OSM_NULLSYSCALL;
        OSM_NULLSYSCALL;
        OSM_NULLSYSCALL;
    }
    gettimeofday(&end, NULL);
    retVal = (double)((end.tv_sec-start.tv_sec)*1000000 +(end.tv_usec-start.tv_usec))/(iterations);
    return retVal*1000;
}


int main(int argc, char** argv) {
    
    if (argc != 2){
        std::cout << "Invalid Argument Number" << std::endl;
        return -1;
    }

    unsigned long ul = std::stoul (argv[1], nullptr, 0);
    std::cout <<"Operation time: " << osm_operation_time(ul) << std::endl;
    std::cout <<"Function time: " << osm_function_time(ul) << std::endl;
    std::cout <<"Trap time: " <<osm_syscall_time(ul) << std::endl;

    return 0;
}
