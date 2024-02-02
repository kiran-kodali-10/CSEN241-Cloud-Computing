#!/bin/bash

# Define test cases
declare -a testCases=(
    "cpu --cpu-max-prime=30000"
    "cpu --cpu-max-prime=50000"
    "memory --memory-block-size=2K"
    "memory --memory-block-size=4K"
    "fileio --file-test-mode=rndrw --file-total-size=3G"
    "fileio --file-test-mode=seqwr --file-total-size=3G"
)

# Iterate over test cases
for testCase in "${testCases[@]}"; do
    # Parse test case into individual components
    read -r currentTestMode currentParameter currentValue <<<"$testCase"
    
    # Display information about the current test case
    echo "Running sysbench with Mode: $currentTestMode, Parameter: $currentParameter, Value: $currentValue"

    # Generate a unique output filename for storing results
    currentOutputFilename="${currentTestMode}_${currentParameter}_${currentValue// /}.txt"

    # Prepare for fileio test if applicable
    if [[ $currentTestMode == "fileio" ]]; then
        sysbench fileio --file-total-size=3G --time=30 $currentParameter prepare
    fi

    # Run sysbench for each test case multiple times
    for ((runNumber=1; runNumber<=5; runNumber++)); do
        # Display run information
        echo "Run $runNumber:" | tee -a "$currentOutputFilename"
        echo "Command: sysbench $currentTestMode $currentParameter $currentValue run" >> "$currentOutputFilename"

        # Execute sysbench and capture results
        results=$(sysbench $currentTestMode $currentParameter $currentValue --time=30 run)

        # Display results and append them to the output file
        echo "Results:" | tee -a "$currentOutputFilename"
        echo "$results" | tee -a "$currentOutputFilename"
        echo "----------------------------------------"| tee -a "$currentOutputFilename"
    done

    # Cleanup after fileio test if applicable
    if [[ $currentTestMode == "fileio" ]]; then
        sysbench fileio --file-total-size=3G --time=30 $currentParameter cleanup
    fi

done
