import streamlit as st
from PIL import Image

if "page" not in st.session_state:
    st.session_state.page = "r1_pick"
if "choice" not in st.session_state:
    st.session_state.choice = None

# ROUND 1 — Pick Blue or Green
if st.session_state.page == "r1_pick":
    st.title("Round 1 — Pick a color")
    st.image("round1_choices.png", use_column_width=True)
    for color in ["💙 Blue", "💚 Green"]:
        if st.button(color, use_container_width=True):
            st.session_state.choice = color
            st.session_state.page = "r1_result"
            st.rerun()

elif st.session_state.page == "r1_result":
    st.title(f"You picked {st.session_state.choice}!")
    st.image("round1_output.png", use_column_width=True)
    if st.button("➡️ Next Round", use_container_width=True):
        st.session_state.page = "r2_pick"
        st.rerun()
    if st.button("⬅️ Back", use_container_width=True):
        st.session_state.page = "r1_pick"
        st.rerun()

# ROUND 2 — Pick Yellow or Purple
elif st.session_state.page == "r2_pick":
    st.title("Round 2 — Pick a color")
    st.image("round2_choices.png", use_column_width=True)
    for color in ["💛 Yellow", "💜 Purple"]:
        if st.button(color, use_container_width=True):
            st.session_state.choice = color
            st.session_state.page = "r2_result"
            st.rerun()

elif st.session_state.page == "r2_result":
    st.title(f"You picked {st.session_state.choice}!")
    st.image("round2_output.png", use_column_width=True)
    if st.button("➡️ Next Round", use_container_width=True):
        st.session_state.page = "r3_pick"
        st.rerun()
    if st.button("⬅️ Back", use_container_width=True):
        st.session_state.page = "r2_pick"
        st.rerun()

# ROUND 3 — Pick from 9 colors
elif st.session_state.page == "r3_pick":
    st.title("Round 3 — Pick a color")
    st.image("round3_choices.png", use_column_width=True)
    for color in ["💜 Lavender", "🩷 Pink", "🩵 Sky Blue", "🧡 Orange",
                  "💚 Mint Green", "🩵 Cyan", "❤️ Red", "💚 Green", "💙 Dark Blue"]:
        if st.button(color, use_container_width=True):
            st.session_state.choice = color
            st.session_state.page = "r3_result"
            st.rerun()

elif st.session_state.page == "r3_result":
    st.title(f"You picked {st.session_state.choice}!")
    st.image("round3_output.png", use_column_width=True)
    if st.button("🔁 Start Over", use_container_width=True):
        st.session_state.page = "r1_pick"
        st.session_state.choice = None
        st.rerun()
    if st.button("⬅️ Back", use_container_width=True):
        st.session_state.page = "r3_pick"
        st.rerun()
