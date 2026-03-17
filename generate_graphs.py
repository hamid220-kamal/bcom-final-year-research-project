"""Generate 8 styled charts for the GST research project."""
import os, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

ASSETS = r"c:\Users\HAMID KAMAL\Downloads\bcom final year research project\assets"
os.makedirs(ASSETS, exist_ok=True)

NAVY = '#1A3A6B'; GOLD = '#B48214'; RED = '#B41E1E'
GREEN = '#1E7840'; LIGHT = '#D6E4F7'; GRAY = '#787878'
COLORS = ['#1A3A6B','#B48214','#B41E1E','#1E7840','#5B8DB8','#E8C56B','#A0522D']

plt.rcParams.update({'font.family':'DejaVu Serif','font.size':10})

def save(name):
    p = os.path.join(ASSETS, name)
    plt.tight_layout()
    plt.savefig(p, dpi=140, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'  Saved: {name}')

# ─── Fig 1: GST Awareness (Pie) ───────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7,5))
labels = ['Fully Aware','Moderately Aware','Partially Aware','Unaware']
sizes  = [15, 50, 25, 10]
explode= (0.05,0.05,0,0)
wedge_colors = [NAVY, GOLD, GREEN, GRAY]
wedges,texts,autotexts = ax.pie(sizes,labels=labels,colors=wedge_colors,
    explode=explode,autopct='%1.0f%%',startangle=140,
    textprops={'fontsize':10,'fontweight':'bold'})
for at in autotexts: at.set_color('white'); at.set_fontsize(9)
ax.set_title('Figure 1: GST Awareness Levels Among Sole Traders (n=50)',
             fontsize=12, fontweight='bold', color=NAVY, pad=14)
fig.patch.set_facecolor('#F8FAFC')
save('awareness_chart.png')

# ─── Fig 2: Pricing Impact (Bar) ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8,5))
cats = ['Prices Increased\nSignificantly','Marginal\nIncrease','No Change','Decrease\n(ITC Benefit)']
vals = [50,30,10,10]
bars = ax.bar(cats, vals, color=[RED,GOLD,GREEN,NAVY], edgecolor='white', linewidth=1.2, width=0.55)
for b in bars:
    ax.text(b.get_x()+b.get_width()/2, b.get_height()+1, f'{b.get_height()}%',
            ha='center', fontweight='bold', color=NAVY, fontsize=11)
ax.set_ylabel('Percentage of Respondents (%)', fontsize=10, color=GRAY)
ax.set_ylim(0,65); ax.set_facecolor('#F8FAFC')
ax.yaxis.grid(True, linestyle='--', alpha=0.5); ax.set_axisbelow(True)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.set_title('Figure 2: Impact of GST on Pricing of Goods/Services (n=50)',
             fontsize=12, fontweight='bold', color=NAVY, pad=12)
save('pricing_chart.png')

# ─── Fig 3: Challenges (Horizontal Bar) ──────────────────────────────────────
fig, ax = plt.subplots(figsize=(8,5))
challs = ['HSN Code\nConfusion','Delayed\nITC Refunds','Technology\nCost','Complex\nFiling']
vals   = [10,20,26,44]
bars = ax.barh(challs, vals, color=[GREEN,GOLD,RED,NAVY], edgecolor='white',
               linewidth=1, height=0.5)
for b in bars:
    ax.text(b.get_width()+0.8, b.get_y()+b.get_height()/2,
            f'{b.get_width()}%', va='center', fontweight='bold', color=NAVY, fontsize=11)
ax.set_xlabel('Percentage of Respondents (%)', fontsize=10, color=GRAY)
ax.set_xlim(0,58); ax.set_facecolor('#F8FAFC')
ax.xaxis.grid(True, linestyle='--', alpha=0.5); ax.set_axisbelow(True)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.set_title('Figure 3: Significant Challenges Under GST (n=50)',
             fontsize=12, fontweight='bold', color=NAVY, pad=12)
save('challenges_chart.png')

# ─── Fig 4: Benefits (Line) ───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8,5))
benefits = ['Logistical\nEfficiency','Transparent\nAccounting','Market\nUnification','Reduced\nCascading']
vals     = [70,80,60,30]
x = np.arange(len(benefits))
ax.plot(x, vals, marker='o', color=NAVY, linewidth=2.5, markersize=10, zorder=3)
ax.fill_between(x, vals, alpha=0.15, color=NAVY)
for i,(xi,yi) in enumerate(zip(x,vals)):
    ax.text(xi, yi+2.5, f'{yi}%', ha='center', fontweight='bold', color=NAVY, fontsize=11)
ax.set_xticks(x); ax.set_xticklabels(benefits, fontsize=10)
ax.set_ylabel('% Respondents Agreeing', fontsize=10, color=GRAY)
ax.set_ylim(0,100); ax.set_facecolor('#F8FAFC')
ax.yaxis.grid(True, linestyle='--', alpha=0.5); ax.set_axisbelow(True)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.set_title('Figure 4: Economic Benefits Observed Post-GST (n=50)',
             fontsize=12, fontweight='bold', color=NAVY, pad=12)
save('benefits_chart.png')

# ─── Fig 5: Business Type (Pie) ───────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7,5))
labels = ['Retail/Trading\n(60%)','Service/Prof\n(24%)','Manufacturing\n(16%)']
sizes  = [60,24,16]
wedge_colors = [NAVY, GOLD, RED]
wedges,texts,autotexts = ax.pie(sizes,labels=labels,colors=wedge_colors,
    autopct='%1.0f%%',startangle=90,textprops={'fontsize':10,'fontweight':'bold'})
for at in autotexts: at.set_color('white'); at.set_fontsize(9)
ax.set_title('Figure 5: Distribution by Type of Business (n=50)',
             fontsize=12, fontweight='bold', color=NAVY, pad=14)
fig.patch.set_facecolor('#F8FAFC')
save('business_type_chart.png')

# ─── Fig 6: Pre-GST vs Post-GST Tax Comparison (Grouped Bar) ─────────────────
fig, ax = plt.subplots(figsize=(8,5))
categories = ['Retail\nTrader','Restaurant','Service\nProvider','Manufacturer']
pre_gst  = [7, 14, 12, 14]
post_gst = [1,  5,  6, 18]
x = np.arange(len(categories)); w = 0.32
b1 = ax.bar(x-w/2, pre_gst, w, label='Pre-GST Effective Rate', color=RED, edgecolor='white')
b2 = ax.bar(x+w/2, post_gst, w, label='Post-GST Rate (Composition)', color=NAVY, edgecolor='white')
for b in list(b1)+list(b2):
    ax.text(b.get_x()+b.get_width()/2, b.get_height()+0.3, f'{b.get_height()}%',
            ha='center', fontsize=9, fontweight='bold', color='white' if b.get_height()>3 else NAVY)
ax.set_ylabel('Effective Tax Rate (%)', fontsize=10, color=GRAY)
ax.set_xticks(x); ax.set_xticklabels(categories)
ax.legend(fontsize=9); ax.set_facecolor('#F8FAFC')
ax.yaxis.grid(True, linestyle='--', alpha=0.5); ax.set_axisbelow(True)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.set_title('Figure 6: Pre-GST vs Post-GST Effective Tax Rate Comparison',
             fontsize=12, fontweight='bold', color=NAVY, pad=12)
save('tax_comparison_chart.png')

# ─── Fig 7: Monthly Compliance Cost Distribution (Stacked Bar) ────────────────
fig, ax = plt.subplots(figsize=(8,5))
trader_types = ['Retail\nTrader','Service\nProvider','Manufacturer','Restaurant\nOwner']
acc_fees   = [1200,1800,2200,1500]
software   = [300, 500, 600, 300]
time_cost  = [800,1200,1500,1000]
x = np.arange(len(trader_types))
p1 = ax.bar(x, acc_fees,  color=NAVY, label='Accountant Fees (Rs/month)')
p2 = ax.bar(x, software,  bottom=acc_fees, color=GOLD, label='Software/Internet (Rs/month)')
p3 = ax.bar(x, time_cost, bottom=[a+b for a,b in zip(acc_fees,software)],
            color=RED, label='Time Cost (Rs equivalent)')
ax.set_ylabel('Monthly Compliance Cost (Rs)', fontsize=10, color=GRAY)
ax.set_xticks(x); ax.set_xticklabels(trader_types)
ax.legend(fontsize=8, loc='upper left'); ax.set_facecolor('#F8FAFC')
ax.yaxis.grid(True, linestyle='--', alpha=0.5); ax.set_axisbelow(True)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.set_title('Figure 7: Monthly GST Compliance Cost by Trader Type',
             fontsize=12, fontweight='bold', color=NAVY, pad=12)
save('compliance_cost_chart.png')

# ─── Fig 8: ITC Utilisation vs Non-utilisation (Donut) ───────────────────────
fig, ax = plt.subplots(figsize=(7,5))
labels_d = ['Claim ITC\n(Regular)','Unaware of\nITC','Ineligible\n(Composition)']
sizes_d  = [30,40,30]
wcolors  = [GREEN, RED, NAVY]
wedges,texts,autotexts = ax.pie(sizes_d, labels=labels_d, colors=wcolors,
    autopct='%1.0f%%', startangle=90, pctdistance=0.75,
    wedgeprops=dict(width=0.55), textprops={'fontsize':10,'fontweight':'bold'})
for at in autotexts: at.set_color('white'); at.set_fontsize(9)
ax.text(0,0,'ITC\nUsage', ha='center', va='center', fontsize=12,
        fontweight='bold', color=NAVY)
ax.set_title('Figure 8: Input Tax Credit (ITC) Utilisation Among Respondents (n=50)',
             fontsize=12, fontweight='bold', color=NAVY, pad=14)
fig.patch.set_facecolor('#F8FAFC')
save('itc_chart.png')

print('\nAll 8 charts saved to assets/')
