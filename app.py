import html
import subprocess
import sys
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="RedSentinel - SOC Operations Center",
    page_icon="🛡️",
    layout="wide"
)

# Custom SOC Dark Mode CSS
st.markdown("""
<style>
    /* Dark SOC Theme Styling */
    .stApp {
        background-color: #0b0e14;
        color: #e2e8f0;
    }
    
    /* Header & Badges */
    .soc-header {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.025em;
        color: #f8fafc;
        margin-bottom: 0.2rem;
    }
    .soc-subtitle {
        color: #94a3b8;
        font-size: 1.0rem;
        margin-bottom: 1.5rem;
    }
    
    /* Agent Cards */
    .agent-card {
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 20px;
        background-color: #131822;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
    }
    
    /* Red Agent - Offensive */
    .agent-card-red {
        border: 2px solid #ef4444;
        box-shadow: 0 0 15px rgba(239, 68, 68, 0.2);
    }
    .header-red {
        color: #fca5a5;
        font-weight: 700;
        font-size: 1.15rem;
        border-bottom: 1px solid rgba(239, 68, 68, 0.3);
        padding-bottom: 8px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Blue Agent - Defensive */
    .agent-card-blue {
        border: 2px solid #3b82f6;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.2);
    }
    .header-blue {
        color: #93c5fd;
        font-weight: 700;
        font-size: 1.15rem;
        border-bottom: 1px solid rgba(59, 130, 246, 0.3);
        padding-bottom: 8px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Auditor Agent - Verification */
    .agent-card-auditor {
        border: 2px solid #10b981;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);
    }
    .header-auditor {
        color: #6ee7b7;
        font-weight: 700;
        font-size: 1.15rem;
        border-bottom: 1px solid rgba(16, 185, 129, 0.3);
        padding-bottom: 8px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Code & Log Output Styling */
    .agent-log {
        font-family: 'Fira Code', 'Courier New', Courier, monospace;
        font-size: 0.88rem;
        line-height: 1.5;
        white-space: pre-wrap;
        word-break: break-word;
        color: #cbd5e1;
        background-color: #090d16;
        padding: 12px;
        border-radius: 6px;
        max-height: 400px;
        overflow-y: auto;
    }
    
    .status-badge {
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .status-idle { background: #334155; color: #cbd5e1; }
    .status-running { background: #854d0e; color: #fef08a; }
    .status-success { background: #14532d; color: #86efac; }
</style>
""", unsafe_allow_html=True)

# Main Title & Header
st.markdown('<div class="soc-header">🛡️ RedSentinel: Autonomous SOC Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="soc-subtitle">Sequential Autonomous Multi-Agent Threat Simulation & Defense powered by <code>@mozaik-ai/core</code></div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚡ SOC Agent Runtime")
    st.markdown("""
    **Active Agents:**
    -  **Red Agent**: Offensive vulnerability analysis
    -  **Blue Agent**: Defensive firewall & rule mitigation
    - **Auditor Agent**: OWASP & state compliance check
    
    ---
    **Framework Specification:**
    - Package: `@mozaik-ai/core` v4.0.5
    - Architecture: Asynchronous Sequential Pipeline
    """)
    st.markdown("---")
    st.caption("RedSentinel Operations v1.0")

# Input Section
scenario_input = st.text_area(
    "Security Threat Scenario:",
    placeholder="e.g., Kinal platform breach via DDoS and dictionary attack to manipulate grades",
    height=100
)

col1, col2, col3 = st.columns([1.5, 2, 2])
with col1:
    start_simulation = st.button("🚀 Run SOC Agent Pipeline", type="primary", use_container_width=True)

# Setup 3-Column Layout for the 3 Agents
col_red, col_blue, col_auditor = st.columns(3)

with col_red:
    red_placeholder = st.empty()

with col_blue:
    blue_placeholder = st.empty()

with col_auditor:
    auditor_placeholder = st.empty()

# Initial render of empty/idle cards
def render_card(placeholder, agent_type, title, icon, content, status="IDLE"):
    status_class = "status-idle" if status == "IDLE" else ("status-running" if status == "RUNNING" else "status-success")
    border_class = f"agent-card-{agent_type}"
    header_class = f"header-{agent_type}"
    
    escaped_content = html.escape(content) if content else "Waiting for simulation event..."
    
    html_code = f"""
    <div class="agent-card {border_class}">
        <div class="{header_class}">
            <span>{icon} {title}</span>
            <span class="status-badge {status_class}" style="margin-left: auto;">{status}</span>
        </div>
        <pre class="agent-log">{escaped_content}</pre>
    </div>
    """
    placeholder.markdown(html_code, unsafe_allow_html=True)

# Render initial state
render_card(red_placeholder, "red", "Red Agent (Offensive)", "🔴", "", "IDLE")
render_card(blue_placeholder, "blue", "Blue Agent (Defensive)", "🔵", "", "IDLE")
render_card(auditor_placeholder, "auditor", "Auditor Agent (Compliance)", "🟢", "", "IDLE")

# Execution loop
if start_simulation:
    if scenario_input.strip():
        # Set cards to pending/running state
        render_card(red_placeholder, "red", "Red Agent (Offensive)", "🔴", "Initializing vulnerability analysis...", "RUNNING")
        render_card(blue_placeholder, "blue", "Blue Agent (Defensive)", "🔵", "Waiting for Red Agent telemetry...", "IDLE")
        render_card(auditor_placeholder, "auditor", "Auditor Agent (Compliance)", "🟢", "Waiting for Blue Agent mitigation rules...", "IDLE")
        
        red_buffer = ""
        blue_buffer = ""
        auditor_buffer = ""
        raw_logs = []
        
        current_agent = "red"
        
        npx_cmd = "npx.cmd" if sys.platform == "win32" else "npx"
        cmd = [npx_cmd, "ts-node", "index.ts", scenario_input]
        
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            if process.stdout:
                for line in iter(process.stdout.readline, ''):
                    # Filter out cloud telemetry warning lines
                    if "mozaik cloud:" in line or "telemetry disabled" in line:
                        continue
                    
                    # Store filtered line in raw log history
                    raw_logs.append(line)
                    
                    # Routing logic based on log headers and agent markers
                    if "[Red Agent]" in line or "[RED TELEMETRY]" in line:
                        current_agent = "red"
                        render_card(red_placeholder, "red", "Red Agent (Offensive)", "🔴", red_buffer + line, "RUNNING")
                    elif "[Blue Agent]" in line or "[BLUE MITIGATION]" in line:
                        current_agent = "blue"
                        render_card(red_placeholder, "red", "Red Agent (Offensive)", "🔴", red_buffer, "COMPLETE")
                        render_card(blue_placeholder, "blue", "Blue Agent (Defensive)", "🔵", blue_buffer + line, "RUNNING")
                    elif "[Auditor Agent]" in line or "[AUDITOR VERIFICATION]" in line:
                        current_agent = "auditor"
                        render_card(blue_placeholder, "blue", "Blue Agent (Defensive)", "🔵", blue_buffer, "COMPLETE")
                        render_card(auditor_placeholder, "auditor", "Auditor Agent (Compliance)", "🟢", auditor_buffer + line, "RUNNING")
                    
                    # Clean transcript separator lines
                    if "--- [LIVE RUNTIME TRANSCRIPT] ---" in line or "Producer Agent ID:" in line or "---------------------------------" in line:
                        continue
                    
                    # Append output line to current active agent buffer
                    if current_agent == "red":
                        red_buffer += line
                        render_card(red_placeholder, "red", "Red Agent (Offensive)", "🔴", red_buffer, "RUNNING")
                    elif current_agent == "blue":
                        blue_buffer += line
                        render_card(blue_placeholder, "blue", "Blue Agent (Defensive)", "🔵", blue_buffer, "RUNNING")
                    elif current_agent == "auditor":
                        auditor_buffer += line
                        render_card(auditor_placeholder, "auditor", "Auditor Agent (Compliance)", "🟢", auditor_buffer, "RUNNING")
                
                process.stdout.close()
            
            return_code = process.wait()
            
            # Final state update for all cards
            render_card(red_placeholder, "red", "Red Agent (Offensive)", "🔴", red_buffer, "COMPLETE")
            render_card(blue_placeholder, "blue", "Blue Agent (Defensive)", "🔵", blue_buffer, "COMPLETE")
            render_card(auditor_placeholder, "auditor", "Auditor Agent (Compliance)", "🟢", auditor_buffer, "COMPLETE")
            
            if return_code == 0:
                st.success("✅ Multi-Agent SOC Threat Neutralization Sequence Completed Successfully!")
            else:
                st.error(f"❌ Process exited with non-zero exit status: {return_code}")
                
            # Collapsible Expander for Raw Log Inspection
            with st.expander("🔍 View Raw Filtered Console Transcript"):
                st.code("".join(raw_logs), language="text")
                
        except Exception as e:
            st.error(f"Failed to execute Mozaik SOC backend: {str(e)}")
    else:
        st.warning("⚠️ Please enter a threat scenario before starting the pipeline.")