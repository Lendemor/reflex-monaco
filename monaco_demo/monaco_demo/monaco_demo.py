"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from typing import Any

import reflex as rx
from reflex_monaco import monaco, monaco_diff

ORIGINAL_CONTENT = """
# Reflex Monaco Editor Demo

This is a demo file you can edit to test the Monaco Editor.

You can also switch to the other tabs, "Diff" to see a comparison of the changes you made with the original content.

```python
from reflex_monaco import monaco, monaco_diff

@rx.page
def index() -> Any:
    return monaco()
```

"""


class FileState(rx.State):
    """The app state."""

    active_view: str = rx.LocalStorage("edit")

    original_content: str = ORIGINAL_CONTENT
    modified_content: str = ""

    @rx.event
    def load_file_content(self):
        """Load the file content."""
        self.modified_content = self.original_content

    @rx.event
    def on_change(self, value: str):
        """Update the modified content."""
        self.modified_content = value

    @rx.event
    def on_view_change(self, view: str):
        """Update the active view."""
        self.active_view = view


MONACO_WIDTH = "80vw"
MONACO_HEIGHT = "50vh"


def edit_view():
    """The Monaco editor view."""
    return monaco(
        width=MONACO_WIDTH,
        height=MONACO_HEIGHT,
        language="python",
        value=FileState.modified_content,
        default_language="text",
        on_change=FileState.on_change.debounce(1000),
    )


def diff_view():
    """The Monaco diff editor view."""
    return monaco_diff(
        width=MONACO_WIDTH,
        height=MONACO_HEIGHT,
        original=FileState.original_content,
        modified=FileState.modified_content,
        original_language="text",
        modified_language="text",
    )


@rx.page(on_load=FileState.load_file_content)
def index() -> Any:
    """The main page."""
    return rx.vstack(
        rx.box(),
        rx.heading(
            "Monaco Editor Demo",
            size="9",
            align="center",
            text_decoration="underline",
        ),
        rx.code("pip install reflex-monaco"),
        rx.center(
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Edit", value="edit"),
                    rx.tabs.trigger("Diff", value="diff"),
                    size="2",
                ),
                rx.tabs.content(edit_view(), value="edit"),
                rx.tabs.content(diff_view(), value="diff"),
                default_value="edit",
                on_change=FileState.on_view_change,
                value=FileState.active_view,
            ),
        ),
        rx.logo(),
        align="center",
        spacing="6",
        width="100vw",
        height="100vh",
    ), rx.color_mode.button(
        position="top-right",
        allow_system=True,
    )


# Add state and page to the app.
app = rx.App(
    theme=rx.theme(appearance="dark"),
)
