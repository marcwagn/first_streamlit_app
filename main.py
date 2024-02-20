import streamlit as st

def main():
    st.title("ICE AGE - Wiki")

    with st.sidebar:
        st.title("Configuration")
        st.subheader("Image uploader")
        img = st.file_uploader("Select input image", type=["jpg", "png"], accept_multiple_files=False)

        st.subheader("Data uploader")
        data = st.file_uploader("Select input data", type=["csv"], accept_multiple_files=False)


    tab1, tab2 = st.tabs(["Sid :sloth:", "Movie data :bar_chart:"])

    with tab1:
        st.write(""" Sidney, known more commonly as Sid, is a ground sloth who was part of a herd of different animals after a number of adventures and experiences brought them all together. Born into a family of sloths that went on to abandon him well into his adulthood, Sid met a mammoth named Manny and a saber-tooth tiger named Diego as the three of them made a journey through a tundra to return a human baby named Roshan to his tribe.""")

        content = st.radio("**What kind of information you want?**",('Video', 'Image'), horizontal=True)

        if content == "Image":    
            if img is not None:
                _, cent_co, _ = st.columns(3)
                with cent_co:
                    st.image(img, width=300)

        elif content == "Video":
            st.subheader("Sid is sleeping")
            st.video("https://www.youtube.com/watch?v=fqgxRcGkTSo")

    with tab2:
        st.write("Plot something")
    

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass