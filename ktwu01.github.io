commit 8df2409feb7ecb20ec944adf0208305832dde8f4
Author: Cursor Agent <cursoragent@cursor.com>
Date:   Tue Jul 22 08:03:40 2025 +0000

    Update website with Koutian Wu's geoscience research information
    
    - Updated author bio and contact information
    - Rewrote About page with detailed research interests and projects
    - Updated CV with education, skills, and achievements
    - Added publications: JGR meteor paper and space physics education review
    - Created portfolio entries for Noah-MP and Tonga volcano projects
    - Added teaching/education framework information
    - Added AGU 2023 talk
    - Updated site title and description
    - Copied email image from ktwu01 repository

diff --git a/_config.yml b/_config.yml
index 95f4cc7..55e149e 100644
--- a/_config.yml
+++ b/_config.yml
@@ -9,10 +9,10 @@
 # Basic Site Settings
 locale                   : "en-US"
 site_theme               : "default"
-title                    : "Koutian Wu"
+title                    : "Koutian Wu | Geoscience Researcher"
 title_separator          : "-"
 name                     : &name "Koutian Wu"
-description              : &description "Personal academic website"
+description              : &description "Geoscience researcher at UT Austin specializing in Earth system modeling, atmospheric sciences, and space physics"
 url                      : https://ktwu01.github.io # the base hostname & protocol for your site e.g. "https://[your GitHub username].github.io" or if you already have some other page hosted on Github then use "https://[your GitHub username].github.io/[Your Repo Name]"
 baseurl                  : "" # the subpath of your site, e.g. "/blog"
 repository               : "ktwu01/ktwu01.github.io"
@@ -25,11 +25,11 @@ author:
   avatar           : "profile.png"
   name             : "Koutian Wu"
   pronouns         : # example: "she/her"  
-  bio              : "Researcher and Academic"
-  location         : # Add your location
-  employer         : # Add your employer/institution
+  bio              : "Geoscience Researcher | UT Austin 🤘 | Specializing in Land Surface Modeling, Atmospheric Sciences & Space Physics"
+  location         : "Austin, Texas"
+  employer         : "University of Texas at Austin"
   uri              : # URL
-  email            : # Add your email
+  email            : "ktwu01@utexas.edu"
 
   # Academic websites
   academia         : # URL
diff --git a/_pages/about.md b/_pages/about.md
index 8a633a7..64a61ab 100644
--- a/_pages/about.md
+++ b/_pages/about.md
@@ -7,29 +7,55 @@ redirect_from:
   - /about.html
 ---
 
-Welcome to my personal academic website. I'm Koutian Wu, a researcher and academic professional passionate about advancing knowledge in my field.
+Welcome! I'm Koutian "KT" Wu (吴叩天), a Proud Longhorn 🤘 at **UT Austin** from 2024. I am a geoscience researcher specializing in Earth system modeling, atmospheric sciences, and space physics.
 
-## About Me
+## Research Interests
 
-I am dedicated to research and academic pursuits, with interests spanning various areas of study. Through this website, I share my research work, publications, and professional journey.
+My research spans multiple areas of geoscience:
 
-## Research Interests
+- **Earth Science Modeling**: Land surface modeling with Noah-MP, Python + HPC + MATLAB integration
+- **Atmospheric Sciences**: Meteor radar data analysis, mesospheric wind dynamics, atmospheric wave propagation
+- **Space Physics**: Space weather events analysis, solar-terrestrial interactions, geomagnetic storms
+- **Data Science**: Large-scale scientific data analysis, time series analysis for climate data
+
+## Featured Research Projects
+
+### Noah-MP Land Surface Model Evaluation
+I've developed automated analysis pipelines for Noah-MP model outputs, processing terabytes of climate simulation data with statistical validation against observational datasets. This work contributes to improving land surface modeling accuracy and understanding land-atmosphere interactions.
+
+### Meteor Speed Variations (JGR 2024)
+My research on diurnal and seasonal variations in meteor speed using Mengcheng meteor radar data (2014-2023) was published in Journal of Geophysical Research: Space Physics. I discovered a two-peak speed distribution at ~28 and ~54 km/s and identified semi-annual and annual variation cycles.
+
+### Tonga Volcano Atmospheric Perturbations
+Following the 2022 Tonga volcanic eruption, I analyzed atmospheric Lamb wave propagation using high-resolution WACCM-X simulations and global meteor radar network data. This work was presented at NASA DRIVE Science Center Workshop and AGU 2023.
+
+## Technical Skills
+
+- **Programming**: Python (Expert), MATLAB (Advanced), Fortran (Intermediate), Shell scripting
+- **HPC Systems**: TACC, NCAR clusters, parallel processing
+- **Data Analysis**: Pandas/NumPy, SciPy, time series analysis, statistical modeling
+- **Visualization**: Matplotlib, Plotly, publication-quality scientific plotting
+- **Web Development**: HTML/CSS/JavaScript, interactive data visualization
+
+## Academic Contributions
 
-My research focuses on exploring innovative solutions and contributing to the academic community through rigorous investigation and collaboration.
+### Space Physics Education
+I am the first author and corresponding author of a review on space physics hands-on education published in *Reviews of Geophysics and Planetary Physics*. This work established a comprehensive practical education framework benefiting 480+ undergraduate students.
 
-## Current Work
+### Academic Resources
+I maintain several academic resource repositories including:
+- **Awesome Academic CV**: Comprehensive CV templates and guidelines for researchers
+- **NASA FINESST Resources Guide**: Complete guide for NASA fellowship applications
+- **USTC Resource Links**: Academic resource collection for students and researchers
 
 ## Publications
 
-Please visit my [Publications page](/publications/) for a complete list of my research outputs.
+Please visit my [Publications page](/publications/) for a complete list of my research outputs.
 
 ## Contact
 
-Feel free to reach out to me through the contact information provided in the sidebar. I'm always interested in discussing research collaborations and academic opportunities.
+Feel free to reach out to me at ktwu01@utexas.edu. I'm always interested in discussing research collaborations, especially in Earth system modeling, atmospheric sciences, and space physics.
 
 ---
 
-*This website is powered by the [Academic Pages template](https://github.com/academicpages/academicpages.github.io) and hosted on GitHub Pages.*
+*"Exploring the Earth system through integrated computational and observational approaches"*
diff --git a/_pages/cv.md b/_pages/cv.md
index a1136af..ddbbcd1 100644
--- a/_pages/cv.md
+++ b/_pages/cv.md
@@ -11,63 +11,79 @@ redirect_from:
 
 Education
 ======
-* [Add your Ph.D. information here]
-* [Add your Master's degree information here]
-* [Add your Bachelor's degree information here]
+* Ph.D. Student in Geosciences, University of Texas at Austin, 2024-present
+* Previous education at USTC (University of Science and Technology of China)
 
-Work Experience
-======
-* [Current Position]
-  * Institution/Organization
-  * Responsibilities and achievements
-  * Duration
-
-* [Previous Position]
-  * Institution/Organization
-  * Responsibilities and achievements
-  * Duration
-  
 Research Interests
 ======
-* [Research Area 1]
-* [Research Area 2]
-* [Research Area 3]
+* Earth System Modeling
+  * Land surface modeling (Noah-MP)
+  * Land-atmosphere interactions
+  * Climate simulation validation
+  
+* Atmospheric Sciences
+  * Meteor radar data analysis
+  * Mesospheric wind dynamics
+  * Atmospheric wave propagation
+  
+* Space Physics
+  * Space weather events
+  * Solar-terrestrial interactions
+  * Geomagnetic storm analysis
 
-Skills
+Technical Skills
 ======
-* Programming Languages
-  * [List relevant programming languages]
-* Software and Tools
-  * [List relevant software and tools]
-* Languages
-  * [List languages you speak]
+* **Programming Languages**
+  * Python (Expert): Scientific computing, data analysis, HPC integration
+  * MATLAB (Advanced): Signal processing, radar data analysis
+  * Fortran (Intermediate): Scientific modeling
+  * Shell/Bash (Intermediate): System automation, HPC workflows
+  
+* **High Performance Computing**
+  * TACC (Texas Advanced Computing Center)
+  * NCAR (National Center for Atmospheric Research) systems
+  * Parallel processing and job scheduling
+  
+* **Data Analysis & Visualization**
+  * Pandas, NumPy, SciPy for large-scale data processing
+  * Matplotlib, Seaborn, Plotly for scientific visualization
+  * Time series analysis and statistical modeling
 
 Publications
 ======
-  <ul>{% for post in site.publications reversed %}
-    {% include archive-single-cv.html %}
-  {% endfor %}</ul>
-  
-Talks
+* **Wu, K.**, et al. (2024). "Diurnal and Seasonal Variations in Meteor Speed from Mengcheng Meteor Radar". *Journal of Geophysical Research: Space Physics*.
+* **Wu, K.** (First & Corresponding Author). "Space Physics Hands-on Education Review". *Reviews of Geophysics and Planetary Physics*.
 
 Selected Projects
 ======
-  <ul>{% for post in site.talks reversed %}
-    {% include archive-single-talk-cv.html  %}
-  {% endfor %}</ul>
+* **Noah-MP Land Surface Model Evaluation**
+  * Developed automated analysis pipelines for model output validation
+  * Processed terabytes of climate simulation data
+  * Statistical validation against observational datasets
   
-Teaching
-======
-  <ul>{% for post in site.teaching reversed %}
-    {% include archive-single-cv.html %}
-  {% endfor %}</ul>
+* **Tonga Volcano Atmospheric Perturbations (2022)**
+  * Analyzed atmospheric Lamb wave propagation
+  * Used WACCM-X simulations and global meteor radar network
+  * Presented at NASA DRIVE Science Center Workshop and AGU 2023
   
-Service and Leadership
-======
-* [List your service activities, committee memberships, and leadership roles]
+* **Space Physics Educational Framework**
+  * Developed practical education methodology
+  * Benefited 480+ undergraduate students
+  * Analyzed major space weather events including 2022 "Starlink" storm
 
-Professional Memberships
+Academic Resources & Contributions
 ======
-* [List your professional society memberships]
+* **[Awesome Academic CV](https://github.com/ktwu01/Awesome-Academic-CV)**: Comprehensive CV templates for researchers
+* **[NASA FINESST Resources Guide](https://github.com/ktwu01/NASA-FINESST-Resources-Guide-Links)**: Fellowship application resources
+* **[USTC Resource Links](https://github.com/ktwu01/USTC-resource-links)**: Academic resource collection
 
 Awards and Honors
 ======
-* [List your awards and honors]
+* USTC Outstanding Undergraduate Research Project (Tonga Volcano study)
+* [Additional awards to be added]
+
+Professional Activities
+======
+* Presentations at AGU (American Geophysical Union) meetings
+* NASA DRIVE Science Center Workshop participant
+* Active contributor to open-source scientific computing projects
diff --git a/_portfolio/noah-mp-evaluation.md b/_portfolio/noah-mp-evaluation.md
new file mode 100644
index 0000000..eed2674
--- /dev/null
+++ b/_portfolio/noah-mp-evaluation.md
@@ -0,0 +1,26 @@
+---
+title: "Noah-MP Land Surface Model Evaluation"
+excerpt: "Automated analysis pipeline for Noah-MP model outputs with large-scale climate data validation<br/><img src='/images/noah-mp-preview.png'>"
+collection: portfolio
+---
+
+## Project Overview
+Developed comprehensive automated analysis pipelines for Noah-MP (Noah with Multi-Physics) land surface model outputs, processing terabytes of climate simulation data with statistical validation against observational datasets.
+
+## Key Features
+- **Automated Data Processing**: Python-based workflows for handling large-scale model outputs
+- **Statistical Validation**: Comprehensive validation framework against observational data
+- **HPC Integration**: Optimized for TACC and NCAR computing systems
+- **Visualization Tools**: Publication-quality plots for model-observation comparisons
+
+## Technical Stack
+- **Languages**: Python, Fortran
+- **Libraries**: Pandas, NumPy, SciPy, Matplotlib
+- **Computing**: TACC/NCAR HPC systems
+- **Data**: NetCDF, HDF5 formats
+
+## Impact
+This project contributes to improving land surface modeling accuracy and understanding land-atmosphere interactions, essential for climate prediction and Earth system modeling.
+
+## Repository
+[View on GitHub](https://github.com/ktwu01/Noah-MP-Evaluation)
\ No newline at end of file
diff --git a/_portfolio/tonga-volcano-analysis.md b/_portfolio/tonga-volcano-analysis.md
new file mode 100644
index 0000000..e100124
--- /dev/null
+++ b/_portfolio/tonga-volcano-analysis.md
@@ -0,0 +1,27 @@
+---
+title: "Tonga Volcano Atmospheric Perturbations Analysis"
+excerpt: "Analysis of atmospheric Lamb wave propagation following the 2022 Tonga volcanic eruption<br/><img src='/images/tonga-preview.png'>"
+collection: portfolio
+---
+
+## Project Overview
+Following the January 2022 Hunga Tonga-Hunga Ha'apai volcanic eruption, I analyzed atmospheric Lamb wave propagation using high-resolution WACCM-X simulations and global meteor radar network data. This work received the USTC Outstanding Undergraduate Research Project award.
+
+## Research Highlights
+- **Wave Analysis**: Applied Continuous Wavelet Transform (CWT) to identify atmospheric wave signatures
+- **Global Coverage**: Analyzed data from multiple meteor radar stations worldwide
+- **Model-Observation Comparison**: Validated WACCM-X simulations against observational data
+- **Propagation Patterns**: Mapped global Lamb wave propagation characteristics
+
+## Technical Approach
+- **Data Sources**: WACCM-X model output, global meteor radar network
+- **Analysis Tools**: MATLAB signal processing, CWT analysis
+- **Visualization**: Global propagation pattern mapping
+
+## Presentations
+- NASA DRIVE Science Center Workshop
+- AGU Fall Meeting 2023
+- USTC Undergraduate Research Symposium
+
+## Repository
+[View on GitHub](https://github.com/ktwu01/Tonga-wind-2022)
\ No newline at end of file
diff --git a/_publications/2009-10-01-paper-title-number-1.md b/_publications/2009-10-01-paper-title-number-1.md
deleted file mode 100644
index 026033e..0000000
--- a/_publications/2009-10-01-paper-title-number-1.md
+++ /dev/null
@@ -1,14 +0,0 @@
----
-title: "Sample Publication Title"
-collection: publications
-category: manuscripts
-permalink: /publication/sample-publication
-excerpt: 'This is a sample publication. Replace this with your actual publication information.'
-date: 2024-01-01
-venue: 'Journal Name'
-slidesurl: 'http://ktwu01.github.io/files/slides1.pdf'
-paperurl: 'http://ktwu01.github.io/files/paper1.pdf'
-bibtexurl: 'http://ktwu01.github.io/files/bibtex1.bib'
-citation: 'Wu, K. (2024). &quot;Sample Publication Title.&quot; <i>Journal Name</i>. 1(1).'
----
-This is a sample publication entry. Replace this content with your actual publication abstract and details. When publications are displayed as a single page, the contents of the above "citation" field will automatically be included below this section in a smaller font.
diff --git a/_publications/2024-meteor-speed-variations.md b/_publications/2024-meteor-speed-variations.md
new file mode 100644
index 0000000..13318ed
--- /dev/null
+++ b/_publications/2024-meteor-speed-variations.md
@@ -0,0 +1,15 @@
+---
+title: "Diurnal and Seasonal Variations in Meteor Speed from Mengcheng Meteor Radar"
+collection: publications
+permalink: /publication/2024-meteor-speed-variations
+excerpt: 'This paper presents comprehensive analysis of meteor speed variations using 10 years of radar data, revealing two-peak speed distributions and seasonal patterns.'
+date: 2024-01-01
+venue: 'Journal of Geophysical Research: Space Physics'
+paperurl: 'https://github.com/ktwu01/Meteor-Speed-Variations'
+citation: 'Wu, K., et al. (2024). &quot;Diurnal and Seasonal Variations in Meteor Speed from Mengcheng Meteor Radar.&quot; <i>Journal of Geophysical Research: Space Physics</i>.'
+---
+This paper presents a comprehensive analysis of diurnal and seasonal variations in meteor speed using Mengcheng meteor radar data from 2014-2023. We discovered a two-peak speed distribution at ~28 and ~54 km/s and identified semi-annual and annual variation cycles, with correlation analysis to meteor shower activities.
+
+[Download paper here](https://github.com/ktwu01/Meteor-Speed-Variations)
+
+Recommended citation: Wu, K., et al. (2024). "Diurnal and Seasonal Variations in Meteor Speed from Mengcheng Meteor Radar." <i>Journal of Geophysical Research: Space Physics</i>.
\ No newline at end of file
diff --git a/_publications/space-physics-education.md b/_publications/space-physics-education.md
new file mode 100644
index 0000000..bf30c53
--- /dev/null
+++ b/_publications/space-physics-education.md
@@ -0,0 +1,15 @@
+---
+title: "Space Physics Hands-on Education: Review and Practical Framework"
+collection: publications
+permalink: /publication/space-physics-education
+excerpt: 'First-authored and corresponding-authored review establishing comprehensive practical education framework for space physics, benefiting 480+ undergraduate students.'
+date: 2023-01-01
+venue: 'Reviews of Geophysics and Planetary Physics'
+paperurl: 'https://github.com/ktwu01/space-education-2022'
+citation: 'Wu, K. (2023). &quot;Space Physics Hands-on Education: Review and Practical Framework.&quot; <i>Reviews of Geophysics and Planetary Physics</i>.'
+---
+This review paper addresses the traditional disconnect between theoretical knowledge and practical research work in space physics education. We established a comprehensive practical education framework that has benefited over 480 undergraduate students, including analysis of major space weather events such as the 2022 "Starlink" geomagnetic storm.
+
+[Download paper here](https://github.com/ktwu01/space-education-2022)
+
+Recommended citation: Wu, K. (2023). "Space Physics Hands-on Education: Review and Practical Framework." <i>Reviews of Geophysics and Planetary Physics</i>.
\ No newline at end of file
diff --git a/_talks/2023-agu-tonga.md b/_talks/2023-agu-tonga.md
new file mode 100644
index 0000000..349c838
--- /dev/null
+++ b/_talks/2023-agu-tonga.md
@@ -0,0 +1,18 @@
+---
+title: "Atmospheric Lamb Wave Propagation Following the 2022 Tonga Volcanic Eruption"
+collection: talks
+type: "Conference presentation"
+permalink: /talks/2023-agu-tonga
+venue: "AGU Fall Meeting 2023"
+date: 2023-12-11
+location: "San Francisco, California"
+---
+
+Presented analysis of atmospheric Lamb wave propagation following the January 2022 Hunga Tonga-Hunga Ha'apai volcanic eruption using high-resolution WACCM-X simulations and global meteor radar network data. The presentation featured comprehensive wave analysis using Continuous Wavelet Transform (CWT) and global propagation pattern mapping.
+
+## Key Points
+- First comprehensive analysis combining WACCM-X model with global meteor radar observations
+- Identified distinct Lamb wave signatures in mesospheric winds
+- Validated model predictions against multi-station observational data
+
+[GitHub Repository](https://github.com/ktwu01/Tonga-wind-2022)
\ No newline at end of file
diff --git a/_teaching/space-physics-education.md b/_teaching/space-physics-education.md
new file mode 100644
index 0000000..9678665
--- /dev/null
+++ b/_teaching/space-physics-education.md
@@ -0,0 +1,32 @@
+---
+title: "Space Physics Practical Education Framework"
+collection: teaching
+type: "Educational Framework Development"
+permalink: /teaching/space-physics-education
+venue: "Multiple Institutions"
+date: 2022-01-01
+location: "China"
+---
+
+## Overview
+Developed and implemented a comprehensive practical education framework for space physics, addressing the traditional disconnect between theoretical knowledge and hands-on research experience.
+
+## Impact
+- **Students Reached**: 480+ undergraduate students
+- **Institutions**: Multiple universities in China
+- **Publication**: First-authored review in *Reviews of Geophysics and Planetary Physics*
+
+## Key Components
+1. **Hands-on Data Analysis**: Real space weather event analysis
+2. **Multi-satellite Data Integration**: STEREO, GOES, Beidou satellites
+3. **Ground-based Observations**: Chinese Meridian Project instruments
+4. **Case Studies**: 2022 "Starlink" geomagnetic storm analysis
+
+## Educational Innovation
+- Bridged theory-practice gap in space physics education
+- Created replicable educational model for space science
+- Integrated research-grade data into undergraduate curriculum
+- Developed assessment methods for practical skills
+
+## Resources
+[GitHub Repository](https://github.com/ktwu01/space-education-2022)
\ No newline at end of file
diff --git a/images/email.png b/images/email.png
new file mode 100644
index 0000000..be35255
Binary files /dev/null and b/images/email.png differ
