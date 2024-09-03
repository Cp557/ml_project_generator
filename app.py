import streamlit as st

# Define topic groups
libraries = ['NumPy', 'Pandas', 'TensorFlow', 'Keras', 'PyTorch', 'Matplotlib', 'Seaborn', 'Scikit-learn']
ml_algorithms = ['Linear Regression', 'Logistic Regression', 'Decision Trees', 'Random Forests', 'SVM', 'KNN']

# Custom CSS for button styling
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
    }
    .selected {
        background-color: #ff4b4b !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

def toggle_button(key):
    if key not in st.session_state:
        st.session_state[key] = False
    st.session_state[key] = not st.session_state[key]

def main():
    st.title("Interactive ML Project Generator")

    st.header("Generate Your Customized ML Project")
    st.write("Select libraries and ML algorithms you want to practice, then enter a project theme to get started!")

    # Library selection
    st.subheader("Select Libraries")
    cols_lib = st.columns(3)
    selected_libraries = []
    for i, lib in enumerate(libraries):
        button_key = f"lib_{lib}"
        if button_key not in st.session_state:
            st.session_state[button_key] = False
        if cols_lib[i % 3].button(
            lib, 
            key=button_key, 
            on_click=toggle_button, 
            args=(button_key,),
            type="secondary" if not st.session_state[button_key] else "primary"
        ):
            pass
        if st.session_state[button_key]:
            selected_libraries.append(lib)

    st.write("Selected libraries:", ", ".join(selected_libraries))

    # ML Algorithm selection
    st.subheader("Select ML Algorithms")
    cols_algo = st.columns(3)
    selected_algorithms = []
    for i, algo in enumerate(ml_algorithms):
        button_key = f"algo_{algo}"
        if button_key not in st.session_state:
            st.session_state[button_key] = False
        if cols_algo[i % 3].button(
            algo, 
            key=button_key, 
            on_click=toggle_button, 
            args=(button_key,),
            type="secondary" if not st.session_state[button_key] else "primary"
        ):
            pass
        if st.session_state[button_key]:
            selected_algorithms.append(algo)

    # Display selected topics
    st.write("Selected ML Algorithms:", ", ".join(selected_algorithms))

    with st.form(key='project_form'):
        st.subheader("Enter Project Theme")
        project_theme = st.text_input("What would you like your project to be about?")
        submit_button = st.form_submit_button(label='Generate Project')

    # Handle form submission
    if submit_button:
        if (selected_libraries or selected_algorithms) and project_theme:
            st.success("Generating your project...")
            # Here you would call your project generation function
            st.write(f"Generating a project about '{project_theme}'")
            st.write(f"Using libraries: {', '.join(selected_libraries)}")
            st.write(f"Implementing algorithms: {', '.join(selected_algorithms)}")
        else:
            st.error("Please select at least one library or algorithm and enter a project theme.")

if __name__ == "__main__":
    main()
