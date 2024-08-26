import streamlit as st

# Define topic groups
libraries = ['NumPy', 'Pandas', 'TensorFlow', 'Keras', 'Matplotlib', 'Seaborn', 'Scikit-learn']
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

def toggle_selection(item, selected_list):
    if item in selected_list:
        selected_list.remove(item)
    else:
        selected_list.append(item)
    return selected_list


def generate_project():
    if (st.session_state.selected_libraries or st.session_state.selected_algorithms) and st.session_state.project_theme:
        st.success("Generating your project...")
        # Here you would call your project generation function
        st.write(f"Generating a project about '{st.session_state.project_theme}'")
        st.write(f"Using libraries: {', '.join(st.session_state.selected_libraries)}")
        st.write(f"Implementing algorithms: {', '.join(st.session_state.selected_algorithms)}")
    else:
        st.error("Please select at least one library or algorithm and enter a project theme.")


def main():
    st.title("Interactive ML Project Generator")

    st.header("Generate Your Customized ML Project")
    st.write("Select libraries and ML algorithms you want to practice, then enter a project theme to get started!")

    # Initialize session state for selections
    if 'selected_libraries' not in st.session_state:
        st.session_state.selected_libraries = []
    if 'selected_algorithms' not in st.session_state:
        st.session_state.selected_algorithms = []

    # Library selection
    st.subheader("Select Libraries")
    cols_lib = st.columns(3)
    for i, lib in enumerate(libraries):
        button_key = f"lib_{lib}"
        button_class = "selected" if lib in st.session_state.selected_libraries else ""
        if cols_lib[i % 3].button(lib, key=button_key):
            st.session_state.selected_libraries = toggle_selection(lib, st.session_state.selected_libraries)
        cols_lib[i % 3].markdown(f"<script>document.querySelector('button[kind=secondary][data-testid={button_key}]').className += ' {button_class}';</script>", unsafe_allow_html=True)

    
    st.write("Selected libraries:", ", ".join(st.session_state.selected_libraries))
    # ML Algorithm selection
    st.subheader("Select ML Algorithms")
    cols_algo = st.columns(3)
    for i, algo in enumerate(ml_algorithms):
        button_key = f"algo_{algo}"
        button_class = "selected" if algo in st.session_state.selected_algorithms else ""
        if cols_algo[i % 3].button(algo, key=button_key):
            st.session_state.selected_algorithms = toggle_selection(algo, st.session_state.selected_algorithms)
        cols_algo[i % 3].markdown(f"<script>document.querySelector('button[kind=secondary][data-testid={button_key}]').className += ' {button_class}';</script>", unsafe_allow_html=True)

    # Display selected topics
    st.write("Selected ML Algorithms:", ", ".join(st.session_state.selected_algorithms))

    with st.form(key='project_form'):
        st.subheader("Enter Project Theme")
        project_theme = st.text_input("What would you like your project to be about?")
        submit_button = st.form_submit_button(label='Generate Project')

    # Handle form submission
    if submit_button:
        if (st.session_state.selected_libraries or st.session_state.selected_algorithms) and project_theme:
            st.success("Generating your project...")
            # Here you would call your project generation function
            st.write(f"Generating a project about '{project_theme}'")
            st.write(f"Using libraries: {', '.join(st.session_state.selected_libraries)}")
            st.write(f"Implementing algorithms: {', '.join(st.session_state.selected_algorithms)}")
        else:
            st.error("Please select at least one library or algorithm and enter a project theme.")

if __name__ == "__main__":
    main()