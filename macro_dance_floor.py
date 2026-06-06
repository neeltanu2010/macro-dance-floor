
# ============================================================
# 🪩 Macro Dance Floor — Direct Theoretical Analyzer
# Select sector + select macro/macro combo + click Analyze.
# No historical data. No CSV. Pure theoretical concept engine.
# ============================================================

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Macro Dance Floor",
    page_icon="🪩",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(255, 230, 109, 0.48), transparent 30%),
            radial-gradient(circle at top right, rgba(255, 112, 179, 0.25), transparent 28%),
            radial-gradient(circle at bottom left, rgba(90, 210, 255, 0.24), transparent 30%),
            linear-gradient(135deg, #fffdf5 0%, #f7fbff 46%, #fff4fb 100%);
    }
    .main-title {
        font-size: 52px;
        font-weight: 950;
        text-align: center;
        color: #241044;
        letter-spacing: -1.2px;
        padding-top: 16px;
    }
    .sub-title {
        font-size: 18px;
        text-align: center;
        color: #5b4b73;
        margin-bottom: 20px;
    }
    .hero {
        background: linear-gradient(135deg, rgba(255,255,255,.97), rgba(255,244,193,.95) 42%, rgba(231,242,255,.97));
        border: 1px solid rgba(74, 45, 130, .12);
        box-shadow: 0 20px 55px rgba(43, 21, 90, .13);
        border-radius: 32px;
        padding: 30px;
        margin-bottom: 18px;
    }
    .hero-label {
        display:inline-block;
        padding: 7px 13px;
        border-radius: 999px;
        background: linear-gradient(90deg, #ffe66d, #ff9fd7);
        color:#321744;
        font-size:13px;
        font-weight:900;
        margin-bottom: 10px;
    }
    .hero-head {
        font-size: 34px;
        font-weight: 950;
        line-height:1.12;
        color:#241044;
        margin-bottom: 10px;
    }
    .hero-text {
        color:#524366;
        font-size:16px;
        line-height:1.65;
    }
    .chip {
        display:inline-block;
        margin: 5px 5px 0 0;
        padding: 8px 12px;
        border-radius: 999px;
        background: rgba(255,255,255,.84);
        border: 1px solid rgba(70,45,120,.10);
        color:#3a2a58;
        font-weight:800;
        font-size:13px;
    }
    .card {
        background: rgba(255,255,255,.90);
        border: 1px solid rgba(70,45,120,.10);
        box-shadow: 0 14px 34px rgba(42, 23, 90, .08);
        border-radius: 26px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .gold-card {
        background: linear-gradient(135deg, rgba(255,255,255,.97), rgba(255,245,198,.95));
        border: 1px solid rgba(180,120,0,.15);
        box-shadow: 0 14px 34px rgba(100,70,0,.09);
        border-radius: 26px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .blue-card {
        background: linear-gradient(135deg, rgba(255,255,255,.97), rgba(223,244,255,.96));
        border: 1px solid rgba(20,110,180,.13);
        box-shadow: 0 14px 34px rgba(20,90,150,.08);
        border-radius: 26px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .pink-card {
        background: linear-gradient(135deg, rgba(255,255,255,.97), rgba(255,229,241,.96));
        border: 1px solid rgba(170,0,90,.13);
        box-shadow: 0 14px 34px rgba(150,0,80,.08);
        border-radius: 26px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .green-card {
        background: linear-gradient(135deg, rgba(255,255,255,.97), rgba(226,255,231,.96));
        border: 1px solid rgba(20,130,70,.13);
        box-shadow: 0 14px 34px rgba(20,130,70,.08);
        border-radius: 26px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .dialog {
        border-radius: 19px;
        padding: 14px 16px;
        margin: 9px 0 14px 0;
        box-shadow: 0 8px 22px rgba(0,0,0,.06);
        border: 1px solid rgba(0,0,0,.08);
    }
    .dialog-title {
        font-weight: 950;
        font-size: 17px;
        color:#241044;
        margin-bottom: 6px;
    }
    .dialog-text {
        color:#463a5c;
        font-size: 14px;
        line-height: 1.55;
    }
    .d-blue {background: linear-gradient(135deg,#ffffff,#dff4ff);}
    .d-green {background: linear-gradient(135deg,#ffffff,#e5ffe9);}
    .d-yellow {background: linear-gradient(135deg,#ffffff,#fff5c8);}
    .d-pink {background: linear-gradient(135deg,#ffffff,#ffe5f1);}
    .d-purple {background: linear-gradient(135deg,#ffffff,#eee6ff);}
    .ribbon {
        display:inline-block;
        padding: 7px 12px;
        border-radius: 999px;
        background: linear-gradient(90deg, #2b155a, #6d3fd6);
        color: white;
        font-size: 13px;
        font-weight: 900;
        margin-bottom: 8px;
    }
    div[data-testid="stMetricValue"] {
        color:#241044;
        font-weight: 950;
    }
    .stButton > button {
        border-radius: 18px;
        min-height: 3.4rem;
        font-weight: 900;
        font-size: 18px;
        letter-spacing: .2px;
        box-shadow: 0 14px 28px rgba(43,21,90,.18);
        padding-top: .6rem;
        padding-bottom: .6rem;
    }
    .block-label {
        display:inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        background: linear-gradient(90deg, #2b155a 0%, #6d3fd6 100%);
        color: white;
        font-weight: 900;
        font-size: 13px;
        margin-bottom: 10px;
    }
    .mega-card {
        background: linear-gradient(135deg, rgba(255,255,255,.98), rgba(253,248,225,.97) 35%, rgba(238,247,255,.98) 100%);
        border-radius: 30px;
        padding: 28px;
        border: 1px solid rgba(74,45,130,.12);
        box-shadow: 0 20px 50px rgba(43,21,90,.10);
        margin-bottom: 24px;
    }
    .step-card {
        background: rgba(255,255,255,.92);
        border-radius: 24px;
        padding: 22px;
        border: 1px solid rgba(74,45,130,.10);
        box-shadow: 0 12px 28px rgba(43,21,90,.07);
        min-height: 170px;
        margin-bottom: 10px;
    }
    .step-no {
        font-size: 26px;
        font-weight: 950;
        color: #6d3fd6;
        margin-bottom: 8px;
    }
    .step-head {
        font-size: 20px;
        font-weight: 900;
        color: #241044;
        margin-bottom: 8px;
    }
    .step-text {
        font-size: 14px;
        line-height: 1.7;
        color: #57486a;
    }
    .lux-note {
        background: linear-gradient(135deg, rgba(255,255,255,.96), rgba(255,229,241,.96));
        border-radius: 22px;
        padding: 18px;
        border: 1px solid rgba(170,0,90,.12);
        margin-top: 8px;
        margin-bottom: 8px;
    }
    .lux-note h4 {
        margin: 0 0 8px 0;
        color: #241044;
    }
    div[data-testid="stDataFrame"] {
        padding-top: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def dialog(title, text, tone="blue"):
    st.markdown(
        f"""
        <div class="dialog d-{tone}">
            <div class="dialog-title">{title}</div>
            <div class="dialog-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def card_start(kind="card"):
    st.markdown(f'<div class="{kind}">', unsafe_allow_html=True)

def card_end():
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# Macro library
# ----------------------------
MACROS = {
    "RBI Repo Rate / Interest Rates": {
        "family": "Rates",
        "when_rises": "Borrowing becomes costlier. Rate-sensitive sectors usually face pressure.",
        "when_falls": "Borrowing becomes cheaper. Banks may see margin pressure, but autos, realty and consumption may benefit.",
        "independence_note": "Often linked with inflation and bond yields, so avoid combining all three blindly.",
    },
    "Bond Yields": {
        "family": "Rates",
        "when_rises": "Equity valuations usually compress. Banks may benefit initially, but long-duration growth sectors can suffer.",
        "when_falls": "Valuations get support, especially growth and real-estate-linked sectors.",
        "independence_note": "Interlinked with repo rate, inflation and fiscal deficit.",
    },
    "Inflation": {
        "family": "Inflation",
        "when_rises": "Input costs rise and consumers may reduce spending. Pricing-power sectors handle it better.",
        "when_falls": "Margins and consumption may improve, but very low inflation can also signal weak demand.",
        "independence_note": "Linked with crude, food prices, currency and rates.",
    },
    "Crude Oil Prices": {
        "family": "Commodities",
        "when_rises": "Hurts oil importers, aviation, paints, tyres and consumers. Helps upstream energy producers.",
        "when_falls": "Benefits import-heavy sectors and reduces inflation pressure.",
        "independence_note": "Linked with inflation, CAD and rupee.",
    },
    "Commodity Prices": {
        "family": "Commodities",
        "when_rises": "Helps commodity producers like metals but hurts input-cost-heavy sectors.",
        "when_falls": "Hurts producers but benefits consumers of raw materials.",
        "independence_note": "Linked with global growth and currency.",
    },
    "USD/INR / Currency": {
        "family": "Currency",
        "when_rises": "Rupee weakens. Exporters benefit; importers and foreign-debt-heavy companies suffer.",
        "when_falls": "Rupee strengthens. Importers benefit; exporters may face margin pressure.",
        "independence_note": "Linked with dollar index, CAD, FII flows and crude.",
    },
    "US Dollar Index": {
        "family": "Currency",
        "when_rises": "Emerging market flows usually face pressure. Rupee can weaken.",
        "when_falls": "Emerging markets may attract flows and risk appetite improves.",
        "independence_note": "Highly linked with USD/INR and FII flows.",
    },
    "FII Inflows / Outflows": {
        "family": "Flows",
        "when_rises": "Liquidity improves, large caps and financials usually benefit.",
        "when_falls": "Markets may face selling pressure, especially large liquid sectors.",
        "independence_note": "Linked with global risk appetite, dollar strength and yields.",
    },
    "Liquidity": {
        "family": "Liquidity",
        "when_rises": "More money in the system supports valuations, credit growth and risk assets.",
        "when_falls": "Market valuations and credit-sensitive sectors may face pressure.",
        "independence_note": "Linked with central bank policy and credit growth.",
    },
    "Bank Credit Growth": {
        "family": "Credit",
        "when_rises": "Healthy lending cycle. Banks, NBFCs, autos, realty and consumption benefit.",
        "when_falls": "Credit demand weakens. Cyclical sectors may slow.",
        "independence_note": "Linked with GDP, employment and liquidity.",
    },
    "NPAs / Banking Stress": {
        "family": "Credit",
        "when_rises": "Banks, NBFCs and lenders face pressure. Credit cycle weakens.",
        "when_falls": "Lender profitability and risk appetite improve.",
        "independence_note": "Linked with credit growth and economic slowdown.",
    },
    "Indian GDP Growth": {
        "family": "Growth",
        "when_rises": "Cyclicals, banks, industrials, autos and consumption usually benefit.",
        "when_falls": "Defensives like FMCG, pharma and utilities may outperform relatively.",
        "independence_note": "Linked with employment, credit growth and demand.",
    },
    "Corporate Earnings Growth": {
        "family": "Growth",
        "when_rises": "Supports broad market and sector valuations.",
        "when_falls": "Valuation risk rises even if macro looks stable.",
        "independence_note": "Linked with GDP, demand and margins.",
    },
    "Employment / Wage Growth": {
        "family": "Demand",
        "when_rises": "Consumption, housing, autos, retail and lending demand improve.",
        "when_falls": "Discretionary consumption and credit demand weaken.",
        "independence_note": "Linked with GDP and consumer demand.",
    },
    "Consumer Demand": {
        "family": "Demand",
        "when_rises": "FMCG, autos, retail, hotels, media and consumer durables benefit.",
        "when_falls": "Consumption-facing sectors face pressure.",
        "independence_note": "Linked with employment, inflation and credit.",
    },
    "GST Collections": {
        "family": "Demand",
        "when_rises": "Signals formal economic activity and consumption strength.",
        "when_falls": "May signal weaker demand or slower formal activity.",
        "independence_note": "Linked with GDP and consumer demand.",
    },
    "Government Spending": {
        "family": "Fiscal",
        "when_rises": "Infrastructure, defence, railways, capital goods, cement and construction benefit.",
        "when_falls": "Order-flow-driven sectors may slow.",
        "independence_note": "Linked with fiscal deficit.",
    },
    "Fiscal Deficit": {
        "family": "Fiscal",
        "when_rises": "Can push yields higher; may help spending-driven sectors but hurt macro stability.",
        "when_falls": "Improves macro stability but may reduce fiscal impulse if spending slows.",
        "independence_note": "Linked with government spending and bond yields.",
    },
    "Current Account Deficit": {
        "family": "External",
        "when_rises": "Rupee pressure rises; import-heavy sectors suffer.",
        "when_falls": "External stability improves and currency risk reduces.",
        "independence_note": "Linked with crude, currency and trade balance.",
    },
    "Global Markets": {
        "family": "Global Risk",
        "when_rises": "Risk appetite improves; IT, metals, financials and high-beta sectors benefit.",
        "when_falls": "Risk-off selling may hit cyclicals and high-beta sectors.",
        "independence_note": "Linked with FII flows and global risk appetite.",
    },
    "Global Risk Appetite / VIX": {
        "family": "Global Risk",
        "when_rises": "High fear hurts equities, especially cyclicals and high valuation sectors.",
        "when_falls": "Risk assets get support.",
        "independence_note": "Linked with FII flows, dollar and global markets.",
    },
    "Global Trade Cycle": {
        "family": "Global Growth",
        "when_rises": "Exporters, metals, chemicals, logistics and ports benefit.",
        "when_falls": "Export-linked sectors face pressure.",
        "independence_note": "Linked with global GDP and commodity prices.",
    },
    "Monsoon / Rural Economy": {
        "family": "Weather/Rural",
        "when_rises": "Good monsoon helps rural income, FMCG, tractors, two-wheelers and agrochemicals.",
        "when_falls": "Rural demand weakens and food inflation risk rises.",
        "independence_note": "Can link with inflation and rural demand.",
    },
    "Real Estate Cycle": {
        "family": "Asset Cycle",
        "when_rises": "Realty, cement, paints, wires, tiles, banks and NBFCs benefit.",
        "when_falls": "Housing-linked sectors slow.",
        "independence_note": "Linked with rates, credit and income.",
    },
    "Valuation Level": {
        "family": "Valuation",
        "when_rises": "Future return risk rises; expensive sectors become vulnerable.",
        "when_falls": "Long-term return potential improves if fundamentals stay intact.",
        "independence_note": "Linked with sentiment and rates.",
    },
    "Market Sentiment": {
        "family": "Sentiment",
        "when_rises": "High-beta, IPO, mid/small cap and discretionary sectors benefit.",
        "when_falls": "Defensive sectors may outperform.",
        "independence_note": "Linked with liquidity and flows.",
    },
    "Election / Policy Stability": {
        "family": "Policy",
        "when_rises": "Stable policy supports infrastructure, PSU, defence, banks and capex sectors.",
        "when_falls": "Policy uncertainty hurts investment-heavy sectors.",
        "independence_note": "Separate from tax policy but can affect the same sectors.",
    },
    "Regulatory Risk": {
        "family": "Policy",
        "when_rises": "Regulated sectors like telecom, pharma, banks, insurance, power and utilities face risk.",
        "when_falls": "Policy clarity supports valuation.",
        "independence_note": "Sector-specific; not always broad macro.",
    },
    "Technological Disruption": {
        "family": "Disruption",
        "when_rises": "Winners benefit, old models suffer. IT, EV, fintech and automation themes gain.",
        "when_falls": "Legacy businesses face less disruption risk.",
        "independence_note": "Independent from rates but valuation can amplify it.",
    },
    "Geopolitical Events": {
        "family": "Shock",
        "when_rises": "Oil, defence, gold and risk-off assets may benefit; global cyclicals may suffer.",
        "when_falls": "Risk appetite normalises.",
        "independence_note": "Can trigger crude, currency and FII effects together.",
    },
    "Black Swan Events": {
        "family": "Shock",
        "when_rises": "Liquidity dries, risk assets fall, defensives outperform relatively.",
        "when_falls": "Recovery trade begins as uncertainty fades.",
        "independence_note": "Rare, nonlinear and not easily modelled.",
    },
    "LTCG Tax": {
        "family": "Tax",
        "when_rises": "Long-term investor sentiment can weaken, especially in high-valuation equities.",
        "when_falls": "Equity attractiveness improves.",
        "independence_note": "Linked with broader tax policy and sentiment.",
    },
    "STCG Tax": {
        "family": "Tax",
        "when_rises": "Short-term trading appetite may reduce.",
        "when_falls": "Trading activity may improve.",
        "independence_note": "Linked with market volumes and sentiment.",
    },
    "GST / Indirect Tax": {
        "family": "Tax",
        "when_rises": "Can hurt consumption if passed to consumers; organised players may benefit from compliance.",
        "when_falls": "Demand may improve in taxed categories.",
        "independence_note": "Linked with consumer demand and pricing.",
    },
    "Corporate Tax": {
        "family": "Tax",
        "when_rises": "Post-tax earnings reduce across corporate sectors.",
        "when_falls": "Corporate profits and cash flows improve.",
        "independence_note": "Broad earnings macro.",
    },
    "STT": {
        "family": "Tax",
        "when_rises": "Trading volumes and short-term activity may reduce.",
        "when_falls": "Market participation may improve.",
        "independence_note": "Linked with trading sentiment.",
    },
    "Tariffs & Import Duties": {
        "family": "Trade Policy",
        "when_rises": "Domestic protected sectors may benefit; import-dependent sectors suffer.",
        "when_falls": "Importers benefit; protected domestic players may face competition.",
        "independence_note": "Linked with inflation and trade policy.",
    },
}


# ----------------------------
# Sector theoretical model
# score: +3 strong positive, -3 strong negative
# Direction means when macro rises / improves as defined.
# ----------------------------
SECTORS = {
    "Auto": {
        "theme": "Rate-sensitive + consumption + commodity-cost sector",
        "macros": {
            "RBI Repo Rate / Interest Rates": -3, "Bank Credit Growth": 3, "Employment / Wage Growth": 3,
            "Consumer Demand": 3, "Inflation": -2, "Crude Oil Prices": -2, "Commodity Prices": -2,
            "Monsoon / Rural Economy": 2, "GST / Indirect Tax": -2, "Real Estate Cycle": 1
        },
        "combo": ["RBI Repo Rate / Interest Rates", "Bank Credit Growth", "Consumer Demand"],
        "why": "Autos are funded by EMIs. Cheaper loans, strong income and strong demand help; high fuel/input costs hurt.",
    },
    "Banks": {
        "theme": "Credit cycle + rates + asset quality",
        "macros": {
            "Bank Credit Growth": 3, "NPAs / Banking Stress": -3, "RBI Repo Rate / Interest Rates": 1,
            "Bond Yields": -2, "Liquidity": 2, "Indian GDP Growth": 2, "FII Inflows / Outflows": 2,
            "Fiscal Deficit": -1, "Regulatory Risk": -2
        },
        "combo": ["Bank Credit Growth", "NPAs / Banking Stress", "Liquidity"],
        "why": "Banks do well when loans grow and asset quality is stable. Liquidity and rates shape margins and credit appetite.",
    },
    "NBFCs": {
        "theme": "Credit availability + borrowing cost",
        "macros": {
            "RBI Repo Rate / Interest Rates": -3, "Liquidity": 3, "Bank Credit Growth": 2,
            "Consumer Demand": 2, "NPAs / Banking Stress": -3, "Bond Yields": -2,
            "Regulatory Risk": -2, "Employment / Wage Growth": 2
        },
        "combo": ["Liquidity", "RBI Repo Rate / Interest Rates", "NPAs / Banking Stress"],
        "why": "NBFCs borrow and lend. Their dance depends on liquidity, cost of funds and borrower health.",
    },
    "Financial Services": {
        "theme": "Market activity + credit + flows",
        "macros": {
            "FII Inflows / Outflows": 3, "Market Sentiment": 3, "Liquidity": 3, "STT": -2,
            "STCG Tax": -2, "LTCG Tax": -1, "RBI Repo Rate / Interest Rates": -1,
            "Regulatory Risk": -2, "Valuation Level": -1
        },
        "combo": ["FII Inflows / Outflows", "Liquidity", "Market Sentiment"],
        "why": "Brokers, AMCs, exchanges and financial platforms depend on activity, flows and participation.",
    },
    "Insurance": {
        "theme": "Rates + regulation + financial savings",
        "macros": {
            "Bond Yields": 2, "Employment / Wage Growth": 2, "Consumer Demand": 1,
            "Regulatory Risk": -3, "RBI Repo Rate / Interest Rates": 1, "Market Sentiment": 1,
            "Corporate Tax": -1
        },
        "combo": ["Bond Yields", "Employment / Wage Growth", "Regulatory Risk"],
        "why": "Insurance benefits from financialisation and long-term savings, but regulation can sharply affect products and margins.",
    },
    "IT Services": {
        "theme": "Export + global tech spending + currency",
        "macros": {
            "USD/INR / Currency": 3, "Global Markets": 2, "Global Trade Cycle": 2, "US Dollar Index": 1,
            "Global Risk Appetite / VIX": -2, "Technological Disruption": 2, "Indian GDP Growth": 0,
            "Corporate Tax": -1
        },
        "combo": ["USD/INR / Currency", "Global Markets", "Global Risk Appetite / VIX"],
        "why": "IT earns largely in foreign currency. Global tech budgets, US sentiment and rupee movement matter more than local GDP.",
    },
    "Pharma": {
        "theme": "Defensive export + regulation",
        "macros": {
            "USD/INR / Currency": 2, "Global Risk Appetite / VIX": 1, "Regulatory Risk": -3,
            "Global Trade Cycle": 1, "Indian GDP Growth": 0, "Inflation": -1, "Corporate Tax": -1
        },
        "combo": ["USD/INR / Currency", "Regulatory Risk", "Global Risk Appetite / VIX"],
        "why": "Pharma is defensive and export-linked, but regulatory events and pricing pressure matter heavily.",
    },
    "Healthcare / Hospitals": {
        "theme": "Domestic healthcare demand + regulation",
        "macros": {
            "Employment / Wage Growth": 2, "Consumer Demand": 1, "Inflation": -1,
            "Regulatory Risk": -3, "Indian GDP Growth": 1, "RBI Repo Rate / Interest Rates": -1
        },
        "combo": ["Employment / Wage Growth", "Regulatory Risk", "Inflation"],
        "why": "Healthcare demand is resilient, but price controls and regulation can affect margins.",
    },
    "FMCG": {
        "theme": "Consumption + rural + inflation",
        "macros": {
            "Consumer Demand": 3, "Employment / Wage Growth": 2, "Monsoon / Rural Economy": 3,
            "Inflation": -2, "Commodity Prices": -2, "GST / Indirect Tax": -1,
            "Indian GDP Growth": 1, "Market Sentiment": 1
        },
        "combo": ["Consumer Demand", "Monsoon / Rural Economy", "Inflation"],
        "why": "FMCG needs volume growth. Rural demand helps; high input inflation hurts unless pricing power is strong.",
    },
    "Consumer Durables": {
        "theme": "Discretionary consumption + credit",
        "macros": {
            "Consumer Demand": 3, "Bank Credit Growth": 2, "RBI Repo Rate / Interest Rates": -2,
            "Employment / Wage Growth": 3, "Inflation": -2, "Commodity Prices": -2,
            "GST / Indirect Tax": -2
        },
        "combo": ["Consumer Demand", "Employment / Wage Growth", "RBI Repo Rate / Interest Rates"],
        "why": "Durables are discretionary and often financed. Income, confidence and rates matter.",
    },
    "Retail": {
        "theme": "Urban consumption + employment",
        "macros": {
            "Consumer Demand": 3, "Employment / Wage Growth": 3, "Inflation": -2,
            "GST Collections": 2, "Market Sentiment": 1, "RBI Repo Rate / Interest Rates": -1
        },
        "combo": ["Consumer Demand", "Employment / Wage Growth", "Inflation"],
        "why": "Retail thrives when wallets are healthy and inflation is not eating discretionary spending.",
    },
    "Media / Entertainment": {
        "theme": "Advertising + discretionary spend",
        "macros": {
            "Consumer Demand": 3, "Indian GDP Growth": 2, "Market Sentiment": 2,
            "Corporate Earnings Growth": 2, "Employment / Wage Growth": 2, "Regulatory Risk": -1
        },
        "combo": ["Consumer Demand", "Indian GDP Growth", "Market Sentiment"],
        "why": "Advertising and entertainment spend rise when companies and consumers feel confident.",
    },
    "Hotels / Tourism": {
        "theme": "Discretionary travel + income",
        "macros": {
            "Consumer Demand": 3, "Employment / Wage Growth": 3, "Crude Oil Prices": -1,
            "Global Risk Appetite / VIX": -2, "Black Swan Events": -3, "Indian GDP Growth": 2
        },
        "combo": ["Consumer Demand", "Employment / Wage Growth", "Global Risk Appetite / VIX"],
        "why": "Travel is discretionary. It benefits from income and confidence but suffers in shocks.",
    },
    "Realty": {
        "theme": "Rates + liquidity + housing cycle",
        "macros": {
            "RBI Repo Rate / Interest Rates": -3, "Liquidity": 3, "Bank Credit Growth": 3,
            "Employment / Wage Growth": 2, "Real Estate Cycle": 3, "Bond Yields": -2,
            "Government Spending": 1
        },
        "combo": ["RBI Repo Rate / Interest Rates", "Liquidity", "Bank Credit Growth"],
        "why": "Real estate is highly rate-sensitive. Liquidity, credit and income drive affordability.",
    },
    "Cement": {
        "theme": "Construction + infra + real estate",
        "macros": {
            "Government Spending": 3, "Real Estate Cycle": 3, "RBI Repo Rate / Interest Rates": -1,
            "Commodity Prices": -2, "Crude Oil Prices": -1, "Indian GDP Growth": 2,
            "Fiscal Deficit": 1
        },
        "combo": ["Government Spending", "Real Estate Cycle", "Commodity Prices"],
        "why": "Cement demand follows housing and infrastructure. Fuel and raw material costs affect margins.",
    },
    "Infrastructure": {
        "theme": "Government capex + rates",
        "macros": {
            "Government Spending": 3, "Fiscal Deficit": 1, "RBI Repo Rate / Interest Rates": -2,
            "Bond Yields": -2, "Indian GDP Growth": 2, "Election / Policy Stability": 3,
            "Liquidity": 2
        },
        "combo": ["Government Spending", "Election / Policy Stability", "RBI Repo Rate / Interest Rates"],
        "why": "Infra depends on order flow, policy continuity and funding cost.",
    },
    "Capital Goods": {
        "theme": "Capex cycle + industrial growth",
        "macros": {
            "Government Spending": 3, "Indian GDP Growth": 3, "Corporate Earnings Growth": 2,
            "RBI Repo Rate / Interest Rates": -1, "Global Trade Cycle": 2,
            "Commodity Prices": -1, "Election / Policy Stability": 2
        },
        "combo": ["Government Spending", "Indian GDP Growth", "Corporate Earnings Growth"],
        "why": "Capital goods benefit when public and private capex cycles are strong.",
    },
    "Defence": {
        "theme": "Government spending + geopolitics",
        "macros": {
            "Government Spending": 3, "Geopolitical Events": 3, "Election / Policy Stability": 2,
            "Fiscal Deficit": 1, "Regulatory Risk": -1, "USD/INR / Currency": -1
        },
        "combo": ["Government Spending", "Geopolitical Events", "Election / Policy Stability"],
        "why": "Defence depends on government orders, geopolitical urgency and policy continuity.",
    },
    "Railways": {
        "theme": "Public capex + policy",
        "macros": {
            "Government Spending": 3, "Election / Policy Stability": 3, "Fiscal Deficit": 1,
            "Commodity Prices": -1, "Indian GDP Growth": 2
        },
        "combo": ["Government Spending", "Election / Policy Stability", "Indian GDP Growth"],
        "why": "Railway-linked businesses are order-flow and policy-capex driven.",
    },
    "Metals": {
        "theme": "Global cycle + commodities + dollar",
        "macros": {
            "Commodity Prices": 3, "Global Trade Cycle": 3, "Indian GDP Growth": 2,
            "US Dollar Index": -2, "USD/INR / Currency": 1, "Tariffs & Import Duties": 2,
            "Global Risk Appetite / VIX": -2
        },
        "combo": ["Commodity Prices", "Global Trade Cycle", "US Dollar Index"],
        "why": "Metals are global cyclicals. Prices, China/global demand and dollar direction dominate.",
    },
    "Chemicals": {
        "theme": "Export + input cost + trade policy",
        "macros": {
            "Crude Oil Prices": -2, "Commodity Prices": -2, "USD/INR / Currency": 2,
            "Global Trade Cycle": 2, "Tariffs & Import Duties": 2, "Regulatory Risk": -2,
            "Global Risk Appetite / VIX": -1
        },
        "combo": ["Crude Oil Prices", "USD/INR / Currency", "Global Trade Cycle"],
        "why": "Chemicals depend on crude-linked inputs, exports and global inventory cycles.",
    },
    "Energy": {
        "theme": "Crude + policy + demand",
        "macros": {
            "Crude Oil Prices": 2, "Indian GDP Growth": 2, "USD/INR / Currency": -1,
            "Regulatory Risk": -2, "Government Spending": 1, "Geopolitical Events": 2
        },
        "combo": ["Crude Oil Prices", "Indian GDP Growth", "Regulatory Risk"],
        "why": "Energy companies react to crude, demand and policy/pricing controls.",
    },
    "Oil & Gas": {
        "theme": "Crude + currency + regulation",
        "macros": {
            "Crude Oil Prices": 3, "USD/INR / Currency": -2, "Current Account Deficit": -1,
            "Regulatory Risk": -3, "Geopolitical Events": 2, "Inflation": -1
        },
        "combo": ["Crude Oil Prices", "USD/INR / Currency", "Regulatory Risk"],
        "why": "Upstream likes high crude; downstream and OMC margins depend on pricing freedom and currency.",
    },
    "Power / Utilities": {
        "theme": "Regulated defensive + capex + rates",
        "macros": {
            "RBI Repo Rate / Interest Rates": -2, "Government Spending": 2, "Indian GDP Growth": 1,
            "Regulatory Risk": -3, "Commodity Prices": -1, "Liquidity": 1
        },
        "combo": ["Regulatory Risk", "RBI Repo Rate / Interest Rates", "Government Spending"],
        "why": "Utilities are defensive but capital intensive and highly regulated.",
    },
    "Telecom": {
        "theme": "Regulation + capex + consumption",
        "macros": {
            "Regulatory Risk": -3, "RBI Repo Rate / Interest Rates": -2, "Consumer Demand": 1,
            "Technological Disruption": 2, "Government Spending": 1, "Market Sentiment": 1
        },
        "combo": ["Regulatory Risk", "RBI Repo Rate / Interest Rates", "Technological Disruption"],
        "why": "Telecom is capital intensive and regulated; technology cycles and spectrum policy matter.",
    },
    "Aviation": {
        "theme": "Crude + currency + travel demand",
        "macros": {
            "Crude Oil Prices": -3, "USD/INR / Currency": -2, "Consumer Demand": 3,
            "Employment / Wage Growth": 2, "Global Risk Appetite / VIX": -2, "Black Swan Events": -3
        },
        "combo": ["Crude Oil Prices", "USD/INR / Currency", "Consumer Demand"],
        "why": "Fuel and dollar costs are huge. Demand helps, but shocks can hurt sharply.",
    },
    "Paints": {
        "theme": "Crude derivatives + housing + consumption",
        "macros": {
            "Crude Oil Prices": -3, "Real Estate Cycle": 3, "Consumer Demand": 2,
            "Commodity Prices": -2, "RBI Repo Rate / Interest Rates": -1
        },
        "combo": ["Crude Oil Prices", "Real Estate Cycle", "Consumer Demand"],
        "why": "Paints benefit from housing and repainting demand but suffer from crude-linked input costs.",
    },
    "Tyres": {
        "theme": "Auto demand + crude/rubber costs",
        "macros": {
            "Auto": 0, "Crude Oil Prices": -2, "Commodity Prices": -2, "Consumer Demand": 2,
            "RBI Repo Rate / Interest Rates": -1, "USD/INR / Currency": -1
        },
        "combo": ["Consumer Demand", "Crude Oil Prices", "Commodity Prices"],
        "why": "Tyres track replacement/auto demand but margins depend on rubber and crude-linked costs.",
    },
    "Fertilizers / Agrochemicals": {
        "theme": "Monsoon + rural + subsidy/policy",
        "macros": {
            "Monsoon / Rural Economy": 3, "Government Spending": 2, "Regulatory Risk": -2,
            "Crude Oil Prices": -1, "USD/INR / Currency": -1, "Inflation": -1
        },
        "combo": ["Monsoon / Rural Economy", "Government Spending", "Regulatory Risk"],
        "why": "Farm demand and subsidy policy dominate. Imported inputs and currency also matter.",
    },
    "Textiles": {
        "theme": "Export + cotton/input costs + global trade",
        "macros": {
            "USD/INR / Currency": 2, "Global Trade Cycle": 3, "Commodity Prices": -2,
            "Consumer Demand": 2, "Tariffs & Import Duties": 1, "Employment / Wage Growth": -1
        },
        "combo": ["Global Trade Cycle", "USD/INR / Currency", "Commodity Prices"],
        "why": "Textiles are export and input-cost sensitive.",
    },
    "Logistics": {
        "theme": "Trade + fuel + industrial activity",
        "macros": {
            "Indian GDP Growth": 3, "Global Trade Cycle": 2, "Crude Oil Prices": -2,
            "Government Spending": 2, "GST Collections": 2, "Consumer Demand": 2
        },
        "combo": ["Indian GDP Growth", "Global Trade Cycle", "Crude Oil Prices"],
        "why": "Logistics follows economic activity and trade volumes. Fuel costs matter.",
    },
    "Ports": {
        "theme": "Trade cycle + commodity movement",
        "macros": {
            "Global Trade Cycle": 3, "Commodity Prices": 2, "Indian GDP Growth": 2,
            "Government Spending": 1, "Geopolitical Events": -1
        },
        "combo": ["Global Trade Cycle", "Commodity Prices", "Indian GDP Growth"],
        "why": "Ports depend on import/export volumes and commodity movement.",
    },
    "Midcap / Smallcap": {
        "theme": "Liquidity + sentiment + valuation",
        "macros": {
            "Liquidity": 3, "Market Sentiment": 3, "FII Inflows / Outflows": 2,
            "Valuation Level": -3, "RBI Repo Rate / Interest Rates": -2,
            "Global Risk Appetite / VIX": -3, "Black Swan Events": -3
        },
        "combo": ["Liquidity", "Market Sentiment", "Valuation Level"],
        "why": "Smaller stocks are more sensitive to liquidity, valuation and sentiment cycles.",
    },
}


# Remove any accidental non-macro keys in sector maps
for s in SECTORS.values():
    s["macros"] = {k: v for k, v in s["macros"].items() if k in MACROS}


# ----------------------------
# Logic helpers
# ----------------------------
def score_label(score):
    if score >= 3:
        return "Strong positive"
    if score == 2:
        return "Positive"
    if score == 1:
        return "Mild positive"
    if score == 0:
        return "Neutral / indirect"
    if score == -1:
        return "Mild negative"
    if score == -2:
        return "Negative"
    return "Strong negative"


def emoji_for_score(score):
    if score >= 2:
        return "🟢"
    if score == 1:
        return "🟡"
    if score == 0:
        return "⚪"
    if score == -1:
        return "🟠"
    return "🔴"


def movement_text(macro, score, direction="rises"):
    if direction == "rises":
        macro_text = MACROS[macro]["when_rises"]
    else:
        macro_text = MACROS[macro]["when_falls"]

    if score > 0:
        sector_effect = "sector usually benefits"
    elif score < 0:
        sector_effect = "sector usually faces pressure"
    else:
        sector_effect = "effect is usually indirect or mixed"

    if direction == "falls":
        score = -score if macro not in ["NPAs / Banking Stress", "Regulatory Risk", "Global Risk Appetite / VIX", "Black Swan Events"] else -score

    return macro_text, sector_effect


def build_sector_rows(sector_name):
    rows = []
    for macro, score in SECTORS[sector_name]["macros"].items():
        rows.append({
            "Macro": macro,
            "Macro family": MACROS[macro]["family"],
            "Direction when macro rises / improves": score_label(score),
            "Score": score,
            "Signal": emoji_for_score(score),
            "Why": MACROS[macro]["when_rises"],
            "Independence note": MACROS[macro]["independence_note"],
        })
    df = pd.DataFrame(rows).sort_values("Score", key=lambda x: x.abs(), ascending=False)
    return df


def independent_combo_for_sector(sector_name):
    sector = SECTORS[sector_name]
    candidates = sorted(sector["macros"].items(), key=lambda x: abs(x[1]), reverse=True)
    selected = []
    used_families = set()
    for macro, score in candidates:
        fam = MACROS[macro]["family"]
        if fam not in used_families:
            selected.append((macro, score, fam))
            used_families.add(fam)
        if len(selected) == 3:
            break
    return selected


def combo_sentence(combo):
    parts = []
    for macro, score, fam in combo:
        direction = "supports" if score > 0 else "pressures" if score < 0 else "mixed"
        parts.append(f"{macro} ({direction})")
    return " + ".join(parts)


def scenario_sector_effect(sector_name, selected_macros):
    total = 0
    notes = []
    for macro in selected_macros:
        score = SECTORS[sector_name]["macros"].get(macro, 0)
        total += score
        if score != 0:
            notes.append(f"{macro}: {score_label(score)}")
    if total >= 5:
        verdict = "Strong tailwind"
    elif total >= 2:
        verdict = "Tailwind"
    elif total > -2:
        verdict = "Mixed / neutral"
    elif total > -5:
        verdict = "Headwind"
    else:
        verdict = "Strong headwind"
    return total, verdict, "; ".join(notes) if notes else "No strong direct theoretical link."




# ----------------------------
# Direct Analyzer UI
# ----------------------------
st.markdown('<div class="main-title">🪩 Macro Dance Floor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Select a sector, choose one macro or a clean macro combo, then click Analyze.</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <div class="hero-label">Direct Theoretical Analyzer • No Data Needed</div>
        <div class="hero-head">Test any sector against individual macros or macro combinations.</div>
        <div class="hero-text">
            This is the simple model you wanted: choose a sector and select macro factors.
            The app tells whether those macros theoretically support, pressure, or have mixed effect on that sector.
            It also warns when your chosen macro combo may be interlinked rather than independent.
        </div>
        <br>
        <span class="chip">Sector + Macro</span>
        <span class="chip">Macro Combo</span>
        <span class="chip">Positive / Negative Direction</span>
        <span class="chip">Independent Macro Warning</span>
        <span class="chip">Luxury Dashboard</span>
    </div>
    """,
    unsafe_allow_html=True,
)

card_start("mega-card")
st.markdown('<div class="block-label">How to use</div>', unsafe_allow_html=True)
dialog(
    "Simple 3-step flow",
    "Pick a <b>sector</b>, pick one or more <b>macros</b>, and click <b>Analyze Macro Dance</b>. The app will show whether your selected macro setup is a theoretical <b>tailwind</b>, <b>headwind</b>, or <b>mixed effect</b> for that sector.",
    "purple",
)

step1, step2, step3 = st.columns(3, gap="large")
with step1:
    st.markdown("""
    <div class="step-card">
        <div class="step-no">01</div>
        <div class="step-head">Choose a sector</div>
        <div class="step-text">Pick the sector you want to test like Banks, Auto, Pharma, FMCG, IT, Realty, Metals or any other sector available in the model.</div>
    </div>
    """, unsafe_allow_html=True)
with step2:
    st.markdown("""
    <div class="step-card">
        <div class="step-no">02</div>
        <div class="step-head">Choose one macro or a combo</div>
        <div class="step-text">Select a single macro for direct effect, or choose multiple macros to test a broader theoretical macro environment.</div>
    </div>
    """, unsafe_allow_html=True)
with step3:
    st.markdown("""
    <div class="step-card">
        <div class="step-no">03</div>
        <div class="step-head">Click analyze</div>
        <div class="step-text">The app will score the chosen macro setup, explain each macro separately, and show whether the combo looks clean or interlinked.</div>
    </div>
    """, unsafe_allow_html=True)
card_end()

# Main selector area
card_start("gold-card")
st.markdown('<div class="block-label">Macro test console</div>', unsafe_allow_html=True)
dialog(
    "What this console does",
    "This is your main testing box. You can test <b>one macro</b> or a <b>combo of macros</b> against any one sector. For cleaner theoretical combos, try mixing different macro families instead of stacking too many similar macros together.",
    "blue",
)

col1, col2 = st.columns([1, 1.5], gap="large")
with col1:
    selected_sector = st.selectbox(
        "1️⃣ Select sector",
        list(SECTORS.keys()),
        index=list(SECTORS.keys()).index("Banks") if "Banks" in SECTORS else 0,
    )
    dialog("Selected sector theme", SECTORS[selected_sector]["theme"], "yellow")

with col2:
    selected_macros = st.multiselect(
        "2️⃣ Select individual macro or macro combo",
        options=list(MACROS.keys()),
        default=["RBI Repo Rate / Interest Rates", "Inflation", "Bank Credit Growth"],
    )
    st.markdown(
        """
        <div class="lux-note">
            <h4>Premium selection tip</h4>
            <div style="color:#57486a; line-height:1.7; font-size:14px;">
                Example of a cleaner combo: <b>Rates + Demand + Liquidity</b>.<br>
                Example of a more interlinked combo: <b>Repo Rate + Bond Yields + Inflation</b>.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

analyze = st.button("🪩 Analyze Macro Dance", use_container_width=True, type="primary")
card_end()

if not analyze:
    preview1, preview2, preview3 = st.columns(3, gap="large")
    with preview1:
        card_start("blue-card")
        st.subheader("Single macro test")
        dialog(
            "When to use this",
            "Use one macro when you want a clean answer like: <b>How does inflation affect FMCG?</b> or <b>How do rates affect realty?</b>",
            "blue",
        )
        card_end()
    with preview2:
        card_start("pink-card")
        st.subheader("Combo macro test")
        dialog(
            "When to use this",
            "Use 2 to 5 macros when you want to create a broader environment like: <b>high liquidity + strong demand + rising credit growth</b>.",
            "pink",
        )
        card_end()
    with preview3:
        card_start("green-card")
        st.subheader("Independent macro check")
        dialog(
            "What the app checks",
            "The app flags when your chosen macros come from repeated families. That helps you avoid treating closely linked macro forces as fully independent.",
            "green",
        )
        card_end()

    st.stop()

if not selected_macros:
    st.error("Please select at least one macro.")
    st.stop()

# ----------------------------
# Analysis calculations
# ----------------------------
sector_info = SECTORS[selected_sector]
rows = []
total_score = 0

for macro in selected_macros:
    score = sector_info["macros"].get(macro, 0)
    total_score += score
    rows.append({
        "Macro": macro,
        "Macro family": MACROS[macro]["family"],
        "Impact score": score,
        "Theoretical direction": score_label(score),
        "Signal": emoji_for_score(score),
        "When macro rises / improves": MACROS[macro]["when_rises"],
        "When macro falls / weakens": MACROS[macro]["when_falls"],
        "Independence note": MACROS[macro]["independence_note"],
    })

result_df = pd.DataFrame(rows)

if total_score >= 6:
    verdict = "Strong theoretical tailwind"
    tone = "green"
elif total_score >= 2:
    verdict = "Theoretical tailwind"
    tone = "green"
elif total_score > -2:
    verdict = "Mixed / neutral theoretical effect"
    tone = "yellow"
elif total_score > -6:
    verdict = "Theoretical headwind"
    tone = "pink"
else:
    verdict = "Strong theoretical headwind"
    tone = "pink"

families = [MACROS[m]["family"] for m in selected_macros]
duplicate_families = sorted([f for f in set(families) if families.count(f) > 1])

# ----------------------------
# Results
# ----------------------------
card_start("green-card" if "tailwind" in verdict.lower() else "pink-card" if "headwind" in verdict.lower() else "gold-card")
st.markdown('<div class="block-label">Analysis result</div>', unsafe_allow_html=True)
st.header(f"{selected_sector} × Macro Dance Result")
dialog(
    "How to read this section",
    "This is the final interpretation of your selected macro setup. <b>Positive score</b> means support, <b>negative score</b> means pressure, and <b>near-zero score</b> means the overall effect is mixed or balanced.",
    "purple",
)

m1, m2, m3, m4 = st.columns(4, gap="large")
m1.metric("Sector", selected_sector)
m2.metric("Macros tested", len(selected_macros))
m3.metric("Net score", total_score)
m4.metric("Verdict", verdict)

dialog(
    "Final answer",
    f"For <b>{selected_sector}</b>, the selected macro setup gives a <b>{verdict}</b>. The net score is <b>{total_score}</b>. Positive score means sector support; negative score means pressure; near zero means mixed effect.",
    tone,
)
card_end()

left, right = st.columns([1.2, 1])

with left:
    card_start("card")
    st.subheader("Macro-by-macro impact")
    dialog(
        "What this table shows",
        "Each selected macro is shown separately so you can see its <b>family</b>, <b>impact score</b>, and whether it is a tailwind or headwind for the selected sector.",
        "blue",
    )
    st.dataframe(
        result_df[["Signal", "Macro", "Macro family", "Impact score", "Theoretical direction", "When macro rises / improves", "Independence note"]],
        use_container_width=True,
        hide_index=True,
    )
    card_end()

with right:
    card_start("card")
    st.subheader("Visual impact view")
    dialog(
        "How to read the bars",
        "Bars to the <b>right</b> show support for the sector. Bars to the <b>left</b> show pressure. Bigger absolute bars mean stronger theoretical importance.",
        "green",
    )
    chart_df = result_df[["Macro", "Impact score"]].copy()
    chart_df = chart_df.set_index("Macro").sort_values("Impact score")
    st.bar_chart(chart_df, use_container_width=True, height=520)
    card_end()

# Independence check
card_start("blue-card")
st.markdown('<div class="block-label">Independent macro check</div>', unsafe_allow_html=True)
dialog(
    "Why this matters",
    "A combo looks cleaner when the selected macros come from different families. If too many selected macros belong to the same family, the combo may be conceptually crowded or interlinked.",
    "blue",
)
if duplicate_families:
    dialog(
        "Macros may be interlinked",
        "You selected multiple macros from the same family: <b>" + ", ".join(duplicate_families) + "</b>. This is not wrong, but avoid treating them as fully independent. Example: repo rate, bond yields and inflation often move together.",
        "yellow",
    )
else:
    dialog(
        "Clean combo",
        "Selected macros come from different macro families, so this is a cleaner theoretical macro combo.",
        "green",
    )

family_df = result_df.groupby("Macro family")["Impact score"].sum().reset_index().sort_values("Impact score")
family_chart = family_df.set_index("Macro family")[["Impact score"]]
st.bar_chart(family_chart, use_container_width=True, height=420)
card_end()

# Plain explanation
card_start("gold-card")
st.markdown('<div class="block-label">Plain English explanation</div>', unsafe_allow_html=True)
st.subheader("What this means")
dialog(
    "Simple takeaway",
    "This section turns the result into plain language so you can quickly understand the sector logic without reading the whole table again.",
    "yellow",
)
st.write(f"**Sector nature:** {sector_info['theme']}")
st.write(f"**Core sector logic:** {sector_info['why']}")

positive = result_df[result_df["Impact score"] > 0]
negative = result_df[result_df["Impact score"] < 0]
neutral = result_df[result_df["Impact score"] == 0]

if not positive.empty:
    st.success("Tailwind macros: " + ", ".join(positive["Macro"].tolist()))
if not negative.empty:
    st.error("Headwind macros: " + ", ".join(negative["Macro"].tolist()))
if not neutral.empty:
    st.info("Neutral/indirect macros: " + ", ".join(neutral["Macro"].tolist()))

best_combo = independent_combo_for_sector(selected_sector)
dialog(
    "Model-suggested clean combo for this sector",
    f"For <b>{selected_sector}</b>, a cleaner independent theoretical combo is: <b>{combo_sentence(best_combo)}</b>.",
    "purple",
)
card_end()

# All macro map for selected sector
with st.expander("View full macro map for this sector"):
    full_df = build_sector_rows(selected_sector)
    st.dataframe(
        full_df[["Signal", "Macro", "Macro family", "Direction when macro rises / improves", "Why", "Independence note"]],
        use_container_width=True,
        hide_index=True,
    )

st.markdown("---")
dialog(
    "Reminder",
    "This app is a theoretical macro-sector concept engine. It explains usual direction of impact. It does not predict exact stock returns.",
    "blue",
)
