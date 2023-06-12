import os, re, csv
def extract_parameters(content):
    parameters = {}

    # Extract Running Time
    running_time_match = re.search(r'Running Time\s+=\s+(\d+\.\d+)', content)
    parameters['Running Time'] = running_time_match.group(1) if running_time_match else "Not found"

    # Extract Efficiency
    efficiency_match = re.search(r'Efficiency\s+([\d.]+)\s+%', content)
    parameters['Efficiency'] = efficiency_match.group(1) if efficiency_match else "Not found"

    # Extract hops traversed
    hops_traversed_match = re.search(r'Average number of hops traversed\s+(\d+\.\d+)', content)
    parameters['Hops Traversed'] = hops_traversed_match.group(1) if hops_traversed_match else "Not found"

    # Extract average chunk latency
    avg_chunk_latency_match = re.search(r'average chunk latency\s+(\d+\.\d+)', content)
    parameters['Average Chunk Latency'] = avg_chunk_latency_match.group(1) if avg_chunk_latency_match else "Not found"

    # Extract maximum chunk latency
    max_chunk_latency_match = re.search(r'maximum chunk latency\s+(\d+\.\d+)', content)
    parameters['Maximum Chunk Latency'] = max_chunk_latency_match.group(1) if max_chunk_latency_match else "Not found"

    # Extract average message latency
    avg_message_latency_match = re.search(r'Mean Message Latency:\s+(\d+\.\d+)', content)
    parameters['Mean Message Latency'] = avg_message_latency_match.group(1) if avg_message_latency_match else "Not found"

    # Extract maximum message latency
    max_message_latency_match = re.search(r'Maximum Message Latency:\s+(\d+\.\d+)', content)
    parameters['Maximum Message Latency'] = max_message_latency_match.group(1) if max_message_latency_match else "Not found"

    # Extract Total packets generated
    total_packets_generated_match = re.search(r'Total packets generated\s+(\d+)', content)
    parameters['Total Packets Generated'] = total_packets_generated_match.group(1) if total_packets_generated_match else "Not found"

    # Extract Total packets finished
    total_packets_finished_match = re.search(r'finished\s+(\d+)', content)
    parameters['Total Packets Finished'] = total_packets_finished_match.group(1) if total_packets_finished_match else "Not found"

    # Extract Total packets finished
    total_messages_received_match = re.search(r'Total Messages Received:\s+(\d+)', content)
    parameters['Total Messages Received'] = total_messages_received_match.group(1) if total_messages_received_match else "Not found"

    return parameters

def search_subdirectories(directory):
    with open('./output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Directory', 'Execution time', 'Efficiency', 'hops', 'avg chunk latency', 'max chunk latency', 'avg message latency', 'max message latency', 'Packets generated', 'Packets finished', 'Messages received'])

        text_files = [file for file in os.listdir(directory) if file.endswith(".txt")]
        text_files.sort()
        for file_name in text_files:
            file_path = os.path.join(directory, file_name)

            # Open the file for reading
            with open(file_path, 'r') as file:
                content = file.read()

            extracted_parameters = extract_parameters(content)

            # Retrieve individual parameters
            running_time = round(float(extracted_parameters['Running Time']),3)
            efficiency = extracted_parameters['Efficiency']
            hops_traversed = round(float(extracted_parameters['Hops Traversed']), 2)
            avg_chunk_latency = round(float(extracted_parameters['Average Chunk Latency']) * 1000)
            max_chunk_latency = round(float(extracted_parameters['Maximum Chunk Latency']) * 1000)
            avg_message_latency = round(float(extracted_parameters['Mean Message Latency']) * 1000)
            max_message_latency = round(float(extracted_parameters['Maximum Message Latency']) * 1000)
            total_packets_generated = extracted_parameters['Total Packets Generated']
            total_packets_finished = extracted_parameters['Total Packets Finished']
            total_messages_received = extracted_parameters['Total Messages Received']

            # Print the extracted values
            # print("Running Time:", running_time)
            # print("Efficiency:", efficiency)
            # print("Hops Traversed:", hops_traversed)
            # print("Average Chunk Latency:", avg_chunk_latency)
            # print("Maximum Chunk Latency:", max_chunk_latency)
            # print("Average Message Latency:", avg_message_latency)
            # print("Maximum Message Latency:", max_message_latency)
            # print("Total Packets Generated:", total_packets_generated)
            # print("Total Packets Finished:", total_packets_finished)
            # print("Total Messages Received", total_messages_received)
            writer.writerow([file_name, running_time, efficiency, hops_traversed, avg_chunk_latency, max_chunk_latency, avg_message_latency, max_message_latency, total_packets_generated, total_packets_finished, total_messages_received])
            print(f'\n {file_name} finished', total_messages_received)
# Example usage:
current_directory = os.getcwd()
search_subdirectories(current_directory)
