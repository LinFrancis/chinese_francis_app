import streamlit as st
import pandas as pd
import re
import uuid


st.set_page_config(
    page_title="林高天 Journey",
    layout="wide",
    initial_sidebar_state="expanded",  # 👈 this keeps the sidebar open
    page_icon="🌱"
)



st.title("Chinese Words Dictionary")

from sidebar_header import render_sidebar_header
render_sidebar_header()


@st.cache_data

def load_data():
    df = pd.read_excel("HelloChinese Word List_edited_2025.xlsx", sheet_name="HelloChinese")
    df = df.dropna(subset=["Characters / Traditional", "Pinyin", "Meaning"])
    df["Tags"] = df["Meaning"].apply(lambda m: re.findall(r"\b[A-Z]{1,4}\.", str(m)))

    # Add category mapping
    dimension_to_category = {
        # Introductions & Identity
        "Hello": "Introductions",
        "Who am I?": "Introductions",
        "Presentation": "Introductions",

        # Language Learning
        "Learning Chinese 1": "Language Learning",
        "Learning Chinese 2": "Language Learning",
        "School": "Language Learning",
        "My learning goals in China": "Language Learning",

        # Food & Dining
        "Food": "Food & Dining",
        "Taste": "Food & Dining",
        "Ordering Food": "Food & Dining",
        "Restaurants 1": "Food & Dining",
        "Restaurants 2": "Food & Dining",

        # Social Interaction
        "Helping Out": "Social Interaction",
        "Suggestions": "Social Interaction",
        "Dating": "Social Interaction",
        "Feelings": "Social Interaction",
        "Greetings": "Social Interaction",
        "Apologizing": "Social Interaction",
        "Gossip": "Social Interaction",
        "Arguments": "Social Interaction",
        "Praise": "Social Interaction",
        "What I do": "Social Interaction",

        # People & Descriptions
        "Appearance": "People & Descriptions",
        "Clothes": "People & Descriptions",
        "Colors": "People & Descriptions",
        "Personality": "People & Descriptions",
        "My love for Chinese culture and music": "People & Descriptions",

        # Daily Life & Routines
        "Money": "Daily Life",
        "Daily Schedule": "Daily Life",
        "Habits": "Daily Life",
        "Housework": "Daily Life",
        "Mistakes": "Daily Life",
        "Bad Luck": "Daily Life",
        "Daily Life": "Daily Life",
        "Life": "Daily Life",

        # Family & Relationships
        "Family 1": "Family & Relationships",
        "Family 2": "Family & Relationships",

        # Work & Career
        "Career": "Work & Career",
        "Interviews": "Work & Career",
        "Office Work": "Work & Career",
        "Work": "Work & Career",

        # Shopping & Services
        "Shopping": "Shopping",
        "Online Shopping": "Shopping",
        "Bargaining": "Shopping",

        # Travel & Transport
        "Transport": "Travel",
        "Traveling 1": "Travel",
        "Traveling 2": "Travel",
        "Catching a Flight": "Travel",
        "Going Abroad": "Travel",
        "Renting": "Travel",

        # Places & Living
        "Hometown": "Places & Living",
        "Locations": "Places & Living",
        "Directions": "Places & Living",
        "Rooms": "Places & Living",
        "Weather": "Places & Living",

        # Personal & Communication
        "Personal Information": "Personal & Communication",
        "Phone-Calls": "Personal & Communication",
        "Communications": "Personal & Communication",

        # Time & Dates
        "Time": "Time & Dates",
        "Dates": "Time & Dates",

        # Hobbies & Leisure
        "Leisure": "Hobbies & Leisure",
        "Sports": "Hobbies & Leisure",
        "Spare Time": "Hobbies & Leisure",
        "Sports Competitions": "Hobbies & Leisure",
        "Movies": "Hobbies & Leisure",
        "Hiking": "Hobbies & Leisure",

        # Emotions & Cognition
        "Comparing": "Emotions & Cognition",
        "Shocked": "Emotions & Cognition",
        "Questions": "Emotions & Cognition",

        # Health & Well-being
        "Weight Loss": "Health & Well-being",
        "Health": "Health & Well-being",

        # Nature & Environment
        "Pets": "Nature & Environment",
        "Nature": "Nature & Environment",
        "Environment": "Nature & Environment",
        "Regeneration": "Nature & Environment",
        "Why regeneration": "Nature & Environment",
        "Final thought": "Reflections",

        # Culture & Interests
        "China 1": "Culture & Interests",
        "China 2": "Culture & Interests",
        
        
        
        # Catch-all
        # any unmapped dimension → “Other”
    }

    df["Category"] = df["Dimension"].map(dimension_to_category).fillna("Other")
    return df

def extract_tag_segment(meaning, tag):
    if pd.isna(meaning):
        return "", meaning
    parts = re.split(r'(\b[A-Z]{1,4}\.)', meaning)
    highlighted = ""
    building = False
    for i, part in enumerate(parts):
        if part == tag:
            building = True
            highlighted += f"**{part}"
        elif building and re.match(r"\b[A-Z]{1,4}\.", part):
            break
        elif building:
            highlighted += f" {part}"
    return highlighted.strip(), meaning

# Define grammatical groups
grammar_groups = {
    "Verbs": ["V.", "V.O.", "S.V.", "R.V.", "AUX.", "COV.", "B.F."],
    "Nouns & Pronouns": ["N.", "NOUN", "PR.", "SUF."],
    "Adjectives": ["A.M.", "ATTR."],
    "Adverbs": ["ADV."],
    "Measure/Classifiers": ["M.", "M.P."],
    "Particles": ["P.W."],
    "Conjunctions": ["CONS.", "CONJ."],
    "Numbers": ["NUM."]
}

# Load data
df = load_data()

# Sidebar filters

# Search section first
st.sidebar.markdown("## 🔍 Search")
if "last_search" not in st.session_state:
    st.session_state.last_search = ""

search_text = st.sidebar.text_input("Search word or pinyin", value="")

if search_text:
    st.session_state.last_search = search_text
whole_word_only = st.sidebar.checkbox("Match whole word only")
if st.sidebar.button("Reset All"):
    st.rerun()
st.sidebar.markdown("---")
group_options = ["All"] + list(grammar_groups.keys())
selected_group = st.sidebar.selectbox("Select grammatical category:", group_options, key="sidebar_group")

# Map tags to full descriptions
tag_descriptions = {
    "V.": "Verb",
    "V.O.": "Verb-Object",
    "S.V.": "Subject-Verb",
    "R.V.": "Reduplicated Verb",
    "AUX.": "Auxiliary Verb",
    "COV.": "Coverb",
    "B.F.": "Base Form",
    "N.": "Noun",
    "NOUN": "Noun",
    "PR.": "Pronoun",
    "SUF.": "Suffix",
    "A.M.": "Adjective Modifier",
    "ATTR.": "Attributive",
    "ADV.": "Adverb",
    "M.": "Measure Word",
    "M.P.": "Measure Word / Particle",
    "P.W.": "Particle Word",
    "CONS.": "Conjunction",
    "CONJ.": "Conjunction",
    "NUM.": "Number"
}

# Create reverse lookup for selectbox
tag_display = {v: k for k, v in tag_descriptions.items() if k in {tag for tags in df["Tags"] for tag in tags}}
tag_display_options = ["All"] + sorted(tag_display.keys())
selected_tag_label = st.sidebar.selectbox("Or select specific grammatical tag:", tag_display_options, key="sidebar_tag")
selected_tag = tag_display[selected_tag_label] if selected_tag_label != "All" else "All"

# Category and Subcategory filter
all_categories = sorted(df["Category"].unique())
selected_category = st.sidebar.selectbox("Topic Category:", ["All"] + all_categories, key="sidebar_cat")

subcat_options = df[df["Category"] == selected_category]["Dimension"].unique() if selected_category != "All" else df["Dimension"].unique()
selected_subcat = st.sidebar.selectbox("Subtopic (Dimension):", ["All"] + sorted(subcat_options), key="sidebar_subcat")





# Filter logic
filtered = df.copy()

if selected_group != "All":
    group_tags = grammar_groups[selected_group]
    filtered = filtered[filtered["Tags"].apply(lambda tags: any(tag in tags for tag in group_tags))]
elif selected_tag != "All":
    filtered = filtered[filtered["Tags"].apply(lambda tags: selected_tag in tags)]

if selected_category != "All":
    filtered = filtered[filtered["Category"] == selected_category]
if selected_subcat != "All":
    filtered = filtered[filtered["Dimension"] == selected_subcat]
import difflib
if search_text:
    search_lower = search_text.lower()
    def fuzzy_match(text):
        if whole_word_only:
            return re.search(rf'\b{re.escape(search_lower)}\b', text, re.IGNORECASE) is not None
        return search_lower in text.lower() or difflib.SequenceMatcher(None, search_lower, text.lower()).ratio() > 0.7
    filtered = filtered[filtered["Characters / Traditional"].apply(fuzzy_match) |
                        filtered["Pinyin"].apply(fuzzy_match) |
                        filtered["Meaning"].apply(fuzzy_match)]

if st.session_state.last_search and not (selected_group != "All" or selected_tag != "All" or selected_category != "All" or selected_subcat != "All"):
    st.markdown(f"🔍 Word searched: \"{st.session_state.last_search}\"")




tab1, tab2 = st.tabs(["🔖 Flashcards View", "📊 Table View"])

with tab1:
    st.markdown(f"### Showing {len(filtered)} words")
    for cat in sorted(filtered["Category"].unique()):
        cat_df = filtered[filtered["Category"] == cat]
        with st.expander(cat, expanded=False):
            for dim in sorted(cat_df["Dimension"].unique()):
                st.markdown(f"#### 📘 {dim}")
                for _, row in cat_df[cat_df["Dimension"] == dim].iterrows():
                    char = row["Characters / Traditional"]
                    pinyin = row["Pinyin"]
                    meaning = row["Meaning"]
                    tags = row["Tags"]
                    tag_highlight = ""
                    highlighted_html = meaning

                    # Highlight specific tag if selected
                    tag_to_highlight = selected_tag if selected_tag != "All" else None
                    if selected_group != "All":
                        for gtag in grammar_groups[selected_group]:
                            if gtag in tags:
                                tag_to_highlight = gtag
                                break

                    if tag_to_highlight:
                        tag_highlight, _ = extract_tag_segment(meaning, tag_to_highlight)
                        if tag_highlight:
                            highlighted_html = meaning.replace(tag_highlight, f'<mark style="background-color:#d4edda; padding:2px; border-radius:3px;">{tag_highlight}</mark>', 1)

                    st.markdown(f"""
                        <div style='border: 2px solid #cde3d4; border-radius: 12px; padding: 1rem; margin-bottom: 1rem; background-color: #edf7f1;'>
                            <div style='display: flex; justify-content: space-between;'>
                                <div style='flex: 1;'>
                                    <h3 style='margin: 0;'>{char}</h3>
                                    <p><code>{pinyin}</code></p>
                                </div>
                                <div style='flex: 2;'>
                                    <p>{highlighted_html}</p>
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

with tab2:
    st.dataframe(filtered, use_container_width=True)

