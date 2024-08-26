import streamlit as st

# Define topic groups
libraries = ['NumPy', 'Pandas', 'TensorFlow', 'Keras', 'Matplotlib', 'Seaborn', 'Scikit-learn']
ml_algorithms = ['Linear Regression', 'Logistic Regression', 'Decision Trees', 'Random Forests', 'SVM', 'KNN']

def main():
    st.title("Interactive ML Project Generator")

    st.header("Generate Your Customized ML Project")
    st.write("Select libraries and ML algorithms you want to practice, then enter a project theme to get started!")

    # Library selection
    st.subheader("Select Libraries")
    selected_libraries = []
    cols_lib = st.columns(3)
    for i, lib in enumerate(libraries):
        if cols_lib[i % 3].button(lib, key=f"lib_{lib}"):
            if lib in selected_libraries:
                selected_libraries.remove(lib)
            else:
                selected_libraries.append(lib)

    st.write("Selected libraries:", ", ".join(selected_libraries))

    # ML Algorithm selection
    st.subheader("Select ML Algorithms")
    selected_algorithms = []
    cols_algo = st.columns(3)
    for i, algo in enumerate(ml_algorithms):
        if cols_algo[i % 3].button(algo, key=f"algo_{algo}"):
            if algo in selected_algorithms:
                selected_algorithms.remove(algo)
            else:
                selected_algorithms.append(algo)

    st.write("Selected ML Algorithms:", ", ".join(selected_algorithms))

    # Project theme input
    st.subheader("Enter Project Theme")
    project_theme = st.text_input("What would you like your project to be about? (Press Enter to submit)",
                                  "I want to work on a project related to...")

    # Generate button
    if st.button("Generate Project"):
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