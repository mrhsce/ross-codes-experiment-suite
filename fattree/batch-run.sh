#!/bin/bash

# Get the root directory using the current working directory
root_directory=$(pwd)

# Find all directories containing a run.sh file
directories=$(find "$root_directory" -type f -name "*.conf" -exec dirname {} \;)

# Iterate through the directories
for directory in $directories; do
    # Change to the directory
    cd "$directory"

    echo -e "\n------------ Start -------------\n"
    echo "Execution in $directory."
    start_time=$(date +%s)

    mpirun --map-by core -np 12 ../../../build/bin/model-net-synthetic-fattree --extramem=200000 --synch=3 --traffic=1 --load=0.1 --payload_sz=32  -- ./modelnet-mpi-test-fattree.conf > results.txt &

    #sleep 0.1s ! This is important to catch the PIDs successfully!
    sleep 1

    # Capture the PID of the mpirun process
    PIDS=$(pgrep "model-net-synth")

    # Monitor the CPU and memory usage of all MPI ranks using pidstat
    #pidstat -p $(echo "$PIDS" | tr '\n' ',') -u -r -h -d 1
     pidstat -p $(echo "$PIDS" | tr "\n" ",") -r 1 > $(pwd)/cpu_RAM.txt  #Must use absolute path here !

    end_time=$(date +%s)
    execution_time=$((end_time - start_time))

    # Print the execution time
    echo -e "\nExecution time: $execution_time seconds"

    echo -e "\n------------- End -------------"
done

cd "$root_directory"
python3 ./output.py