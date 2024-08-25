import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta
# Title
st.subtitle("Umesh Kumar Kumawat")
# st.markdown("---")

# Contact Information
st.write(""" 
**Date Of Birth:** 12-Aug-1992  
**📞:** +91 9664308014  
**📧:** [umeshsingatiya@gmail.com](mailto:umeshsingatiya@gmail.com)
""")
st.markdown("---")

# Career Objective
st.header("Career Objective")
st.write("""
Passionate about addressing infrastructure challenges in India's electricity domain by digitizing management information systems (MIS) and reducing electricity losses. Seeking to leverage extensive experience in smart metering, software development, and project management to drive innovative solutions in the industry.
""")
st.markdown("---")

# Key Achievements
st.header("Key Achievements")
st.write("""
- 🧪Successfully led the Site acceptance Test (SAT) of 50K smart meters.
- 📈Managed the Service level agreements (SLA) 
- 🛠️Successfully led the deployment of 60K RF and GPRS smart meters across 60,000 sq km in Ladakh, overcoming extreme environmental challenges.
- 🛠️Managed the installation and operations of 40K smart meters in Gaya, Bihar, driving significant improvements in electricity distribution efficiency.
- 📐Architected and led the backend infrastructure for embedded DCUs, enhancing the scalability and reliability of smart metering systems.
""")
st.markdown("---")

# Professional Experience
st.header("Professional Experience")

st.subheader("Polaris Smart Metering (2014 - Present)")

st.write("""
**HES Development Engineer**  
_Dec 2023 - Present_  
- Currently leading the development of Head-End Systems (HES) for UPPCL, Manipur, and West Bengal, focusing on enhancing data management and system integration.
""")

st.write("""
**Senior Project Manager & Deputy General Manager**  
_Ladakh Power Development & Distribution (LPDD) - AMISP Project_  
_April 2023 - Nov 2023_  
- Spearheaded the installation of 60K RF and GPRS smart meters, optimizing metering infrastructure in one of India's most challenging regions.
- Directed a multi-disciplinary team, ensuring project milestones were met on time and within budget.
- Enhanced communication networks using RF planning and canopy creation to ensure robust meter connectivity across vast distances.
""")

st.write("""
**Project Manager**  
_SBPDCL Project - Gaya, Bihar_  
_2021 - 2022_  
- Oversaw the deployment of 40K smart meters, ensuring precise installation and integration into the existing grid.
- Coordinated with cross-functional teams to streamline operations, resulting in a significant reduction in electricity losses.
""")

st.write("""
**Embedded DCU Backend Infrastructure Architect & Team Lead**  
_2019 - 2020_  
- Led a team in the development and implementation of backend systems for embedded DCUs, improving system performance and scalability.
- Collaborated with developers to refine software solutions, ensuring seamless integration with existing infrastructure.
""")

st.write("""
**Linux DCU/Gateway Software Developer & IT Support**  
_2016 - 2018_  
- Developed and maintained software for Linux-based DCUs and Gateways, supporting critical smart metering projects.
- Provided backend IT support across multiple projects, ensuring system reliability and uptime.
""")

st.write("""
**Field Operations Engineer**  
_2014 - 2016_  
- Managed on-ground operations for the deployment of smart metering systems, ensuring successful implementation in diverse environments.
""")

st.markdown("---")

# Education
st.header("Education")
st.write("""
**B.Tech in Electrical Engineering**  
B.K. Birla Institute of Engineering and Technology, Pilani  
_2010 - 2014_
""")
st.markdown("---")

# Core Competencies
st.header("Core Competencies")
st.write("""
- **AMISP Project Management**: Large-scale meter deployment, remote and challenging terrain execution, cross-functional team leadership.
- **RF Communication Protocols**: Expertise in Tiny Mesh, Wirepas for efficient communication in AMI networks.
- **Infrastructure Development**: Embedded systems architecture, backend infrastructure, HES development.
- **Data Management**: Proficient in MySQL, PostgreSQL, Redis, Kafka.
- **Technical Tools**: NMS, HES, MDMS, VMS, WFM, Grafana, Streamlit.
- **Programming**: Python, Go (beginner), Shell scripts, Embedded tools (Arduino, ESP8266).
- **Software & IDEs**: Git, FogBugz, Jira, DataGrip, VSCode.
""")
st.markdown("---")

# Self-Declaration
st.header("Self-Declaration")
st.write(f"""
I, Umesh Kumar Kumawat, hereby declare that all the information provided above is true to the best of my knowledge and belief. I understand that any false information or misrepresentation may lead to the rejection of my application or termination of my employment.

**Date:** {str(datetime.datetime.utcnow()+relativedelta(minutes=330)).split('.')[0]}  
**Place:** [Your Location]
""")
