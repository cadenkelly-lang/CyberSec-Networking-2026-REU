# Cybersecurity Networking Training Modules — Summer 2026

## Project Overview

This repository contains documentation, diagrams, and training materials developed during my Summer 2026 research internship with the Alaska Center for Energy and Power (ACEP).

The project focuses on developing cybersecurity training modules for rural Alaskan Communities. The goal is to create accessible, cost-effective, hands-on cybersecurity education through a virtualized cyber range environment covering networking fundamentals (with a focus on network segmentation), system administration, and firewall configuration.

The training environment uses virtualization and network simulation to allow students to explore real-world networking and cybersecurity concepts in a controlled environment.

---

## Project Architecture

The project network architecture is documented at both the physical (Layer 1) and logical (Layer 3) levels.

### Layer 1 — Physical Network Architecture

The Layer 1 diagram shows the physical components of the training environment, including servers, switches, network connections, and hardware organization.

<img src="Diagrams/Training%20Ground%20Network%20Diagrams/6.26%20Final%20PTG%20Diagram.png" width="850">

### Layer 3 — Logical Network Architecture

The Layer 3 diagram shows the logical network design, including IP addressing, network segmentation, student stations, and firewall boundaries.

<img src="Diagrams/Training%20Ground%20Network%20Diagrams/jehaverlack-layer3-student-station.excalidraw.png" width="850">

---

## Training Modules

### Module 1 — Networking Fundamentals

Topics covered:

- Linux command line fundamentals
- IPv4 addressing and subnetting
- MAC addresses and network communication
- DHCP
- DNS
- NTP
- LAN
- Network segmentation

### Module 2 — Firewall Configuration and Security

Topics covered:

- Firewall concepts
- OPNsense services configuration
- >> DHCP/DNS/NTP configuration
- Firewall rules, configuration, testing
- Rule testing and validation

---

## Repository Structure
CyberSec-Networking-2026-Summer-Research-Internship/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── Diagrams/
│   ├── ACEP Intern Presentation Diagrams/
│   │
│   ├── Training Ground Network Diagrams/
│   │   ├── layer1-ptg-network.png
│   │   ├── layer3-student-network.png
│   │   ├── 6.26 Final PTG Diagram.md
│   │   └── other diagrams...
│   │
│   ├── Training Module 1 Diagrams/
│   │   └── ...
│   │
│   └── Training Module 2 Diagrams/
│       └── ...
│
├── Publications and Media/
│
├── Training Materials/
│   │
│   ├── Module 1/
│   │   ├── Instructor Notes/
│   │   ├── Student Guides/
│   │   └── Exercises/
│   │
│   └── Module 2/
│       ├── Instructor Notes/
│       ├── Student Guides/
│       └── Exercises/
│
├── Meetings/
│   └── ...
│
├── Notes for me and students/
│   └── ...
│
├── Daily Notes Starting 6.4/
│   └── ...
│
└── .obsidian/
    ├── app.json
    ├── appearance.json
    ├── community-plugins.json
    └── core-plugins.json
