import numpy as np
import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import networkx as nx
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="HeatShield - Heatwave Warning System",
    page_icon="🔥",
    layout="wide"
)

# Custom CSS for Hero Banner, Animated Heat Waves Background, and Modern UI Components
st.markdown("""
    <style>
    /* Animated Heat Wave Background */
    .stApp {
        background: linear-gradient(135deg, #0d0e15 0%, #171010 40%, #201008 100%);
        background-attachment: fixed;
    }
    
    .stAppViewContainer::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 50% 30%, rgba(255, 69, 0, 0.12), transparent 60%),
                    radial-gradient(circle at 80% 70%, rgba(255, 140, 0, 0.08), transparent 50%);
        pointer-events: none;
        z-index: 0;
    }

    /* Hero Header Banner */
    .hero-banner {
        background: linear-gradient(135deg, rgba(255, 69, 0, 0.15) 0%, rgba(255, 140, 0, 0.05) 100%);
        border: 1px solid rgba(255, 69, 0, 0.3);
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(255, 69, 0, 0.15);
        backdrop-filter: blur(8px);
        margin-bottom: 30px;
        position: relative;
        overflow: hidden;
    }

    /* Live Animated Pulsing Badge */
    .live-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 69, 0, 0.2);
        border: 1px solid #FF4500;
        color: #FF7F50;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 12px;
        letter-spacing: 0.5px;
    }

    .pulse-dot {
        width: 8px;
        height: 8px;
        background-color: #FF4500;
        border-radius: 50%;
        box-shadow: 0 0 0 rgba(255, 69, 0, 0.7);
        animation: pulse 1.6s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 69, 0, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(255, 69, 0, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 69, 0, 0); }
    }

    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF4500, #FFA500, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        color: #C0C0C0;
        font-size: 1.1rem;
        margin-top: 8px;
        font-weight: 400;
    }

    /* Color Map Legend Card Styling */
    .legend-box {
        display: flex;
        justify-content: space-around;
        background: rgba(22, 27, 34, 0.8);
        padding: 14px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 18px;
        backdrop-filter: blur(5px);
    }

    .legend-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.95rem;
        font-weight: 500;
        color: #E0E0E0;
    }

    .dot {
        height: 12px;
        width: 12px;
        border-radius: 50%;
        display: inline-block;
    }

    /* Footer Styling */
    .footer {
        width: 100%;
        background-color: rgba(13, 14, 21, 0.9);
        color: #FAFAFA;
        text-align: center;
        padding: 20px 0;
        margin-top: 50px;
        border-top: 1px solid rgba(255, 69, 0, 0.2);
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for Teacher Evaluation Guide
st.sidebar.header("📌 Teacher's Evaluation Guide")
st.sidebar.markdown("""
**Syllabus Topics Implemented:**
* **Module 1.1:** Propositions & Truth Logic (Rule-Based Alert Engine)
* **Module 3.1 & 3.3:** Digraphs & Matrix Composition (Wind Flow & Heat Propagation)
* **Module 4.1 & Sets:** Partitioning Temperature Sets into Regional Risk Ordering (Poset Banding)
""")

# ===================================================================
# HERO HEADER BANNER
# ===================================================================
st.markdown("""
<div class="hero-banner">
    <div class="live-badge">
        <span class="pulse-dot"></span> LIVE THERMAL MONITORING
    </div>
    <h1 class="hero-title">🔥 HeatShield OS</h1>
    <p class="hero-subtitle">Maharashtra Regional Heatwave Early Warning & Spatial Propagation System</p>
</div>
""", unsafe_allow_html=True)

# ===================================================================
# 1. LIVE RISK LEVEL CLASSIFIER (LOGIC ENGINE)
# ===================================================================
st.header("1. Environmental Threat Classifier")
st.caption("Adjust atmospheric parameters to simulate the propositional risk engine.")

col1, col2 = st.columns([1, 1])

with col1:
    temp = st.slider("Temperature (°C)", min_value=25, max_value=50, value=42)
    humidity = st.slider("Humidity (%)", min_value=10, max_value=100, value=55)
    duration = st.slider("Duration (Days)", min_value=1, max_value=7, value=3)

# Logic Evaluation Rules
p1 = temp >= 40
p2 = (temp >= 37) and (duration >= 3)
p3 = (temp >= 38) and (humidity >= 60)

is_severe = p1 or p2
is_warning = p3

with col2:
    st.subheader("Current Risk Evaluation")
    if is_severe:
        st.error("🚨 **SEVERE HEATWAVE ALERT**\n\nHigh risk conditions triggered! Emergency measures recommended.")
    elif is_warning:
        st.warning("⚠️ **HEATWAVE WARNING**\n\nModerate-to-high atmospheric risk detected.")
    else:
        st.success("✅ **NORMAL CONDITIONS**\n\nEnvironmental parameters are within safe parameters.")

st.markdown("---")

# ===================================================================
# 2. SPATIAL HEAT SPREAD TRACKER (DIGRAPH NETWORK)
# ===================================================================
st.header("2. Micro-Region Heat Spread Tracker")
st.caption("Predict thermal trajectory across neighboring Maharashtra districts using a Directed Graph (Digraph).")

zones = ["Mumbai Coast", "Pune Sector", "Nashik Belt", "Solapur Region"]

# Adjacency Matrix representing 1-step wind/thermal movement
A = np.array([
    [0, 1, 1, 0],  # Mumbai -> Pune, Nashik
    [0, 0, 0, 1],  # Pune -> Solapur
    [0, 0, 0, 1],  # Nashik -> Solapur
    [0, 0, 0, 0]   # Solapur -> None
])

A_squared = np.linalg.matrix_power(A, 2)

col_m1, col_m2 = st.columns([1, 1])

with col_m1:
    source_zone = st.selectbox("Select Sector Experiencing Initial Heat Spike:", zones)
    src_idx = zones.index(source_zone)
    
    direct_nodes = [zones[i] for i in range(4) if A[src_idx][i] == 1]
    indirect_nodes = [zones[i] for i in range(4) if A_squared[src_idx][i] > 0]

    st.subheader("Spread Prediction")
    st.markdown("**Direct Propagation (Next 1-2 Hours):**")
    if direct_nodes:
        for node in direct_nodes:
            st.write(f"• `{source_zone}` ➔ **{node}**")
    else:
        st.write("No direct downwind propagation.")

    st.markdown("**Secondary Spread (Next 3-5 Hours):**")
    if indirect_nodes:
        for node in indirect_nodes:
            st.write(f"• `{source_zone}` ➔ `[Intermediate Sector]` ➔ **{node}**")
    else:
        st.write("No secondary spread paths predicted.")

with col_m2:
    st.subheader("Thermal Network Digraph")
    
    G = nx.DiGraph()
    for i in range(4):
        for j in range(4):
            if A[i][j] == 1:
                G.add_edge(zones[i], zones[j])

    node_colors = []
    for zone in zones:
        if zone == source_zone:
            node_colors.append("#FF2B2B")
        elif zone in direct_nodes:
            node_colors.append("#FF8C00")
        elif zone in indirect_nodes:
            node_colors.append("#FFD700")
        else:
            node_colors.append("#4CAF50")

    pos = {
        "Mumbai Coast": (0, 1),
        "Pune Sector": (1, 2),
        "Nashik Belt": (1, 0),
        "Solapur Region": (2, 1)
    }

    fig, ax = plt.subplots(figsize=(6, 3.5))
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#0E1117')

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2200, ax=ax)
    nx.draw_networkx_labels(G, pos, font_color="white", font_weight="bold", font_size=8, ax=ax)
    nx.draw_networkx_edges(
        G, pos, edge_color="white", arrows=True, arrowsize=20, arrowstyle="-|>", node_size=2200, ax=ax
    )

    plt.axis("off")
    st.pyplot(fig)

st.markdown("---")

# ===================================================================
# 3. INTERACTIVE MAHARASHTRA WEATHER HEATMAP
# ===================================================================
st.header("3. Maharashtra Regional Temperature & Heat Risk Map")
st.caption("Interactive spatial monitoring across major urban and regional hubs in Maharashtra.")

# HTML Color Map Legend Card
st.markdown("""
<div class="legend-box">
    <div class="legend-item"><span class="dot" style="background-color: #2E7D32;"></span> <b>Normal:</b> &le; 36°C</div>
    <div class="legend-item"><span class="dot" style="background-color: #F57C00;"></span> <b>Moderate Risk:</b> 37°C - 39°C</div>
    <div class="legend-item"><span class="dot" style="background-color: #D32F2F;"></span> <b>Severe Heatwave:</b> 40°C - 43°C</div>
    <div class="legend-item"><span class="dot" style="background-color: #7B1FA2;"></span> <b>Extreme Heatwave:</b> &ge; 44°C</div>
</div>
""", unsafe_allow_html=True)

# City coordinates in Maharashtra with simulated temperatures (°C)
city_data = [
    {"city": "Mumbai", "lat": 19.0760, "lon": 72.8777, "temp": 34, "risk": "Normal"},
    {"city": "Pune", "lat": 18.5204, "lon": 73.8567, "temp": 38, "risk": "Moderate Risk"},
    {"city": "Nagpur", "lat": 21.1458, "lon": 79.0882, "temp": 44, "risk": "Extreme Heatwave"},
    {"city": "Nashik", "lat": 20.0059, "lon": 73.7898, "temp": 36, "risk": "Normal"},
    {"city": "Chhatrapati Sambhajinagar", "lat": 19.8762, "lon": 75.3433, "temp": 41, "risk": "Severe Heatwave"},
    {"city": "Solapur", "lat": 17.6599, "lon": 75.9064, "temp": 43, "risk": "Severe Heatwave"},
    {"city": "Kolhapur", "lat": 16.7050, "lon": 74.2433, "temp": 35, "risk": "Normal"},
    {"city": "Amravati", "lat": 20.9374, "lon": 77.7796, "temp": 43, "risk": "Severe Heatwave"},
    {"city": "Chandrapur", "lat": 19.9615, "lon": 79.2961, "temp": 45, "risk": "Extreme Heatwave"}
]

# Create OpenStreetMap centered on Maharashtra
m = folium.Map(location=[19.7515, 75.7139], zoom_start=6, tiles="OpenStreetMap")

# Prepare heat data array [lat, lon, weight]
heat_data = [[c["lat"], c["lon"], c["temp"]] for c in city_data]

# Add HeatMap overlay with refined radius
HeatMap(heat_data, radius=22, blur=15, max_zoom=1).add_to(m)

# Add Marker details for each city
for c in city_data:
    color = "purple" if c["temp"] >= 44 else ("red" if c["temp"] >= 40 else ("orange" if c["temp"] >= 37 else "green"))
    
    folium.CircleMarker(
        location=[c["lat"], c["lon"]],
        radius=7,
        popup=f"<b>{c['city']}</b><br>Temperature: {c['temp']}°C<br>Status: {c['risk']}",
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.9
    ).add_to(m)

# Render Map in Streamlit
st_folium(m, width=1200, height=500)

# ===================================================================
# FOOTER SECTION
# ===================================================================
st.markdown("""
<div class="footer">
    <p><b>HeatShield OS — Heatwave Monitoring, Prediction & Early Warning System</b></p>
    <p style="color: #888888; font-size: 0.82rem;">Academic Project | Discrete Mathematics & Network Modeling Integration</p>
</div>
""", unsafe_allow_html=True)