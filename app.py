import streamlit as st
import time
import pandas as pd
import numpy as np
from PIL import Image
import base64

# Custom function for animated text
def animated_text(text, speed=0.03):
    container = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        container.markdown(displayed_text)
        time.sleep(speed)
    return container

# Function to add background image
def add_bg_from_url():
    with open("train_image.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
    f"""
    <style>
    /* Create a pseudo-element for the background with reduced opacity */
    .stApp:before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url(data:image/png;base64,{encoded_string});
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
        opacity: 0.2;
        z-index: -1;
    }}
    
    /* Remove the background from the main app element */
    .stApp {{
        background: none;
    }}
    
    .main-content {{
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 1rem;
        margin: 1rem 0;
        color: white;
        position: relative; 
    }}
    
    h1, h2, h3 {{
        color: #1E3A8A;
    }}
    
    .stSidebar {{
        background-color: rgba(0, 0, 0, 0.7);
        position: relative; 
    }}
    
    .stSidebar .stRadio label {{
        color: white;
    }}
    
    .stSidebar h1 {{
        color: white;
    }}
    
    .highlight {{
        background-color: #FFC107;
        padding: 0.2rem;
        border-radius: 0.3rem;
    }}
    
    p, span, label, div {{
        color: white;
    }}
    
    .stat-box {{
        background-color: #4169E1;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 0.5rem 0;
        color: white;
        text-align: center;
    }}
    
    .stat-number {{
        font-size: 2rem;
        font-weight: bold;
    }}
    
    .stat-label {{
        font-size: 0.9rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Set page title and layout
st.set_page_config(
    page_title="Indian Railways Analysis",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply background and styling
add_bg_from_url()

# Sidebar Navigation with animation
with st.sidebar:
    st.title("🚆 Navigation")
    
    sections = [
        "Introduction",
        "Source of Data and Structure",
        "Train Delay Analysis Overview",
        "Delay across different zones and divisions",
        "Some Statistical Analysis",
        "Conclusion"
    ]
    
    section = st.radio("", sections)
    
    st.sidebar.markdown("---")
# Main content with background
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Section 1: Introduction
if section == "Introduction":
    st.title("🚆 A Deep Dive into the World of Indian Railways")
    
    # Animated introduction
    intro_text = """
    The Indian Railways is one of the largest rail networks in the world, serving millions of passengers daily.
    However, delays are a common issue that affect both passengers and freight operations. Last year Indian Railways
    lost about one crore minutes of train delay.
    """
    animated_text(intro_text, 0.01)
    
    # Add some engaging statistics in boxes
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">17</div>
            <div class="stat-label">Railway Zones</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">72</div>
            <div class="stat-label">Divisions</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">3,100+</div>
            <div class="stat-label">Trains Analyzed</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("Organization and structure of Indian Railways")
    
    # Create two columns for zones and train types
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Railway Zones")
        zones = [
            "Northern Railway", "North Eastern Railway", "East Central Railway",
            "East Coast Railway", "South Eastern Railway", "South Central Railway",
            "South Western Railway", "Western Railway", "Central Railway",
            "North Western Railway", "North East Frontier Railway", "Southern Railway",
            "Eastern Railway", "South East Central Railway", "West Central Railway",
            "North Central Railway", "Konkan Railway"
        ]
        
        for i, zone in enumerate(zones, 1):
            st.markdown(f"{i}. {zone}")
    
    with col2:
        st.markdown("### Train Categories")
        categories = [
            "Mail/Express", "Superfast", "Rajdhani", "Duronto", "Shatabdi",
            "Jan Shatabdi", "Garib Rath", "Humsafar Express", "Special/Temporary Trains"
        ]
        
        for i, category in enumerate(categories, 1):
            st.markdown(f"{i}. {category}")
    
    st.subheader("Key Questions")
    st.markdown("""
    This study explores two key questions:
    1. **Which zone and which division requires the most attention?**
    2. **Which trains are more susceptible to delay?**
    """)

elif section == "Source of Data and Structure":
    st.title("📊 Source of Data and Structure")
    
    # Add some animation for data sources
    st.markdown("### Data Sources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #E8F5E9; padding: 1rem; border-radius: 0.5rem; height: 100%;">
            <h4 style="color: #2E7D32;">m.etrain.info</h4>
            <p>Used for train running history data</p>
            <div style="text-align: center; margin-top: 1rem;">
                <i class="material-icons" style="font-size: 3rem; color: #2E7D32;">query_stats</i>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #E3F2FD; padding: 1rem; border-radius: 0.5rem; height: 100%;">
            <h4 style="color: #1565C0;">erain.in</h4>
            <p>Used for train meta data like originZone, destinationZone, etc.</p>
            <div style="text-align: center; margin-top: 1rem;">
                <i class="material-icons" style="font-size: 3rem; color: #1565C0;">hub</i>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### Data Collection Process")
    st.info("""
    The data of all trains mentioned in the categories were tried to be included
    but due to the dynamic nature of the website and structure mismatch for some trains, the scraping could not be
    done for all trains. More precisely the data of around 3200 trains were scraped out of approximately 3600 trains.
    """)
    
    st.subheader("Data Structure")
    
    # Create an expandable section for data structure
    with st.expander("See detailed data structure"):
        st.markdown("""
        Each train's data follows this format:
        
        1. Origin station Code
        2. Destination station Code
        3. Number of stoppages
        4. Distance covered
        5. Train Type
        6. Origin Station Zone
        7. Destination Station Zone
        8. A 1 x 72 sized vector representing divisions and station counts
        9. Average delay across all stations over past 3 months
        """)
        
        # Show a mock dataframe as example
        mock_data = {
            'Origin': ['NDLS', 'HWH', 'CSTM'],
            'Destination': ['HWH', 'MAS', 'JAT'],
            'Stoppages': [12, 22, 8],
            'Distance(km)': [1450, 1660, 1420],
            'Type': ['Rajdhani', 'Mail/Express', 'Duronto'],
            'OriginZone': ['NR', 'ER', 'CR'],
            'DestZone': ['ER', 'SR', 'NR'],
            'AvgDelay(min)': [28, 62, 45]
        }
        
        df = pd.DataFrame(mock_data)
        st.dataframe(df, use_container_width=True)

elif section == "Train Delay Analysis Overview":
    st.title("🚉 Train Delay Analysis Overview")
    
    # Introduction with animation
    overview_text = """
    In this section and the next, we present a detailed analysis of train delays with respect to zones and train types.
    """
    animated_text(overview_text, 0.01)
    
    # Key metrics in boxes
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="stat-box" style="background-color: #D32F2F;">
            <div class="stat-number">47.21</div>
            <div class="stat-label">Average Delay (minutes)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box" style="background-color: #1976D2;">
            <div class="stat-number">26.53</div>
            <div class="stat-label">Median Delay (minutes)</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Image with improved styling
    st.subheader("Distribution Of Train Delays")
    st.image("delay_chart.png")
    
    # Key observations with better formatting
    st.subheader("Key Observations")
    
    observations = [
        {
            "percentage": "55%",
            "description": "of trains are delayed by less than 30 minutes. These mainly include all premium trains like Rajdhani, Duronto and short distance trains with distance covered no more than 500 km.",
            "color": "#4CAF50"
        },
        {
            "percentage": "23%",
            "description": "of trains are delayed by less than 60 minutes. These mainly include all superfast trains and express trains who happen to enjoy the luxury of travelling through low traffic zones.",
            "color": "#2196F3"
        },
        {
            "percentage": "8%",
            "description": "of trains are delayed in range 60-120 minutes.",
            "color": "#FFC107"
        },
        {
            "percentage": "14%",
            "description": "of trains are delayed by more than 120 minutes. This is particularly concerning as this means that a train is more likely to be delayed by more than 2 hours than be late by 1-2 hours. These happen to be long distant trains travelling through high traffic zones or trains who get low priority.",
            "color": "#F44336"
        }
    ]
    
    for obs in observations:
        st.markdown(f"""
        <div style="background-color: {obs['color']}22; border-left: 5px solid {obs['color']}; padding: 1rem; margin: 0.5rem 0; border-radius: 0.3rem;">
            <span style="font-size: 1.5rem; font-weight: bold; color: {obs['color']};">{obs['percentage']}</span> {obs['description']}
        </div>
        """, unsafe_allow_html=True)
    
    # Delay by train type analysis
    st.subheader("Delay by Train Type Analysis")
    st.image("type_delay_chart.png")
    
    # Create toggleable sections for each train type analysis
    train_types = {
        "Special Trains": "The most delayed trains are the Special trains that run on an average of 100 minutes. This is because they are temporary trains and always get lower priority than regular trains.",
        "Humsafar Express": "The second most delayed trains are the Humsafar trains with an average delay of 94 minutes. This is very counter intuitive because they are a type of premium trains. The only reason that can be thought of is that most of humsafar trains run for long distances > 2000 km and hence are more prone to delays.",
        "Shatabdi & Jan Shatabdi": "Shatabdis and Jan Shatabdis are the least delayed trains with an average delay of just 18 and 22 minutes. This is because not only do they have higher priority but also they are short distance trains and hence less probable to get delayed.",
        "Mail/Express Trains": "Among long distance trains the least delayed trains are the Mail/Express trains with an average delay of 37.5 minutes. This is even less than Rajdhani trains even though they are of lower priority. This is because they have a low average speed and thus enjoy some slack in the schedule so whenever gets a little track clearance they can make up for the delay.",
        "Duronto, Rajdhani & Garib Rath": "Duronto, Rajdhani and Garib Rath trains get late due to their high average speed and tight schedule and also the fact that they travel on some of the most congested routes."
    }
    
    for train_type, analysis in train_types.items():
        with st.expander(f"Analysis: {train_type}"):
            st.write(analysis)

elif section == "Delay across different zones and divisions":
    st.title("🗺️ Delay across different zones and divisions")
    
    # Zones vs Delay
    st.subheader("Zones vs Delay")
    st.image("zone_delay_chart.png")
    
    # Create tabs for different analyses
    tab1, tab2, tab3 = st.tabs(["Zone Analysis", "Distance vs Delay", "Correlation Analysis"])
    
    with tab1:
        # Zone analysis with better formatting
        zones_analysis = [
            {
                "zone": "North Central Railways",
                "avg_delay": "75 minutes",
                "median_delay": "54.1 minutes",
                "reason": "This is likely because of the high traffic on the route between Delhi and DDU (erstwhile Mughalsarai)",
                "color": "#C62828"
            },
            {
                "zone": "East Central Railways",
                "avg_delay": "69.5 minutes",
                "median_delay": "51.8 minutes",
                "reason": "This is because of fewer tracks in Bihar's Hajipur-Sonpur-Barauni-Muzzaffarpur-Katihar section and an infamous act by local people namely chain pulling. Chain Pulling annually causes more delay in Bihar than any other state.",
                "color": "#AD1457"
            },
            {
                "zone": "Southern Railways",
                "avg_delay": "31 minutes",
                "median_delay": "17.1 minutes",
                "reason": "Most punctual. This is basically because most of the trains operating in the region have a weekly/bi-weekly frequency so the tracks are not congested much.",
                "color": "#1565C0"
            }
        ]
        
        for analysis in zones_analysis:
            st.markdown(f"""
            <div style="background-color: {analysis['color']}22; border-left: 5px solid {analysis['color']}; padding: 1rem; margin: 1rem 0; border-radius: 0.3rem;">
                <h4 style="color: {analysis['color']};">{analysis['zone']}</h4>
                <p><strong>Average Delay:</strong> {analysis['avg_delay']}</p>
                {f"<p><strong>Median Delay:</strong> {analysis['median_delay']}</p>" if 'median_delay' in analysis else ""}
                {f"<p><strong>Reason:</strong> {analysis['reason']}</p>"}
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        # Delay vs Distance
        st.image("distance_delay_chart.png")
        
        st.info("""
        As we see, the delay increases with the distance covered by the train. This is because the longer the train travels, the more
        probable it is to get delayed due to various factors like track congestion, weather conditions, and operational constraints.
        """)
        
        st.warning("""
        An anomaly: Beyond 2000 km the delay decreases. This is likely because
        long distance trains get slack zones in their schedule. Like the train may be allotted 100 minutes to cover 50 km but
        the train may cover that in around 40 minutes (avg speed = 75km/h not tough) thus making up time.
        """)
    
    with tab3:
        # Correlation analysis
        st.markdown("### Correlation Between Delay and Other Factors")
        col1, col2 = st.columns(2)

        with col1:
            st.image("delay_correlation_part1.png")

        with col2:
            st.image("delay_correlation_part2.png")

        st.markdown("""
        <div style="background-color: #FFFDE7; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;">
        <h4 style="color: #F57F17;">Key Correlation Findings</h4>
        <ul style="color: #333;">
            <li>Positive correlation between delay and distance</li>
            <li>Positive correlation between delay and number of stops</li>
            <li>Highest correlation for PRYJ (Prayagraj) division</li>
            <li>Top 3 correlations: Prayagraj, Jhansi, and Lucknow (all in NCR)</li>
            <li>CKP (Charadharpur) division is 4th most affected</li>
            <li>Some divisions like BRC (Vadodara), ADI (Ahmedabad), and SRT (Surat) have negative correlation with delay</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif section == "Some Statistical Analysis":
    st.title("🔍 Statistical Deep Dive")
    
    # Distribution Analysis
    st.subheader("📊 Delay Distribution")
    
    # First visualization
    st.image("delay_distribution.png")
    st.markdown("""
    #### Raw Probability Density Function
    Let's explore how flight delays distribute across time! This visualization shows the raw probability density function (PDF) 
    where delay is our random variable. Each point on the curve represents the likelihood of a specific delay duration occurring.
    
    *Technical note: Using a 3-minute interval and a 2-pointer algorithm on sorted delays for probability calculations.*
    """)
    
    # Second visualization
    st.image("smoothened_distribution.png")
    st.markdown("""
    #### Smoothened Distribution
    To get a clearer picture, we've applied some mathematical magic! Using a Savitzky-Golay filter 
    (window size: 11, polynomial order: 3), we've smoothened out the rough edges while preserving the 
    distribution's key features. The result? A beautiful, continuous, and differentiable function!
    """)
    
    # Third visualization
    st.image("regression.png")
    st.markdown("""
    #### Polynomial Regression Analysis
    Here's where it gets interesting! We've fitted a 5th-degree polynomial to our PDF, and the results are impressive.
    
    For the math enthusiasts, the cumulative distribution function can be approximated by:
    
    ```math
    f(x) = -2.228e-13x^5 + 2.094e-10x^4 - 7.51e-08x^3 + 1.28e-05x^2 - 0.001043x
    ```
    *(Valid for x > 12)*
                
    ```math
    R² Score: 0.9673
    ```
    *(for x>12)*
    
    This mathematical model helps us predict and understand delay patterns with remarkable accuracy! 
    """)


elif section == "Conclusion":
    st.title("📌 Conclusion")
    
    # Animated conclusion text
    conclusion_text = """
    Our analysis highlights critical areas in the Indian Railways system that need improvement.
    """
    animated_text(conclusion_text, 0.01)
    
    # Create two columns for key findings
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #E8EAF6; padding: 1rem; border-radius: 0.5rem;color:black;">
            <h3 style="color: #3F51B5;">Answers to Our Key Questions</h3>
            <ul>
                <li>North Central Railways and East Central Railways are the most affected zones</li>
                <li>Long-distance trains are more prone to delays</li>
                <li>Trains with more stops tend to have higher delays</li>
                <li>Prayagraj, Jhansi, and Lucknow are the most affected divisions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #FFF3E0; padding: 1rem; border-radius: 0.5rem;color:black;">
            <h3 style="color: #E65100;">Key Takeaways</h3>
            <ul>
                <li>Certain zones and divisions experience significantly higher delays</li>
                <li>Specific train types, especially long-distance trains, are more prone to delays</li>
                <li>Understanding these trends can help policymakers and railway authorities optimize operations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Future work
    st.markdown("""
    <div style="background-color: #E0F7FA; padding: 1rem; border-radius: 0.5rem; margin-top: 1rem; color:black;">
        <h3 style="color: #006064;">Future Work</h3>
        <p style="color:black">Future work can include predictive modeling to anticipate delays and suggest mitigation strategies.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Thank you message with animation
    st.balloons()
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <h2 style="color: #1E3A8A;">Thank you for exploring this analysis!</h2>
    </div>
    """, unsafe_allow_html=True)

# Close the main content div
st.markdown('</div>', unsafe_allow_html=True)
