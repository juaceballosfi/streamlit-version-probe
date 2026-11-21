"""Small compatibility check for the Fi Apps Streamlit template."""

import platform

import streamlit as st


@st.fragment
def document_row() -> None:
    name, warnings = st.columns([3, 1])
    if name.button("Sample contract", type="tertiary"):
        st.session_state["document"] = "Sample contract"
        st.switch_page(review_page)
    with warnings.popover("Warnings (1)", icon=":material/warning:"):
        st.write("Example: a field needs review.")


def documents() -> None:
    st.title("Documents")
    document_row()


def review() -> None:
    document = st.session_state.get("document")
    if document is None:
        st.switch_page(documents_page)
    if st.button("Back to Documents", icon=":material/arrow_back:"):
        st.switch_page(documents_page)
    st.title(document)
    st.checkbox("Reviewed")


def export() -> None:
    st.title("Export")
    st.info("This probe uses synthetic data.")


st.set_page_config(page_title="Streamlit compatibility probe")
documents_page = st.Page(documents, title="Documents", default=True)
export_page = st.Page(export, title="Export")
review_page = st.Page(review, title="Review", visibility="hidden")

page = st.navigation([documents_page, export_page, review_page], position="top")
if page is not review_page:
    st.session_state.pop("document", None)

identity_header = "present" if "X-User-Id" in st.context.headers else "absent"
st.caption(
    f"Streamlit {st.__version__} · Python {platform.python_version()}"
    f" · X-User-Id: {identity_header}"
)
page.run()
