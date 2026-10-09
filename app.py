
import streamlit as st

from llm import generate_response
from prompt_templates import (
    zero_shot_prompt,
    one_shot_prompt,
    few_shot_prompt,
    cot_prompt
)

st.set_page_config(
    page_title="Prompt Engineering Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Prompt Engineering Dashboard")
st.write("Compare different prompting techniques using an LLM.")

st.sidebar.title("Prompt Technique")

technique = st.sidebar.selectbox(
    "Choose a technique",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "Chain-of-Thought"
    ]
)

st.sidebar.info(
    "Select a prompting technique and enter your question."
)

user_input = st.text_area(
    "Enter your prompt",
    placeholder="Example: Explain Artificial Intelligence",
    height=120
)

if st.button("Generate Response", type="primary"):
    if user_input.strip():

        if technique == "Zero-shot":
            prompt = zero_shot_prompt(user_input)

        elif technique == "One-shot":
            prompt = one_shot_prompt(user_input)

        elif technique == "Few-shot":
            prompt = few_shot_prompt(user_input)

        else:
            prompt = cot_prompt(user_input)

        try:
            with st.spinner("Generating response..."):
                response = generate_response(prompt)

            st.subheader("Selected Technique")
            st.write(technique)

            st.subheader("Generated Response")
            st.write(response)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a prompt.")
