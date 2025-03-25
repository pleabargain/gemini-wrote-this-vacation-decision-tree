import streamlit as st

decision_tree = {
    "question": "What is your budget?",
    "type": "choice",
    "choices": [
        {
            "label": "Under $1000",
            "next": {
                "question": "Do you prefer beaches or mountains?",
                "type": "choice",
                "choices": [
                    {
                        "label": "Beaches",
                        "result": "Consider a local beach vacation."
                    },
                    {
                        "label": "Mountains",
                        "result": "Consider a local hiking trip."
                    }
                ]
            }
        },
        {
            "label": "$1000 - $3000",
            "next": {
                "question": "Do you want to travel internationally?",
                "type": "boolean",
                "trueBranch": {
                    "question": "Do you have a valid passport?",
                    "type": "boolean",
                    "trueBranch": {
                        "question": "Are you interested in cultural experiences?",
                        "type": "boolean",
                        "trueBranch": {
                            "result": "Consider a trip to Europe."
                        },
                        "falseBranch": {
                            "result": "Consider a resort in the Caribbean."
                        }
                    },
                    "falseBranch": {
                        "result": "Explore domestic destinations."
                    }
                },
                "falseBranch": {
                    "question": "What type of vacation are you looking for?",
                    "type": "choice",
                    "choices": [
                        {
                            "label": "Relaxing",
                            "result": "Consider a spa retreat."
                        },
                        {
                            "label": "Adventurous",
                            "result": "Consider a national park visit."
                        }
                    ]
                }
            }
        },
        {
            "label": "Over $3000",
            "next": {
                "question": "What is your dream destination type?",
                "type": "choice",
                "choices": [
                    {
                        "label": "Luxury Beach Resort",
                        "result": "Consider Maldives or Bora Bora"
                    },
                    {
                        "label": "Adventure Safari",
                        "result": "Consider a safari in Africa"
                    },
                    {
                        "label": "World Tour",
                        "result": "Consider a cruise or multi-city tour"
                    }
                ]
            }
        }
    ]
}

def navigate_tree(node, session_state):
    """
    Navigates the decision tree based on user input using Streamlit.

    Args:
        node (dict): The current node in the decision tree.
        session_state (streamlit.runtime.state.SafeSessionState): Streamlit's session state object.
    """
    st.header("Vacation Planner")

    if "result" in node:
        st.success(f"Result: {node['result']}")
        return  # Stop execution after displaying the result

    question = node["question"]
    st.subheader(question)

    if node["type"] == "boolean":
        if f"choice_{question}" not in session_state:
            session_state[f"choice_{question}"] = None

        yes = st.button("Yes", key=f"yes_{question}")  # Add unique keys
        no = st.button("No", key=f"no_{question}")    # Add unique keys

        if yes:
            session_state[f"choice_{question}"] = True
            return navigate_tree(node["trueBranch"], session_state)
        elif no:
            session_state[f"choice_{question}"] = False
            return navigate_tree(node["falseBranch"], session_state)
        else:
            if session_state[f"choice_{question}"] is not None: #check if it is not None
                if session_state[f"choice_{question}"] :
                    return navigate_tree(node["trueBranch"], session_state)
                else:
                    return navigate_tree(node["falseBranch"], session_state)
            else:
                return

    elif node["type"] == "choice":
        labels = [choice["label"] for choice in node["choices"]]
        choice_label = st.radio("Select an option:", labels, key=question)  # Use question as key

        for choice in node["choices"]:
            if choice["label"] == choice_label:
                next_node = choice.get("next")
                result = choice.get("result")
                if next_node:
                    return navigate_tree(next_node, session_state)
                else:
                    st.success(f"Result: {result}")
                    return

def main():
    """
    Main function to run the Streamlit app.
    """
    if "session_state" not in st.session_state:
        st.session_state.session_state = {}
    navigate_tree(decision_tree, st.session_state.session_state)

if __name__ == "__main__":
    main()
