<!-- =========================================================================================
                                     HEADER SECTION
     ========================================================================================= -->
<div align="center">

  # Computer Network Lab

  ### CSL502 · Semester V · Computer Engineering

  [![Curated by](https://img.shields.io/badge/Curated%20by-Amey%20Thakur-blue.svg)](https://github.com/Amey-Thakur)
  [![Programs](https://img.shields.io/badge/Programs-10-yellowgreen.svg)](#laboratory-experiments)
  [![Language](https://img.shields.io/badge/Language-Python%20%7C%20Cisco-blueviolet.svg)](./CISCO/)

  **A collection of network topology simulations and socket programming implementations covering LAN, Star, Ring, Tree, Hybrid topologies, OSPF routing, FTP configuration, and TCP/UDP communication.**

  ---

  **[📂 Experiment 1](#-experiment-1-network-topologies)** &nbsp;·&nbsp; **[⭐ Experiment 2](#-experiment-2-star-topology)** &nbsp;·&nbsp; **[🔄 Experiment 3](#-experiment-3-ring-topology)** &nbsp;·&nbsp; **[🌳 Experiment 4](#-experiment-4-tree-topology)** &nbsp;·&nbsp; **[📁 Experiment 5](#-experiment-5-ftp-configuration)** &nbsp;·&nbsp; **[🔀 Experiment 6](#-experiment-6-ospf-routing)** &nbsp;·&nbsp; **[💻 Experiment 7](#-experiment-7-socket-programming)** &nbsp;·&nbsp; **[🔍 Experiment 8](#-experiment-8-error-detection)** &nbsp;·&nbsp; **[🔗 Experiment 9](#-experiment-9-hybrid-topology)** &nbsp;·&nbsp; **[🌐 Experiment 10](#-experiment-10-network-simulation)** &nbsp;·&nbsp; **[🚀 How to Use](#-how-to-use)** &nbsp;·&nbsp; **[📖 Learning Path](#-learning-path)**

</div>

---

> [!TIP]
> **Network Testing**: Use the `ping` command within Cisco Packet Tracer's CLI to verify connectivity between devices. For socket programming, always start the server before the client, and ensure both are running on the same port (default: 9999).

> [!WARNING]
> **Cisco Packet Tracer Required**: The `.pkt` files require [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer) software to open. For Python socket programs, ensure no firewall is blocking localhost connections on port 9999.

---

<!-- =========================================================================================
                                     EXPERIMENT 1
     ========================================================================================= -->
## 📂 Experiment 1: Network Topologies

Implementation of basic LAN configuration using Cisco Packet Tracer to understand network fundamentals.

| # | Program | Description | Source Code |
|:---|:---|:---|:-:|
| 1 | [CN_LAN.pkt](CISCO/CN_LAN.pkt) | LAN Configuration using switches and routers | [View](CISCO/CN_LAN.pkt) |
| 📄 | [Lab Report](Experiments/Amey_B-50_CN_Experiment-1.pdf) | Detailed experiment report | [View](Experiments/Amey_B-50_CN_Experiment-1.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT 2
     ========================================================================================= -->
## ⭐ Experiment 2: Star Topology

Implementation of Star network topology where all nodes connect to a central hub/switch.

| # | Program | Description | Source Code |
|:---|:---|:---|:-:|
| 1 | [CN_STAR.pkt](CISCO/CN_STAR.pkt) | Star Network with central switch | [View](CISCO/CN_STAR.pkt) |
| 📄 | [Lab Report](Experiments/Amey_B-50_CN_Experiment-2.pdf) | Detailed experiment report | [View](Experiments/Amey_B-50_CN_Experiment-2.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT 3
     ========================================================================================= -->
## 🔄 Experiment 3: Ring Topology

Implementation of Ring network topology where each node connects to exactly two other nodes.

| # | Program | Description | Source Code |
|:---|:---|:---|:-:|
| 1 | [CN_RING.pkt](CISCO/CN_RING.pkt) | Ring Network Configuration | [View](CISCO/CN_RING.pkt) |
| 📄 | [Lab Report](Experiments/Amey_B-50_CN_Experiment-3.pdf) | Detailed experiment report | [View](Experiments/Amey_B-50_CN_Experiment-3.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT 4
     ========================================================================================= -->
## 🌳 Experiment 4: Tree Topology

Implementation of hierarchical Tree topology combining characteristics of Star and Bus topologies.

| # | Program | Description | Source Code |
|:---|:---|:---|:-:|
| 1 | [CN_TREE.pkt](CISCO/CN_TREE.pkt) | Hierarchical Tree Network Design | [View](CISCO/CN_TREE.pkt) |
| 📄 | [Lab Report](Experiments/Amey_B-50_CN_Experiment-4.pdf) | Detailed experiment report | [View](Experiments/Amey_B-50_CN_Experiment-4.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT 5
     ========================================================================================= -->
## 📁 Experiment 5: FTP Configuration

Configuration of File Transfer Protocol (FTP) server and client for file sharing across the network.

| # | Program | Description | Source Code |
|:---|:---|:---|:-:|
| 1 | [CN_FTP.pkt](CISCO/CN_FTP.pkt) | FTP Server Setup and Configuration | [View](CISCO/CN_FTP.pkt) |
| 📄 | [Lab Report](Experiments/Amey_B-50_CN_Experiment-5.pdf) | Detailed experiment report | [View](Experiments/Amey_B-50_CN_Experiment-5.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT 6
     ========================================================================================= -->
## 🔀 Experiment 6: OSPF Routing

Implementation of Open Shortest Path First (OSPF) dynamic routing protocol for efficient packet routing.

| # | Program | Description | Source Code |
|:---|:---|:---|:-:|
| 1 | [CN_OSPF.pkt](CISCO/CN_OSPF.pkt) | OSPF Dynamic Routing Implementation | [View](CISCO/CN_OSPF.pkt) |
| 📄 | [Lab Report](Experiments/Amey_B-50_CN_Experiment-6.pdf) | Detailed experiment report | [View](Experiments/Amey_B-50_CN_Experiment-6.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT 7
     ========================================================================================= -->
## 💻 Experiment 7: Socket Programming

Implementation of TCP Client-Server communication using Python socket library.

| # | Program | Description | Source Code |
|:---|:---|:---|:-:|
| 1 | [TCP_Server.py](CISCO/Socket%20Programming/TCP_Server.py) | TCP Server Implementation | [View](CISCO/Socket%20Programming/TCP_Server.py) |
| 2 | [TCP_Client.py](CISCO/Socket%20Programming/TCP_Client.py) | TCP Client Implementation | [View](CISCO/Socket%20Programming/TCP_Client.py) |
| 📄 | [Lab Report](Experiments/Amey_B-50_CN_Experiment-7.pdf) | Detailed experiment report | [View](Experiments/Amey_B-50_CN_Experiment-7.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT 8
     ========================================================================================= -->
## 🔍 Experiment 8: Error Detection

Implementation of Cyclic Redundancy Check (CRC) algorithm for error detection in data transmission.

| # | Program | Description | Source Code |
|:---|:---|:---|:-:|
| 1 | [CRC_Error_Detection.py](CISCO/CRC_Error_Detection.py) | CRC Algorithm Implementation | [View](CISCO/CRC_Error_Detection.py) |
| 📄 | [Lab Report](Experiments/Amey_B-50_CN_Experiment-8.pdf) | Detailed experiment report | [View](Experiments/Amey_B-50_CN_Experiment-8.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT 9
     ========================================================================================= -->
## 🔗 Experiment 9: Hybrid Topology

Implementation of Hybrid topology combining Bus and Star topologies for practical network design.

| # | Program | Description | Source Code |
|:---|:---|:---|:-:|
| 1 | [AMEY_B-50_CN_EXAM_HYBRID_TOPOLOGY.pkt](CISCO/AMEY_B-50_CN_EXAM_HYBRID_TOPOLOGY.pkt) | Hybrid Topology (Bus + Star) | [View](CISCO/AMEY_B-50_CN_EXAM_HYBRID_TOPOLOGY.pkt) |
| 📄 | [Lab Report](Experiments/Amey_B-50_CN_Experiment-9.pdf) | Detailed experiment report | [View](Experiments/Amey_B-50_CN_Experiment-9.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT 10
     ========================================================================================= -->
## 🌐 Experiment 10: Network Simulation

Complete network setup and simulation combining all learned concepts.

| # | Program | Description | Source Code |
|:---|:---|:---|:-:|
| 📁 | [All Packet Tracer Files](CISCO/) | Complete network simulation files | [View](CISCO/) |
| 📄 | [Lab Report](Experiments/Amey_B-50_CN_Experiment-10.pdf) | Detailed experiment report | [View](Experiments/Amey_B-50_CN_Experiment-10.pdf) |

---

<!-- =========================================================================================
                                     HOW TO USE SECTION
     ========================================================================================= -->
## 🚀 How to Use

### For Cisco Packet Tracer Files (.pkt)

1. **Install Cisco Packet Tracer** from [Cisco Networking Academy](https://www.netacad.com/courses/packet-tracer).
2. **Open** the `.pkt` file in Cisco Packet Tracer.
3. **Simulate** the network by clicking the "Simulation" tab.
4. **Test connectivity** using the ping command or PDU (Protocol Data Unit).

### For Python Programs

1. **Install Python 3.x** from [python.org](https://www.python.org/).
2. **Navigate** to the program directory.
3. **Run the server first**:
   ```bash
   python TCP_Server.py
   ```
4. **Run the client** in a separate terminal:
   ```bash
   python TCP_Client.py
   ```

---

<!-- =========================================================================================
                                     LEARNING PATH SECTION
     ========================================================================================= -->
## 📖 Learning Path

**Beginner Level:**
- Start with **Experiments 1-4** to understand basic network topologies (LAN, Star, Ring, Tree).
- Practice creating simple networks in Cisco Packet Tracer.

**Intermediate Level:**
- Explore **Experiments 5 & 6** to learn application layer protocols (FTP) and routing (OSPF).
- Understand how data flows across complex networks.

**Advanced Level:**
- Study **Experiments 7 & 8** for socket programming and error detection algorithms.
- Master **Experiments 9 & 10** for hybrid network design and complete simulations.

---

<!-- =========================================================================================
                                     FOOTER SECTION
     ========================================================================================= -->
<div align="center">

  <!-- Footer Navigation -->
  **[⬆ Back to Top](#computer-network-lab)**

  **[📂 Experiment 1](#-experiment-1-network-topologies)** &nbsp;·&nbsp; **[⭐ Experiment 2](#-experiment-2-star-topology)** &nbsp;·&nbsp; **[🔄 Experiment 3](#-experiment-3-ring-topology)** &nbsp;·&nbsp; **[🌳 Experiment 4](#-experiment-4-tree-topology)** &nbsp;·&nbsp; **[📁 Experiment 5](#-experiment-5-ftp-configuration)** &nbsp;·&nbsp; **[🔀 Experiment 6](#-experiment-6-ospf-routing)** &nbsp;·&nbsp; **[💻 Experiment 7](#-experiment-7-socket-programming)** &nbsp;·&nbsp; **[🔍 Experiment 8](#-experiment-8-error-detection)** &nbsp;·&nbsp; **[🔗 Experiment 9](#-experiment-9-hybrid-topology)** &nbsp;·&nbsp; **[🌐 Experiment 10](#-experiment-10-network-simulation)** &nbsp;·&nbsp; **[🚀 How to Use](#-how-to-use)** &nbsp;·&nbsp; **[📖 Learning Path](#-learning-path)**

  <br>

  **[🏠 Back to Main Repository](../)**

</div>

---

<div align="center">

  ### [Computer Network Lab](https://github.com/Amey-Thakur/COMPUTER-NETWORK-AND-COMPUTER-NETWORK-LAB/tree/main/Computer%20Network%20Lab)

  **CSL502 · Semester V · Computer Engineering**

  *University of Mumbai · Curated by [Amey Thakur](https://github.com/Amey-Thakur)*

</div>
