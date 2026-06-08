import streamlit as st
import random

def text_to_uwu(text: str) -> str:
    text_size = len(text)
    index = 0
    uwuified = ""
    kaomojis = ["(・`ω´・)", ";;w;;", "owo", "UwU", ">w<", "^w^", ":3", "xD", "(*^_^*)", "(^人^)", "(>_<)", "(^o^)", "(^_^)/", "(*^.^*)", "(>ω<)", "(^_^)", "(^_^;)", "(>_<)"]

    while index < text_size:
        if text[index] == "l" or text[index] == "r":
            uwuified += "w"
            index += 1
        elif text[index] == "t" and index + 1 < text_size and text[index + 1] == "h":
            uwuified += "d"
            index += 2
        else:
            uwuified += text[index]
            index += 1
    uwuified += " " + random.choice(kaomojis)
    return uwuified


def main() -> None:
    st.set_page_config(page_title="Babi UwU", page_icon="./assets/awesome_logo.png", layout="wide")

    placeholders=[
        "Hello world!",
        "I am a text uwu-ificator tool!",
        "Lorem ipsum dolor sit amet, yada yada.",
        "In the grim darkness of the far future, there is only war.",
        "U.u.user...",
        "It's not like I want to uwu-ify your text or anything...",
        "Chat, is this real?",
        "Number fifteeeeeen, burger king foot lettuuuuuuce...",
        "Please, Speed, I need this! My mom is kinda homeless...",

        ]
    
    st.markdown("# :rainbow[Babi UwU!]")
    st.subheader("This is a text uwu-ificator tool! You input a text and it will, uh, uwu-ify it... ^^")
    st.caption("(That's very much it.)")
    st.divider()

    input_col, output_col = st.columns(2)
    with input_col:
        st.write("Please insert your text here... >.<")
        text = st.code(language="text", height="stretch")
    with output_col:
        st.write("uwu-ified text:")
        if text:
            st.code(text_to_uwu(text), language="text")
        else:
            st.code(text_to_uwu(random.choice(placeholders)), language="text", height="stretch")
    
    st.caption("Version 1.0.0s")
    st.caption("Made wuv by [@obabigail] on github! Check out the repo [here](https://github.com/obabigail/uwuifier)!")

if __name__ == "__main__":
    main()
