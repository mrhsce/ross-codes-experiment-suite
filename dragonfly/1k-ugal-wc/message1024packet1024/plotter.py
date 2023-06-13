import csv, os
import matplotlib.pyplot as plt


packets_generated = []
packets_finished = []
messages_received = []
avg_chunk_latency = []
avg_message_latency = []
loads = [0.01,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

def draw_latency():
    label = 'Latency vs load'
    plt.figure()
    plt.xlabel("Load (fraction of EP output bitrate)")
    plt.ylabel("Latency (cycles - ns)")
    plt.title(label)
    plt.plot(loads, avg_chunk_latency, '-.', label=f"Chunk latency", marker='o')
    plt.plot(loads, avg_message_latency, '-.', label=f"Packet latency", marker='^')
    plt.legend()
    # plt.show()
    plt.savefig(label + ".png")
    plt.close()
    
def draw_chunk_latency():
    label = 'Chunk Latency vs load comparison'
    plt.figure()
    plt.xlabel("Load (fraction of EP output bitrate)")
    plt.ylabel("Chunk Latency (cycles - ns)")
    plt.title(label)
    plt.plot(loads, avg_chunk_latency, '-.', label=f"Chunk latency experiment", marker='o')
    plt.plot(loads, [280,280, 280, 290, 550, 1500, 2000, 2800, 3000, 3000, 2900], '-.', label=f"Chunk latency paper", marker='^')
    plt.legend()
    # plt.show()
    plt.savefig(label + ".png")
    plt.close()    

def draw_aggregate_rate():
    label = 'Packet and message generated vs load'
    plt.figure()
    plt.xlabel("Load (fraction of EP output bitrate)")
    plt.ylabel("Packet and message count")
    plt.title(label)
    plt.plot(loads, packets_generated, '-.', label=f"Generated packets", marker='o')
    plt.plot(loads, packets_finished, '-.', label=f"Finished packets", marker='^')
    plt.plot(loads, messages_received, '-.', label=f"Received messages", marker='p')
    plt.legend()
    # plt.show()
    plt.savefig(label + ".png")
    plt.close()

def draw_packet_rate():
    label = 'Packet generated vs load'
    plt.figure()
    plt.xlabel("Load (fraction of EP output bitrate)")
    plt.ylabel("Packet and message count")
    plt.title(label)
    plt.plot(loads, packets_generated, '-.', label=f"Generated packets", marker='o')
    plt.plot(loads, packets_finished, '-.', label=f"Finished packets", marker='^')
    plt.legend()
    # plt.show()
    plt.savefig(label + ".png")
    plt.close()

def draw_message_rate():
    label = 'Message generated vs load'
    plt.figure()
    plt.xlabel("Load (fraction of EP output bitrate)")
    plt.ylabel("Message count")
    plt.title(label)
    plt.plot(loads, messages_received, '-.', label=f"Received messages", marker='p')
    plt.legend()
    # plt.show()
    plt.savefig(label + ".png")
    plt.close()


with open('output.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        packets_generated.append(int(row['Packets generated']))
        packets_finished.append(int(row['Packets finished']))
        messages_received.append(int(row['Messages received']))
        avg_chunk_latency.append(int(row['avg chunk latency']))
        avg_message_latency.append(int(row['avg message latency']))


directory = 'graphs'  # Specify the directory name you want to create and check
if not os.path.exists(directory):
    os.makedirs(directory)
os.chdir(directory)

draw_message_rate()
draw_aggregate_rate()
draw_packet_rate()
draw_latency()
draw_chunk_latency()
