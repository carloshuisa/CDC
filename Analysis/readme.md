# Project Analysis
## 1. Disaster Analysis
We compared the number of disasters that happened in the US since 2000 with the vulnerability level average for each state to see the states we should focus on more in the future. We found that Texas was the state with the highest vulnerability level and the number of disasters. Also, we did the same analysis for each county in North Carolina and Texas.

## 2. COVID-19 Analysis
We created a Vulnerability Level (High, Medium, and Low) variable using the F_TOTAL variable provided by the SVI dataset. We chose the thresholds to create this variable by looking at the percentiles (0.3 and 0.7) of the F_TOTAL variable. We matched this Vulnerability Level with each county in the COVID-19 dataset. Then we analyzed how the COVID-19 cases and deaths increased differentiated by Vulnerability Level. We found that the groups with the highest Vulnerability Level had increased their COVID-19 cases and deaths faster than those with a lower Vulnerability Level. We also made some summary statistics for each Vulnerability Level to see how different they are for each social variable provided by the CDC.
