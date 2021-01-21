"""
Author : Nathalia Graf Grachet
Date   : 2021-01-18
Purpose: Rosalind App
"""

from subprocess import getstatusoutput
import streamlit as st


# --------------------------------------------------
def main():
    """App"""

    st.title("My Rosalind Answers")

    intro()

    st.write("---")

    topic = get_topic()

    script = get_problem_set(topic)

    file = get_file()

    if file is not None:
        st.write('Output:')
        st.text(run_script(script, file))



# --------------------------------------------------
def intro():
    """More like a promise"""

    st.write("""I made this app to practice my skills, and I really do not
    want this to be misused.""")

    st.write("**You must promise me:**")

    st.write("""1 - You will use this solely for educational purposes to
    improve your own skills, and """)
    st.write("""2 - You will **NOT** use this app to generate
    answers for yourself.""")


# --------------------------------------------------
def get_topic():
    """Get problem set"""

    topic = st.sidebar.selectbox("Select a Topic",
            ('Python Village', 'Bioinformatics Stronghold',
            'Bioinformatics Armory', 'Bioinformatics Textbook Track',
            'Algorithmic Heights'))

    return topic


# --------------------------------------------------
def get_problem_set(t):
    """From major topic, t, display problem sets, p"""

    script = ''
    file = ''

    if t == 'Python Village':
        directory = 'python_village'
        problem = st.sidebar.selectbox('Select Problem Set',
                    ('INI2', 'INI3', 'INI4', 'INI5', 'INI6'))
        script = f"{directory}/{problem.lower()}.py"

    elif t == 'Bioinformatics Stronghold':
        directory = 'bioinformatics_stronghold'
        problem = st.sidebar.selectbox('Select Problem Set',
                    ('DNA', 'RNA', 'REVC', 'FIB', 'GC', 'HAMM'))
        script = f"{directory}/{problem.lower()}.py"

    else:
        st.write('Not available yet.')

    return script


# --------------------------------------------------
def get_file():
    """From major topic, t, display problem sets, p"""

    file = st.sidebar.file_uploader('Input file:', type="txt")

    if file is not None:
        file = file.name
        return file


# --------------------------------------------------
def run_script(s, f):
    """Run the script s with input file f"""

    cmd = f'./{s} data/{f}'

    rv, out = getstatusoutput(cmd)

    return out


# --------------------------------------------------
if __name__ == '__main__':
    main()
