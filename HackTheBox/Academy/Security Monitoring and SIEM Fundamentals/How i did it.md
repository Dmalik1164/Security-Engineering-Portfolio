## Hack The Box — SIEM & Kibana Walkthrough

## Overview

As part of the Hack The Box SIEM Fundamentals module, I worked through creating and modifying live SIEM visualisations using the Elastic Stack (Elasticsearch, Kibana, Logstash, and Beats).

The goal was to gain hands-on experience with:
- Kibana dashboards
- KQL (Kibana Query Language)
- Filtering Windows event logs
- Creating visualisations
- Investigating failed authentication events

---

# Environment Setup

I launched the Hack The Box Pwnbox and accessed Kibana through the target machine using:

```bash
http://[TARGET_IP]:5601
```

From there, I navigated through the Kibana dashboards and Discover sections to begin querying and analysing Windows log data.

---

# SIEM Investigation & Visualisation

Following the HTB walkthrough, I created and modified SIEM visualisations using Kibana Lens and table-based visualisations.

The workflow included:
- Selecting the `windows*` index pattern
- Setting the appropriate timeframe
- Filtering specific Windows event IDs
- Creating table visualisations
- Sorting and displaying the top 1000 values in descending order
- Adding multiple fields and filters to refine investigation results

---

# KQL Queries & Filters

I used KQL queries and filters to identify:
- Failed login attempts (`4625`)
- Disabled account authentication attempts
- Username activity
- Logon types
- Hostnames associated with authentication events

Example filters used:

```kql
event.code:4625
```

```kql
winlog.event_data.SubStatus:0xc0000072
```

These filters allowed me to isolate failed logon attempts against disabled accounts and investigate related activity.

---

# Dashboard & Visualisation Editing

I modified existing visualisations and experimented with:
- Table layouts
- Metrics
- Row grouping
- Field aggregation
- Top value sorting
- Logon type categorisation

This helped me better understand how Elastic can be used to:
- Organise security data
- Categorise authentication events
- Build SOC-style monitoring dashboards
- Investigate suspicious activity within a SIEM environment

---

# Skills Learned

Through this lab I gained practical exposure to:
- Kibana navigation
- SIEM workflows
- KQL filtering
- Windows event log analysis
- Dashboard creation/editing
- SOC investigation techniques
- Visualising authentication-related events

---

# Key Takeaway

This exercise gave me hands-on experience using Elastic as a live SIEM platform and improved my understanding of how SOC analysts investigate, filter, and visualise security events in real-world environments.

This exercise gave me hands-on experience using Elastic as a live SIEM platform and improved my understanding of how SOC analysts investigate, filter, and visualise security events in real-world environments.
