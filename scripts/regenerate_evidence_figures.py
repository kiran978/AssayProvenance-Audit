#!/usr/bin/env python3
"""Create evidence-derived manuscript figure alternatives from deposited CSVs.
Requires matplotlib, numpy (see requirements-figures.txt).
These are reproducible analytical plots, not identical to any original editorial artwork.
"""
import csv, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"figures"/"reproducible"
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150,"savefig.dpi":300})
NAVY="#162d4d"; TEAL="#268e98"; SLATE="#798b9e"; AMBER="#c68a43"; RED="#ad5565"
def rows(p):
 with open(ROOT/p,encoding="utf-8-sig",newline="") as fh:return list(csv.DictReader(fh))
def save(fig,name):
 fig.tight_layout(pad=1.6)
 for ext in ("png","svg"):
  fig.savefig(OUT/(name+"."+ext),dpi=300,bbox_inches="tight",facecolor="white")
 plt.close(fig)
 print("CREATED",name)

# Figure 1: conceptual diagram — no implied truth assignments
fig,ax=plt.subplots(figsize=(11,6.2));ax.set(xlim=(0,10),ylim=(0,7));ax.axis("off")
def node(x,y,w,h,text,fc="#edf4f8",ec="#42799d",fs=10):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.08,rounding_size=0.14",
    linewidth=1.2,edgecolor=ec,facecolor=fc))
 ax.text(x+w/2,y+h/2,text,va="center",ha="center",fontsize=fs,weight="semibold")
def arrow(x1,y1,x2,y2):
 ax.annotate("",xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle="-|>",lw=1.4,color=SLATE))
node(3.1,5.9,3.8,.75,"Shared compounds / assay records")
node(.7,4.45,3.35,.8,"Endpoint/estimand compatibility")
node(5.95,4.45,3.35,.8,"Document and program lineage")
node(3.25,2.9,3.55,.8,"Raw measurement and run evidence")
node(.2,1.0,2.75,.75,"Independent source supported","#e9f5ef","#34836d",9)
node(3.55,1.0,2.9,.75,"Program-disjoint benchmark excluded","#fff0ef","#b04a4f",9)
node(7,1.0,2.8,.75,"Insufficient data: HOLD","#eff2f5","#677786",9)
arrow(5,5.9,2.5,5.28);arrow(5,5.9,7.5,5.28);arrow(2.45,4.45,4.2,3.72);arrow(7.5,4.45,5.8,3.72)
arrow(5,2.9,1.55,1.84);arrow(5,2.9,5,1.84);arrow(5,2.9,8.4,1.84)
ax.text(5,.2,"Shared program ≠ proven identical laboratory runs. Missing independence evidence ≠ proven dependence.",ha="center",fontsize=9,color=SLATE)
ax.set_title("Figure 1  |  Provenance dimensions and decision boundaries",fontsize=15,weight="bold",pad=20)
save(fig,"fig1_provenance_decision_framework")

a=rows("data/chembl/strict_s0_ge20_atlas_304.csv")
c=rows("data/chembl/cross_document_64_triage.csv")
m=rows("data/chembl/pre_manual_candidates_36.csv")
p=rows("data/pubchem/stage5e_43pair_provisional_scientific_decision_dimensions.csv")
sid=rows("data/pubchem/stage6c_kcnk9_sid88_concordance.csv")
d=rows("data/pubchem/stage6c_kcnk9_1760_dose_sd_comparisons.csv")
frozen=rows("data/pubchem/stage6c_six_pair_frozen_vs_current_overlap.csv")

# Figure 2: source-pair funnel with flags, not verified duplicated raw data
fig,ax=plt.subplots(figsize=(9.8,4.7))
names=["GE20 overlap (102 targets)","Same document ID","Different document IDs","Bibliographic review flags","Pre-manual candidates (22 targets)"]
counts=[len(a),sum(x["same_document"]=="1" for x in a),len(c),sum(x["bibliographic_duplicate_review"]=="1" for x in c),len(m)]
ax.barh(names[::-1],counts[::-1],color=[TEAL,AMBER,NAVY,SLATE,NAVY][::-1])
for i,v in enumerate(counts[::-1]):ax.text(v+4,i,str(v),va="center")
ax.set(xlabel="Distinct selected assay pairs",xlim=(0,350),title="Figure 2  |  ChEMBL source-document triage")
ax.text(.01,-.25,"28 records flagged for bibliographic review; not confirmed reused measurements.",transform=ax.transAxes,fontsize=8,color=SLATE)
save(fig,"fig2_chembl_document_attrition")

# Figure 3: conditional GE20+ threshold refilter
levels=[20,25,30,40,50,100,200]
counts=[];crosses=[];manual=[]
for n in levels:
 counts.append(sum(int(x["n_shared"])>=n for x in a))
 crosses.append(sum(int(x["n_shared"])>=n for x in c))
 manual.append(sum(int(x["n_shared"])>=n for x in m))
fig,ax=plt.subplots(figsize=(9,5.2))
for line,col,label in [(counts,NAVY,"All numerical-overlap pairs"),(crosses,TEAL,"Different-document pairs"),(manual,AMBER,"Pre-manual candidates")]:
 ax.plot(levels,line,"o-",lw=2.1,color=col,label=label)
ax.set(xlabel="Minimum shared parent compounds",ylabel="Pairs remaining",title="Figure 3  |  ChEMBL source-overlap threshold sensitivity",xlim=(17,205),ylim=(-4,320))
ax.grid(alpha=.16);ax.legend(frameon=False)
ax.text(.02,-.23,"GE20+ re-filter of the recovered 304-pair atlas; GE10 source records were unavailable.",transform=ax.transAxes,fontsize=8,color=SLATE)
save(fig,"fig3_chembl_overlap_thresholds")

# Figure 4: orthogonal categorical axes
endpoint=["COMPATIBLE","SENSITIVITY_ONLY","INCOMPATIBLE_FOR_INTENDED_ESTIMAND"]
epcounts=[sum(x["Frozen_endpoint_compatibility"]==n for x in p) for n in endpoint]
prog=["SHARED_PROGRAM","UNRESOLVED"]
prcounts=[sum(x["ReviewerA_discovery_program"]==n for x in p) for n in prog]
fig,axes=plt.subplots(1,2,figsize=(10,5))
axes[0].bar(["Compatible","Sensitivity-only","Incompatible"],epcounts,color=[TEAL,AMBER,RED])
axes[1].bar(["Shared program","Unresolved program"],prcounts,color=[NAVY,SLATE])
for ax,vals in zip(axes,[epcounts,prcounts]):
 for i,v in enumerate(vals):ax.text(i,v+.5,str(v),ha="center")
 ax.set(ylabel="Number of selected assay pairs",ylim=(0,46))
axes[0].set_title("Frozen endpoint suitability");axes[1].set_title("Provisional program-lineage review")
fig.suptitle("Figure 4  |  Program links and endpoint compatibility are different dimensions")
save(fig,"fig4_pubchem_distinct_categories")

# Figure 5: 10 dose ratios per matched SID
near={x["SID"]:x["ALL20_Dose_and_SD_near_match"]=="YES" for x in sid}
xy={True:([],[]),False:([],[])}
for x in d:
 if not x["field"].startswith("Ratio at"):continue
 try:u=float(x["AID_540322"]);v=float(x["AID_652211"])
 except:continue
 group=xy[near[x["SID"]]]
 group[0].append(u);group[1].append(v)
fig,ax=plt.subplots(figsize=(7,6.6))
for flag,col,label in [(True,TEAL,"84 near-matching SID profiles"),(False,RED,"4 divergent SID profiles")]:
 xx,yy=xy[flag];ax.scatter(xx,yy,c=col,s=18 if flag else 25,alpha=.7,label=label)
ax.plot([0,1.2],[0,1.2],"--",lw=1,color=SLATE)
ax.set(xlabel="AID 540322: deposited dose ratio",ylabel="AID 652211: deposited dose ratio",xlim=(0,1.2),ylim=(0,1.2),title="Figure 5  |  KCNK9 same-substance response concordance")
ax.legend(frameon=False)
save(fig,"fig5_kcnk9_paired_dose_ratios")

# Figure 6: exact cell-level difference heatmap
ids=[x["SID"] for x in sid if x["ALL20_Dose_and_SD_near_match"]=="YES"] + [x["SID"] for x in sid if x["ALL20_Dose_and_SD_near_match"]!="YES"]
fields=list(dict.fromkeys(x["field"] for x in d))
v={(x["SID"],x["field"]):float(x["abs_difference"]) if x["abs_difference"] else np.nan for x in d}
data=np.array([[math.log10(v[(s,f)]+1e-6) if (s,f) in v and np.isfinite(v[(s,f)]) else np.nan for f in fields] for s in ids])
fig,ax=plt.subplots(figsize=(10,6.5))
im=ax.imshow(data,aspect="auto",cmap="viridis",vmin=-6,vmax=0)
fig.colorbar(im,ax=ax,label="log10(|deposited value difference| + 10⁻⁶)")
ax.set(xlabel="Twenty matched ratio/SD fields",ylabel="Shared SIDs; four divergent profiles at bottom",title="Figure 6  |  KCNK9 field-level source differences")
ax.axhline(83.5,ls="--",lw=1.2,color=RED)
save(fig,"fig6_kcnk9_88sid_20field_heatmap")

# Figure 7: previous frozen selection vs newly retrieved concise activity records
labels=[f'{x["AID_A"]}/{x["AID_B"]}' for x in frozen]
historic=[int(x["Frozen_shared_CIDs"]) for x in frozen]
current=[int(x["Current_shared_CIDs"]) for x in frozen]
x=np.arange(len(labels));w=.38
fig,ax=plt.subplots(figsize=(11,5.4))
ax.bar(x-w/2,historic,w,color=NAVY,label="Frozen selected CIDs")
ax.bar(x+w/2,current,w,color=AMBER,label="Later complete concise CIDs")
ax.set(yscale="symlog",ylabel="Shared CIDs (symmetric-log)",xticks=x,xticklabels=labels,title="Figure 7  |  Frozen source selection vs later PubChem intersection")
ax.tick_params(axis="x",labelrotation=25)
ax.legend(frameon=False)
save(fig,"fig7_pubchem_old_vs_current_cid")

# Figure 8: declared rule sensitivity, counterfactual bars visually identified
scenarios=["Original reviewer\ngate","Mechanical\nprogram rule","Optimistic\nprogram only","All runs distinct:\ncompatible","All runs distinct:\ncompat + sensitivity","All runs distinct:\nreviewer compatible","All runs distinct:\nreviewer broader"]
vals=[0,0,2,23,33,18,31]
colors=[NAVY,NAVY,AMBER,RED,RED,RED,RED]
fig,ax=plt.subplots(figsize=(11,5.9))
ax.bar(range(len(vals)),vals,color=colors)
ax.set(xticks=range(len(vals)),xticklabels=scenarios,ylabel="Hypothetical candidate pairs",
 title="Figure 8  |  Operational rule sensitivity — NOT confirmed independent assays",ylim=(0,38))
ax.tick_params(axis="x",labelsize=8)
for i,num in enumerate(vals):ax.text(i,num+.5,str(num),ha="center",fontsize=9)
ax.text(.01,-.31,"Last four scenarios counterfactually assume all experimental runs are distinct; not empirically demonstrated.",transform=ax.transAxes,fontsize=8,color=RED)
save(fig,"fig8_independence_rule_counterfactuals")
