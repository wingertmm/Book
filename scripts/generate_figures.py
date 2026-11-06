#!/usr/bin/env python3
"""
Publication Figure Generator: Timing, Distance, and Power
Generates high-resolution (300 DPI equivalent) vector-rendered graphics for manuscript figures
using Playwright headless Chromium.

Outputs to: exports/figures/
"""

import os
import sys
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

REPO_ROOT = Path("C:/Book")
FIGURES_DIR = REPO_ROOT / "exports" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# HTML / SVG Templates
# ---------------------------------------------------------------------------

def get_figure_1_1_html():
    """Figure 1.1: The Mechanical Triad (Timing, Distance, Power) with Efficiency at the Core."""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
  
  * { box-sizing: border-box; margin: 0; padding: 0; }
  
  body {
    width: 1200px;
    height: 900px;
    background-color: #F8FAFC;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #1E293B;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 40px;
  }
  
  .card {
    width: 1120px;
    height: 820px;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.03);
    padding: 36px 44px;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
  }
  
  /* Top Banner */
  .header {
    border-bottom: 2px solid #EDF2F7;
    padding-bottom: 16px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  
  .title-area h1 {
    font-size: 24px;
    font-weight: 800;
    color: #1A365D;
    letter-spacing: -0.5px;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  
  .title-area p {
    font-size: 14px;
    color: #4A5568;
    font-weight: 500;
  }
  
  .badge {
    background: #EBF8FF;
    color: #2B6CB0;
    border: 1px solid #BEE3F8;
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
  }
  
  /* SVG Container */
  .diagram-container {
    flex: 1;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  svg {
    width: 1000px;
    height: 600px;
  }
  
  /* Technical Footnote */
  .footer {
    border-top: 1px solid #EDF2F7;
    padding-top: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 12px;
    color: #718096;
  }
  
  .footer-formula {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    color: #2D3748;
    background: #F7FAFC;
    padding: 4px 10px;
    border-radius: 6px;
    border: 1px solid #E2E8F0;
  }
</style>
</head>
<body>

<div class="card">
  <div class="header">
    <div class="title-area">
      <h1>Figure 1.1: The Mechanical Triad of Combatives</h1>
      <p>The Three Operational Variables Converging to Produce Peak Kinetic Efficiency</p>
    </div>
    <div class="badge">Axiomatic Architecture</div>
  </div>
  
  <div class="diagram-container">
    <svg viewBox="0 0 1000 580" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Gradients -->
        <linearGradient id="triGrad" x1="500" y1="60" x2="500" y2="480" gradientUnits="userSpaceOnUse">
          <stop offset="0%" stop-color="#2B6CB0" stop-opacity="0.08"/>
          <stop offset="100%" stop-color="#1A365D" stop-opacity="0.18"/>
        </linearGradient>
        
        <linearGradient id="edgeTiming" x1="500" y1="70" x2="200" y2="460" gradientUnits="userSpaceOnUse">
          <stop offset="0%" stop-color="#2B6CB0"/>
          <stop offset="100%" stop-color="#3182CE"/>
        </linearGradient>
        
        <linearGradient id="edgeDist" x1="500" y1="70" x2="800" y2="460" gradientUnits="userSpaceOnUse">
          <stop offset="0%" stop-color="#2B6CB0"/>
          <stop offset="100%" stop-color="#319795"/>
        </linearGradient>
        
        <linearGradient id="edgePower" x1="200" y1="460" x2="800" y2="460" gradientUnits="userSpaceOnUse">
          <stop offset="0%" stop-color="#3182CE"/>
          <stop offset="50%" stop-color="#C53030"/>
          <stop offset="100%" stop-color="#319795"/>
        </linearGradient>
        
        <linearGradient id="coreGrad" x1="420" y1="260" x2="580" y2="380" gradientUnits="userSpaceOnUse">
          <stop offset="0%" stop-color="#1A365D"/>
          <stop offset="100%" stop-color="#0F172A"/>
        </linearGradient>
        
        <!-- Glow Filter -->
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.15"/>
        </filter>
        <filter id="coreGlow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#2B6CB0" flood-opacity="0.25"/>
        </filter>
      </defs>

      <!-- Background Subtle Geometry -->
      <circle cx="500" cy="330" r="220" stroke="#E2E8F0" stroke-width="1.5" stroke-dasharray="4 4"/>
      <circle cx="500" cy="330" r="160" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="2 2"/>

      <!-- Inward Flow Vectors from vertices to centroid -->
      <line x1="500" y1="80" x2="500" y2="250" stroke="#94A3B8" stroke-width="2" stroke-dasharray="5 5"/>
      <polygon points="500,256 495,244 505,244" fill="#64748B"/>
      
      <line x1="200" y1="460" x2="430" y2="370" stroke="#94A3B8" stroke-width="2" stroke-dasharray="5 5"/>
      <polygon points="436,368 424,364 430,374" fill="#64748B"/>
      
      <line x1="800" y1="460" x2="570" y2="370" stroke="#94A3B8" stroke-width="2" stroke-dasharray="5 5"/>
      <polygon points="564,368 570,374 576,364" fill="#64748B"/>

      <!-- Main Triangle Body -->
      <polygon points="500,80 800,460 200,460" fill="url(#triGrad)" stroke="#CBD5E1" stroke-width="2"/>

      <!-- Outer Triangle Edges (Thickened Accents) -->
      <!-- Left Edge: Timing -->
      <line x1="500" y1="80" x2="200" y2="460" stroke="url(#edgeTiming)" stroke-width="6" stroke-linecap="round"/>
      <!-- Right Edge: Distance -->
      <line x1="500" y1="80" x2="800" y2="460" stroke="url(#edgeDist)" stroke-width="6" stroke-linecap="round"/>
      <!-- Bottom Edge: Power -->
      <line x1="200" y1="460" x2="800" y2="460" stroke="url(#edgePower)" stroke-width="6" stroke-linecap="round"/>

      <!-- Vertex Nodes -->
      <circle cx="500" cy="80" r="12" fill="#FFFFFF" stroke="#2B6CB0" stroke-width="4" filter="url(#glow)"/>
      <circle cx="200" cy="460" r="12" fill="#FFFFFF" stroke="#3182CE" stroke-width="4" filter="url(#glow)"/>
      <circle cx="800" cy="460" r="12" fill="#FFFFFF" stroke="#319795" stroke-width="4" filter="url(#glow)"/>

      <!-- Central Core: EFFICIENCY -->
      <g filter="url(#coreGlow)">
        <!-- Core Outer Ring -->
        <circle cx="500" cy="333" r="88" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="2"/>
        <!-- Core Disc -->
        <circle cx="500" cy="333" r="80" fill="url(#coreGrad)"/>
        <!-- Accent Inner Ring -->
        <circle cx="500" cy="333" r="74" fill="none" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3 3"/>
        
        <!-- Core Typography -->
        <text x="500" y="318" text-anchor="middle" font-family="'Inter', sans-serif" font-weight="800" font-size="20" fill="#FFFFFF" letter-spacing="1.5">EFFICIENCY</text>
        <text x="500" y="338" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-weight="600" font-size="14" fill="#38BDF8">η = W_eff / E_met</text>
        <text x="500" y="358" text-anchor="middle" font-family="'Inter', sans-serif" font-weight="600" font-size="10.5" fill="#94A3B8" letter-spacing="0.5">THE END RESULT</text>
      </g>

      <!-- EDGE 1: TIMING CALLOUT (Left Face) -->
      <g transform="translate(190, 220)" filter="url(#glow)">
        <rect x="0" y="0" width="180" height="74" rx="10" fill="#FFFFFF" stroke="#3182CE" stroke-width="2"/>
        <rect x="0" y="0" width="6" height="74" rx="3" fill="#3182CE"/>
        <text x="18" y="24" font-family="'Inter', sans-serif" font-weight="800" font-size="14" fill="#1A365D" letter-spacing="0.5">TIMING ( Δt )</text>
        <text x="18" y="42" font-family="'Inter', sans-serif" font-weight="600" font-size="11" fill="#4A5568">Temporal Precision</text>
        <text x="18" y="58" font-family="'Inter', sans-serif" font-weight="500" font-size="10" fill="#718096">Seizes decision windows</text>
      </g>

      <!-- EDGE 2: DISTANCE CALLOUT (Right Face) -->
      <g transform="translate(630, 220)" filter="url(#glow)">
        <rect x="0" y="0" width="180" height="74" rx="10" fill="#FFFFFF" stroke="#319795" stroke-width="2"/>
        <rect x="0" y="0" width="6" height="74" rx="3" fill="#319795"/>
        <text x="18" y="24" font-family="'Inter', sans-serif" font-weight="800" font-size="14" fill="#1A365D" letter-spacing="0.5">DISTANCE ( d )</text>
        <text x="18" y="42" font-family="'Inter', sans-serif" font-weight="600" font-size="11" fill="#4A5568">Spatial Geometry</text>
        <text x="18" y="58" font-family="'Inter', sans-serif" font-weight="500" font-size="10" fill="#718096">Reactionary gap & lever</text>
      </g>

      <!-- EDGE 3: POWER CALLOUT (Bottom Face) -->
      <g transform="translate(410, 478)" filter="url(#glow)">
        <rect x="0" y="0" width="180" height="74" rx="10" fill="#FFFFFF" stroke="#C53030" stroke-width="2"/>
        <rect x="0" y="0" width="6" height="74" rx="3" fill="#C53030"/>
        <text x="18" y="24" font-family="'Inter', sans-serif" font-weight="800" font-size="14" fill="#1A365D" letter-spacing="0.5">POWER ( P = W/Δt )</text>
        <text x="18" y="42" font-family="'Inter', sans-serif" font-weight="600" font-size="11" fill="#4A5568">Kinetic Transfer</text>
        <text x="18" y="58" font-family="'Inter', sans-serif" font-weight="500" font-size="10" fill="#718096">Mass in coordinated motion</text>
      </g>

      <!-- Convergence Badges on Edges -->
      <g transform="translate(315, 235)">
        <circle cx="15" cy="15" r="15" fill="#EBF8FF" stroke="#3182CE" stroke-width="1.5"/>
        <text x="15" y="20" text-anchor="middle" font-family="'Inter', sans-serif" font-weight="800" font-size="11" fill="#2B6CB0">T</text>
      </g>
      
      <g transform="translate(645, 235)">
        <circle cx="15" cy="15" r="15" fill="#E6FFFA" stroke="#319795" stroke-width="1.5"/>
        <text x="15" y="20" text-anchor="middle" font-family="'Inter', sans-serif" font-weight="800" font-size="11" fill="#234E52">D</text>
      </g>
      
      <g transform="translate(485, 445)">
        <circle cx="15" cy="15" r="15" fill="#FFF5F5" stroke="#C53030" stroke-width="1.5"/>
        <text x="15" y="20" text-anchor="middle" font-family="'Inter', sans-serif" font-weight="800" font-size="11" fill="#9B2C2C">P</text>
      </g>
    </svg>
  </div>
  
  <div class="footer">
    <div><strong>Principle:</strong> An efficient fighter wins. Efficiency is the operational state achieved when power is directed by timing and protected by distance.</div>
    <div class="footer-formula">Efficiency = Decisive Effect ÷ Metabolic Cost</div>
  </div>
</div>

</body>
</html>
"""

def get_figure_1_2_html():
    """Figure 1.2: The Master Equation Kinetic Flowchart."""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1200px;
    height: 580px;
    background-color: #F8FAFC;
    font-family: 'Inter', -apple-system, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 24px 30px;
  }
  .card {
    width: 1140px;
    height: 532px;
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 16px;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    padding: 24px 32px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .header {
    border-bottom: 2px solid #EDF2F7;
    padding-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .header h1 { font-size: 21px; font-weight: 800; color: #1A365D; text-transform: uppercase; letter-spacing: -0.3px; }
  .header p { font-size: 13px; color: #4A5568; font-weight: 500; margin-top: 3px; }
  .badge { background: #EBF8FF; color: #2B6CB0; border: 1px solid #BEE3F8; padding: 5px 12px; border-radius: 9999px; font-size: 11px; font-weight: 700; font-family: 'JetBrains Mono', monospace; }
  
  .flow-row {
    display: flex;
    align-items: stretch;
    justify-content: space-between;
    margin: 16px 0;
    gap: 8px;
  }
  .step-node {
    flex: 1;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    padding: 16px 14px;
    position: relative;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
  }
  .step-node.active { border-top: 4px solid #2B6CB0; }
  .step-node.highlight { border-top: 4px solid #C53030; }
  
  .step-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 4px;
  }
  .step-num { font-family: 'JetBrains Mono', monospace; font-size: 10.5px; font-weight: 700; color: #718096; }
  .step-title { font-size: 16px; font-weight: 800; color: #1A365D; letter-spacing: -0.2px; }
  
  .role-badge {
    display: inline-block;
    align-self: flex-start;
    font-size: 10px;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    padding: 3px 8px;
    border-radius: 4px;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }
  .role-blue { background: #EBF8FF; color: #2B6CB0; border: 1px solid #BEE3F8; }
  .role-crimson { background: #FFF5F5; color: #C53030; border: 1px solid #FED7D7; }
  
  .step-desc {
    font-size: 11.5px;
    color: #334155;
    line-height: 1.45;
    flex: 1;
  }
  .step-desc strong { color: #0F172A; }
  
  .breakdown-box {
    margin-top: 10px;
    background: #FFF5F5;
    border-left: 3px solid #E53E3E;
    border-radius: 0 4px 4px 0;
    padding: 6px 8px;
  }
  .breakdown-label {
    font-size: 9px;
    font-weight: 800;
    color: #9B2C2C;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 2px;
  }
  .breakdown-text {
    font-size: 10.5px;
    color: #742A2A;
    line-height: 1.35;
  }
  
  .step-bottom {
    border-top: 1px dashed #CBD5E1;
    padding-top: 8px;
    margin-top: 10px;
    font-size: 10.5px;
    font-weight: 700;
    color: #475569;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.3px;
    text-align: center;
  }
  
  .arrow {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    align-self: center;
  }
  .arrow svg { width: 24px; height: 24px; }
  
  .footer {
    border-top: 1px solid #EDF2F7;
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11.5px;
    color: #64748B;
  }
  .footer strong { color: #1E293B; }
  .footer-right { font-family: 'JetBrains Mono', monospace; font-size: 10.5px; font-weight: 600; color: #475569; }
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div>
      <h1>Figure 1.2: The Master Equation Kinetic Cascade</h1>
      <p>Sequential Causal Pipeline: How Spatial Buffer Cascades into Decisive Kinetic Transfer</p>
    </div>
    <div class="badge">OPERATIONAL PIPELINE</div>
  </div>
  
  <div class="flow-row">
    <!-- Step 1: Distance -->
    <div class="step-node active">
      <div class="step-header">
        <div class="step-title">DISTANCE</div>
        <div class="step-num">STAGE 01</div>
      </div>
      <div class="role-badge role-blue">Spatial Buffer</div>
      <div class="step-desc">
        Enforces the <strong>Reactionary Gap</strong>. Physical space denies immediate hostile contact, forcing the attacker to commit forward mass across visible terrain.
      </div>
      <div class="breakdown-box">
        <div class="breakdown-label">System Breakdown If Lost</div>
        <div class="breakdown-text">Zero reaction window; defender is trapped in involuntary flinch response.</div>
      </div>
      <div class="step-bottom">REACTIONARY GAP</div>
    </div>
    
    <div class="arrow">
      <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#3182CE" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>
    
    <!-- Step 2: Time -->
    <div class="step-node active">
      <div class="step-header">
        <div class="step-title">TIME</div>
        <div class="step-num">STAGE 02</div>
      </div>
      <div class="role-badge role-blue">Cognitive Runway</div>
      <div class="step-desc">
        Expands the <strong>Decision Window</strong>. Closing distance requires measurable transit time (&gt;300 ms), enabling visual telemetry to read intent and choose response.
      </div>
      <div class="breakdown-box">
        <div class="breakdown-label">System Breakdown If Lost</div>
        <div class="breakdown-text">Cognitive freeze; sensory overload and panic lockup override motor pathways.</div>
      </div>
      <div class="step-bottom">DECISION WINDOW</div>
    </div>
    
    <div class="arrow">
      <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#3182CE" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>
    
    <!-- Step 3: Timing -->
    <div class="step-node active">
      <div class="step-header">
        <div class="step-title">TIMING</div>
        <div class="step-num">STAGE 03</div>
      </div>
      <div class="role-badge role-blue">Transition Seam</div>
      <div class="step-desc">
        Seizes the <strong>Window of Opportunity</strong>. Intercepts the adversary at peak vulnerability—precisely when forward weight is committed and balance is unrecoverable.
      </div>
      <div class="breakdown-box">
        <div class="breakdown-label">System Breakdown If Lost</div>
        <div class="breakdown-text">Braced collision; striking into a guarded line or hitting empty air.</div>
      </div>
      <div class="step-bottom">TACTICAL TRIGGER</div>
    </div>
    
    <div class="arrow">
      <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#C53030" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>
    
    <!-- Step 4: Power -->
    <div class="step-node highlight">
      <div class="step-header">
        <div class="step-title">POWER</div>
        <div class="step-num">STAGE 04</div>
      </div>
      <div class="role-badge role-crimson">Kinetic Transfer</div>
      <div class="step-desc">
        Delivers <strong>Decisive Work</strong>. Directs unified skeletal mass into exposed structural flaws with concentrated acceleration and zero dissipated motion.
      </div>
      <div class="breakdown-box">
        <div class="breakdown-label">System Breakdown If Lost</div>
        <div class="breakdown-text">Dissipated force; superficial impact fails to neutralize adversary momentum.</div>
      </div>
      <div class="step-bottom" style="color: #C53030;">TERMINAL RESOLUTION</div>
    </div>
  </div>
  
  <div class="footer">
    <div><strong>Doctrinal Invariant:</strong> Distance buys Time; Time enables Timing; Timing directs Power. If any stage is severed, the cascade collapses.</div>
    <div class="footer-right">Space ➔ Perception ➔ Interception ➔ Resolution</div>
  </div>
</div>
</body>
</html>
"""

def get_figure_12_1_html():
    """Figure 12.1: The Range Matrix: Standoff Defense vs. Chaos Zone."""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1200px;
    height: 750px;
    background-color: #F8FAFC;
    font-family: 'Inter', -apple-system, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 30px;
  }
  .card {
    width: 1140px;
    height: 690px;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    padding: 30px 40px;
    display: flex;
    flex-direction: column;
  }
  .header {
    border-bottom: 2px solid #EDF2F7;
    padding-bottom: 14px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .header h1 { font-size: 22px; font-weight: 800; color: #1A365D; text-transform: uppercase; }
  .header p { font-size: 13.5px; color: #4A5568; font-weight: 500; }
  .badge { background: #FEFCBF; color: #744210; border: 1px solid #F6E05E; padding: 5px 12px; border-radius: 9999px; font-size: 11px; font-weight: 700; font-family: 'JetBrains Mono', monospace; }
  
  .columns {
    flex: 1;
    display: flex;
    gap: 30px;
  }
  
  .col-box {
    flex: 1;
    border-radius: 12px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    border: 2px solid;
  }
  
  .col-threat {
    background: #FFF5F5;
    border-color: #FEB2B2;
  }
  
  .col-tactical {
    background: #F0FFF4;
    border-color: #9AE6B4;
  }
  
  .col-title {
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .col-threat .col-title { color: #9B2C2C; }
  .col-tactical .col-title { color: #22543D; }
  
  .col-metric {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 16px;
  }
  .col-threat .col-metric { color: #C53030; }
  .col-tactical .col-metric { color: #2F855A; }
  
  .feature-list {
    list-style: none;
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  
  .feature-item {
    font-size: 13px;
    line-height: 1.4;
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }
  
  .col-threat .feature-item { color: #742A2A; }
  .col-tactical .feature-item { color: #22543D; }
  
  .icon-cross { color: #E53E3E; font-weight: 800; }
  .icon-check { color: #38A169; font-weight: 800; }
  
  .outcome-box {
    margin-top: 16px;
    padding: 12px 16px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 700;
  }
  .col-threat .outcome-box { background: #FED7D7; color: #742A2A; border: 1px solid #FEB2B2; }
  .col-tactical .outcome-box { background: #C6F6D5; color: #22543D; border: 1px solid #9AE6B4; }
  
  .footer {
    border-top: 1px solid #EDF2F7;
    padding-top: 12px;
    display: flex;
    justify-content: space-between;
    font-size: 11.5px;
    color: #718096;
  }
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div>
      <h1>Figure 12.1: The Range Matrix: Standoff Defense vs. Chaos Zone</h1>
      <p>Tactical Geometry: Kicking Envelope Standoff vs. Punching/Blade Attrition</p>
    </div>
    <div class="badge">Spatial Defense Model</div>
  </div>
  
  <div class="columns">
    <!-- Left: Chaos Zone -->
    <div class="col-box col-threat">
      <div class="col-title">
        <span>CHAOS ZONE</span>
        <span style="font-size: 20px;">⚠️</span>
      </div>
      <div class="col-metric">PUNCHING / BLADE RANGE ( d &lt; 30 in )</div>
      
      <ul class="feature-list">
        <li class="feature-item">
          <span class="icon-cross">✕</span>
          <span><strong>Mutual Attrition Exchange:</strong> Both combatants operate within reciprocal strike range; defense becomes reactive and probabilistic.</span>
        </li>
        <li class="feature-item">
          <span class="icon-cross">✕</span>
          <span><strong>Severe Head Trauma Risk:</strong> Hooks, headbutts, and pavement impacts occur with zero deceleration margin.</span>
        </li>
        <li class="feature-item">
          <span class="icon-cross">✕</span>
          <span><strong>Concealed Weapon Trap:</strong> Edged weapons and impact tools deploy from pockets in &lt; 200 ms with zero reactionary buffer.</span>
        </li>
        <li class="feature-item">
          <span class="icon-cross">✕</span>
          <span><strong>Collapsed Escape Lanes:</strong> Attacker momentum crowds and traps the defender against obstacles or pavement.</span>
        </li>
      </ul>
      
      <div class="outcome-box">
        TERMINAL RESULT: Catastrophic Vulnerability (Survival Left to Random Chance)
      </div>
    </div>
    
    <!-- Right: Standoff Perimeter -->
    <div class="col-box col-tactical">
      <div class="col-title">
        <span>STANDOFF PERIMETER</span>
        <span style="font-size: 20px;">🛡️</span>
      </div>
      <div class="col-metric">KICKING ENVELOPE ( d &gt; 40 in )</div>
      
      <ul class="feature-list">
        <li class="feature-item">
          <span class="icon-check">✓</span>
          <span><strong>Asymmetric Spatial Leverage:</strong> Strike with the longest biological lever (the leg) while vital command centers remain out of reach.</span>
        </li>
        <li class="feature-item">
          <span class="icon-check">✓</span>
          <span><strong>Attacker Trapped by Space:</strong> Aggressor cannot land punches without physically crossing terrain (Δx = v · Δt).</span>
        </li>
        <li class="feature-item">
          <span class="icon-check">✓</span>
          <span><strong>Expanded Decision Window:</strong> Advance is telegraphed early, providing ample time for angular evasion or interception.</span>
        </li>
        <li class="feature-item">
          <span class="icon-check">✓</span>
          <span><strong>Preserved Egress Corridors:</strong> Standoff keeps escape routes open, allowing disengagement before chaos consolidates.</span>
        </li>
      </ul>
      
      <div class="outcome-box">
        TERMINAL RESULT: Decisive Counter &amp; Unhindered Disengagement Corridor
      </div>
    </div>
  </div>
  
  <div class="footer">
    <div><strong>Tactical Rule:</strong> Never trade punches on concrete. Standoff distance is structural armor that makes hostile strikes mechanically impossible.</div>
    <div>Δd_safety = d_kick - d_punch &gt; 12-18 inches</div>
  </div>
</div>
</body>
</html>
"""

def get_banner_master_equation_html():
    """Banner: Distance -> Time -> Timing -> Power."""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700;800&family=JetBrains+Mono:wght@700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1050px;
    height: 160px;
    background: transparent;
    font-family: 'Inter', -apple-system, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .card {
    width: 1020px;
    height: 140px;
    background: #FFFFFF;
    border: 1.5px solid #CBD5E1;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    position: relative;
    border-left: 6px solid #2B6CB0;
  }
  .node {
    flex: 1;
    height: 86px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 8px;
    text-align: center;
  }
  .node.final {
    background: #FFF5F5;
    border-color: #FEB2B2;
  }
  .node-title {
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 0.5px;
    color: #1A365D;
    margin-bottom: 4px;
  }
  .node.final .node-title { color: #9B2C2C; }
  .node-sub {
    font-size: 11px;
    font-weight: 600;
    color: #64748B;
  }
  .node.final .node-sub { color: #C53030; }
  .arrow {
    width: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .arrow svg { width: 24px; height: 24px; }
  .pipeline-tag {
    position: absolute;
    top: -10px;
    left: 20px;
    background: #1A365D;
    color: #FFFFFF;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 2px 10px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
  }
</style>
</head>
<body>
<div class="card">
  <div class="pipeline-tag">Operational Master Equation</div>
  <div class="node">
    <div class="node-title">DISTANCE</div>
    <div class="node-sub">Enforces Reactionary Gap</div>
  </div>
  <div class="arrow">
    <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#3182CE" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="node">
    <div class="node-title">TIME</div>
    <div class="node-sub">Expands Decision Window</div>
  </div>
  <div class="arrow">
    <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#3182CE" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="node">
    <div class="node-title">TIMING</div>
    <div class="node-sub">Seizes Vulnerable Seam</div>
  </div>
  <div class="arrow">
    <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#C53030" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="node final">
    <div class="node-title">POWER</div>
    <div class="node-sub">Delivers Kinetic Work</div>
  </div>
</div>
</body>
</html>
"""

def get_banner_triad_principles_html():
    """Banner: Distance -> Time -> Power."""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700;800&family=JetBrains+Mono:wght@700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 900px;
    height: 150px;
    background: transparent;
    font-family: 'Inter', -apple-system, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .card {
    width: 860px;
    height: 125px;
    background: #FFFFFF;
    border: 1.5px solid #CBD5E1;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 28px;
    position: relative;
    border-left: 6px solid #2B6CB0;
  }
  .node {
    flex: 1;
    height: 76px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 6px;
    text-align: center;
  }
  .node.final { background: #FFF5F5; border-color: #FEB2B2; }
  .node-title { font-size: 15px; font-weight: 800; letter-spacing: 0.5px; color: #1A365D; margin-bottom: 2px; }
  .node.final .node-title { color: #9B2C2C; }
  .node-sub { font-size: 11px; font-weight: 600; color: #64748B; }
  .node.final .node-sub { color: #C53030; }
  .arrow { width: 44px; display: flex; align-items: center; justify-content: center; }
  .arrow svg { width: 26px; height: 26px; }
  .pipeline-tag {
    position: absolute;
    top: -10px;
    left: 20px;
    background: #1A365D;
    color: #FFFFFF;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 2px 10px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
  }
</style>
</head>
<body>
<div class="card">
  <div class="pipeline-tag">Strategic Invariant Cascade</div>
  <div class="node">
    <div class="node-title">DISTANCE</div>
    <div class="node-sub">Spatial Defense &amp; Standoff</div>
  </div>
  <div class="arrow">
    <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#3182CE" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="node">
    <div class="node-title">TIME</div>
    <div class="node-sub">Temporal Decision Window</div>
  </div>
  <div class="arrow">
    <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#C53030" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="node final">
    <div class="node-title">POWER</div>
    <div class="node-sub">Concentrated Kinetic Impact</div>
  </div>
</div>
</body>
</html>
"""

def get_banner_4_step_cycle_html():
    """Banner: Recognize -> Prioritize -> Choose -> Act & Reassess."""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700;800&family=JetBrains+Mono:wght@700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1050px;
    height: 160px;
    background: transparent;
    font-family: 'Inter', -apple-system, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .card {
    width: 1020px;
    height: 140px;
    background: #FFFFFF;
    border: 1.5px solid #CBD5E1;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    position: relative;
    border-left: 6px solid #2B6CB0;
  }
  .node {
    flex: 1;
    height: 86px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 6px;
    text-align: center;
  }
  .node.final { background: #F0FFF4; border-color: #9AE6B4; }
  .node-title { font-size: 14px; font-weight: 800; letter-spacing: 0.5px; color: #1A365D; margin-bottom: 4px; }
  .node.final .node-title { color: #22543D; }
  .node-sub { font-size: 10.5px; font-weight: 600; color: #64748B; }
  .node.final .node-sub { color: #2F855A; }
  .arrow { width: 34px; display: flex; align-items: center; justify-content: center; }
  .arrow svg { width: 22px; height: 22px; }
  .pipeline-tag {
    position: absolute;
    top: -10px;
    left: 20px;
    background: #1A365D;
    color: #FFFFFF;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 2px 10px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
  }
</style>
</head>
<body>
<div class="card">
  <div class="pipeline-tag">The Tactical Decision Engine (Chapter 17)</div>
  <div class="node">
    <div class="node-title">1. RECOGNIZE</div>
    <div class="node-sub">Sensory Threat Cues</div>
  </div>
  <div class="arrow">
    <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#3182CE" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="node">
    <div class="node-title">2. PRIORITIZE</div>
    <div class="node-sub">Filter Lethal Vectors</div>
  </div>
  <div class="arrow">
    <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#3182CE" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="node">
    <div class="node-title">3. CHOOSE</div>
    <div class="node-sub">Binary Engram Selection</div>
  </div>
  <div class="arrow">
    <svg viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#38A169" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="node final">
    <div class="node-title">4. ACT &amp; REASSESS</div>
    <div class="node-sub">Execute &amp; Close Loop</div>
  </div>
</div>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Generator Runner
# ---------------------------------------------------------------------------

FIGURES_TO_RENDER = [
    {
        "id": "fig_01_the_triad",
        "title": "Figure 1.1: The Mechanical Triad (Timing, Distance, Power) & Efficiency",
        "html_fn": get_figure_1_1_html,
        "width": 1200,
        "height": 900,
        "scale": 2, # Retina / 300 DPI equivalent
    },
    {
        "id": "fig_02_master_equation",
        "title": "Figure 1.2: The Master Equation Kinetic Cascade",
        "html_fn": get_figure_1_2_html,
        "width": 1200,
        "height": 580,
        "scale": 2,
    },
    {
        "id": "fig_12_01_range_matrix",
        "title": "Figure 12.1: The Range Matrix: Standoff Defense vs. Chaos Zone",
        "html_fn": get_figure_12_1_html,
        "width": 1200,
        "height": 750,
        "scale": 2,
    },
    {
        "id": "banner_master_equation",
        "title": "Banner: Operational Master Equation (Distance -> Time -> Timing -> Power)",
        "html_fn": get_banner_master_equation_html,
        "width": 1050,
        "height": 160,
        "scale": 2,
    },
    {
        "id": "banner_triad_principles",
        "title": "Banner: Strategic Invariant Cascade (Distance -> Time -> Power)",
        "html_fn": get_banner_triad_principles_html,
        "width": 900,
        "height": 150,
        "scale": 2,
    },
    {
        "id": "banner_4_step_cycle",
        "title": "Banner: The 4-Step Cycle (Recognize -> Prioritize -> Choose -> Act)",
        "html_fn": get_banner_4_step_cycle_html,
        "width": 1050,
        "height": 160,
        "scale": 2,
    }
]

async def render_all():
    print(f"[FIG-GEN] Initializing Playwright Chromium at 2x Scale (Retina / 300 DPI)...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        for item in FIGURES_TO_RENDER:
            fig_id = item["id"]
            out_png = FIGURES_DIR / f"{fig_id}.png"
            print(f"[FIG-GEN] Rendering: {item['title']} -> {out_png.name}...")
            
            page = await browser.new_page(
                viewport={"width": item["width"], "height": item["height"]},
                device_scale_factor=item["scale"]
            )
            html_content = item["html_fn"]()
            await page.set_content(html_content, wait_until="networkidle")
            await page.screenshot(path=str(out_png))
            await page.close()
            
            file_size_kb = out_png.stat().st_size / 1024
            print(f"  [OK] Rendered {out_png.name} ({file_size_kb:.1f} KB)")
            
        await browser.close()
    print("[FIG-GEN] Figure generation complete!")

if __name__ == "__main__":
    asyncio.run(render_all())
